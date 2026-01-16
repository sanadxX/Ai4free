import os, sys, subprocess, importlib

PACKAGES = [
    "ai4free==0.6.8",
    "webscout<2025.10",
    "colorama>=0.4.6",
    "curl_cffi",
    "cloudscraper",
    "tls-client",
    "httpx",
    "beautifulsoup4",
    "lxml",
    "fake-useragent",
    "loguru",
    "termcolor",
    "regex",
    "pydantic",
    "tqdm",
]

def pip_install(pkgs):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-cache-dir", *pkgs])

def has_module(name: str) -> bool:
    try:
        importlib.import_module(name)
        return True
    except Exception:
        return False

if __name__ == "__main__":
    # لو ai4free أو webscout غير موجودين فعلاً، ثبّت كل شيء
    if not has_module("ai4free") or not has_module("webscout"):
        print("Installing dependencies (missing ai4free/webscout)...")
        pip_install(PACKAGES)
    else:
        print("Dependencies look installed (ai4free/webscout import OK).")
