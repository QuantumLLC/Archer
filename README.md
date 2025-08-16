# Archer

**Archer** is a headless, browser-like HTTP client that emulates modern browsers.  
It handles realistic TLS fingerprints, randomized headers, and session cookies.  

```python
from archer import ArcherSession

s = ArcherSession(browser="chrome", version="122")
r = s.get("https://example.com")
print(r.status_code, r.text[:200])
```

---
- `pip install .` to install locally  
- `pip install git+https://github.com/QuantumLLC/Archer`

**ONLY `pip install archerfr` IS REAL DO NOT TRUST THEM FAKES**
