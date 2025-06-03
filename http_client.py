from typing import Optional, Dict, Any
import requests
import logging
from requests.sessions import Session
from urllib.parse import urljoin

class HTTPClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        })

    def _build_url(self, endpoint: str) -> str:
        """构建完整的URL"""
        return urljoin(self.base_url, endpoint)

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """发送GET请求"""
        url = self._build_url(endpoint)
        response = self.session.get(url, **kwargs)
        response.raise_for_status()
        return response

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        """发送POST请求"""
        url = self._build_url(endpoint)
        response = self.session.post(url, **kwargs)
        response.raise_for_status()
        return response

    def update_cookies(self, cookies: Dict[str, str]) -> None:
        """更新会话cookies"""
        self.session.cookies.update(cookies)

    def get_cookies(self) -> Dict[str, str]:
        """获取当前会话的cookies"""
        return dict(self.session.cookies)

    def __enter__(self) -> 'HTTPClient':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close() 