from setuptools import setup, find_packages

setup(
    name="archerfr",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "httpx",
        "tls-client",
        "fake-useragent",
        "undetected-chromedriver"
    ],
    python_requires=">=3.7",
    author="QuantumLLC",
    description="Archer - Smart browser-like HTTP client",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/QuantumLLC/Archer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)
