from  __init__ import *
import requests
import re
import time
import random
import os
import json
import logging
from typing import Optional, Dict
from config_manager import ConfigManager, ConfigurationError
from http_client import HTTPClient
from dataclasses import dataclass

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@dataclass
class LoginResult:
    """登录结果数据类"""
    success: bool
    message: str
    headers: Optional[Dict[str, str]] = None

class AnthinkerClient:
    def __init__(self):
        self.config = ConfigManager()
        self.http_client = HTTPClient(base_url=home)
        self._setup_logging()

    def _setup_logging(self):
        self.logger = logging.getLogger(__name__)

    def _extract_form_hash(self, content: str) -> str:
        """从页面内容提取formhash"""
        matches = re.findall(reformhash, content)
        if not matches:
            raise ValueError("无法找到formhash")
        return matches[0]

    def _build_login_cookie(self, headers: Dict[str, str]) -> Dict[str, str]:
        """构建登录cookie"""
        try:
            cookie_data = {
                'saltkey': re.findall(resaltkey, headers["Set-Cookie"])[0],
                'lastvisit': re.findall(relastvisit, headers["Set-Cookie"])[0],
                'sid': re.findall(resid, headers["Set-Cookie"])[0],
                'lastact': re.findall(restact, headers["Set-Cookie"])[0]
            }
            return {f"cRkY_2132_{k}": v for k, v in cookie_data.items()}
        except (KeyError, IndexError) as e:
            raise ValueError(f"提取cookie数据失败: {str(e)}")

    def login(self) -> LoginResult:
        """用户登录"""
        try:
            # 获取初始页面
            initial_response = self.http_client.get("/")
            formhash = self._extract_form_hash(initial_response.text)
            
            # 构建登录数据
            login_data = {
                "formhash": formhash,
                "ident": "user_login",
                "referer": home,
                "username": self.config.credentials.username,
                "password": self.config.credentials.password
            }

            # 设置初始cookie
            initial_cookies = self._build_login_cookie(initial_response.headers)
            self.http_client.update_cookies(initial_cookies)

            # 发送登录请求
            login_response = self.http_client.post(loginurl, data=login_data)
            
            if login_response.ok and "message" in login_response.json():
                self.logger.info(f"登录响应: {login_response.json()['message']}")
                return LoginResult(True, "登录成功", dict(self.http_client.session.headers))
            
            return LoginResult(False, "登录失败", None)

        except Exception as e:
            self.logger.error(f"登录过程出错: {str(e)}")
            return LoginResult(False, str(e), None)

    def registration(self) -> bool:
        """签到功能"""
        try:
            response = self.http_client.get(signhome)
            formhash = self._extract_form_hash(response.text)

            sign_data = {
                "formhash": formhash,
                "signsubmit": "yes",
                "handlekey": "signin",
                "emotid": "1",
                "referer": f"{host}{um}",
                "content": "记上一笔，hold住我的快乐！"
            }

            sign_response = self.http_client.post(signrequest, data=sign_data)
            
            if sign_response.ok:
                self.logger.info("签到成功！")
                return True
            return False

        except ValueError as e:
            self.logger.info("今天已经签到过了！明天再来吧")
            return False
        except Exception as e:
            self.logger.error(f"签到失败: {str(e)}")
            return False

def main():
    try:
        client = AnthinkerClient()
        login_result = client.login()
        
        if login_result.success:
            client.registration()
        else:
            logging.error(f"登录失败: {login_result.message}")

    except ConfigurationError as e:
        logging.error(f"配置错误: {str(e)}")
    except Exception as e:
        logging.error(f"程序执行出错: {str(e)}")

if __name__ == '__main__':
    main()






