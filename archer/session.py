import requests
import random
from .headers import get_browser_headers
from .tls import ArcherTLSAdapter

class ArcherSession(requests.Session):
    def __init__(self, browser="chrome", version="120", proxies=None):
        super().__init__()
        self.headers.update(get_browser_headers(browser, version))
        self.mount("https://", ArcherTLSAdapter())
        if proxies:
            self.proxies.update(proxies)

    def request(self, method, url, **kwargs):
        if "headers" not in kwargs:
            kwargs["headers"] = self.headers
        return super().request(method, url, **kwargs)
