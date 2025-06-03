from dataclasses import dataclass
from typing import Optional
import json
import os
import logging
from pathlib import Path

@dataclass
class Credentials:
    username: str
    password: str

class ConfigurationError(Exception):
    """自定义配置异常类"""
    pass

class ConfigManager:
    _instance: Optional['ConfigManager'] = None
    _credentials: Optional[Credentials] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._credentials is None:
            self._load_config()

    def _load_config(self) -> None:
        """加载配置文件"""
        config_dir = Path(__file__).parent
        test_config = config_dir / 'config_test.json'
        default_config = config_dir / 'config.json'

        try:
            config_path = test_config if test_config.exists() else default_config
            if not config_path.exists():
                raise ConfigurationError("未找到配置文件")

            with config_path.open('r', encoding='utf-8') as f:
                config_data = json.load(f)

            username = config_data.get('username')
            password = config_data.get('password')

            if not username or not password or username == "your_username" or password == "your_password":
                raise ConfigurationError("配置文件中的凭据无效")

            self._credentials = Credentials(username=username, password=password)
            
            logging.info(f"已成功加载配置文件: {config_path.name}")

        except json.JSONDecodeError as e:
            raise ConfigurationError(f"配置文件格式错误: {str(e)}")
        except Exception as e:
            raise ConfigurationError(f"加载配置文件时出错: {str(e)}")

    @property
    def credentials(self) -> Credentials:
        """获取凭据"""
        if self._credentials is None:
            self._load_config()
        return self._credentials 