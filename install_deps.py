import os, sys, subprocess

PACKAGES = [
    "ai4free==0.7",
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

if __name__ == "__main__":
    # حتى لا يثبت كل مرة إذا تم التثبيت سابقًا (مهم على منصات فيها disk persistent)
    marker = "/tmp/deps_installed.marker"
    if os.path.exists(marker):
        print("Dependencies already installed.")
        sys.exit(0)

    print("Installing extra dependencies...")
    pip_install(PACKAGES)
    open(marker, "w").write("ok")
    print("Done.")
