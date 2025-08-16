import requests
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
import ssl

class ArcherTLSAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        ctx = ssl.create_default_context()
        ctx.set_ciphers("ECDHE+AESGCM:ECDHE+CHACHA20")
        kwargs["ssl_context"] = ctx
        return super().init_poolmanager(*args, **kwargs)
