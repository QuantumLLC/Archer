import random

UA_TEMPLATES = {
    "chrome": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/{v}.0.0.0 Safari/537.36",
    "firefox": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{v}.0) "
               "Gecko/20100101 Firefox/{v}.0"
}

def get_browser_headers(browser="chrome", version="120"):
    ua = UA_TEMPLATES[browser].format(v=version)
    return {
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }
