import urllib.request, os, sys

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
BASE = "C:/Users/timwo/WorkBuddy/2026-10-26-10-26-50/cme295"
os.makedirs(BASE, exist_ok=True)

TARGETS = [
    ("https://cme295.stanford.edu/slides/fall26-cme295-lecture1.pdf", "lecture1-slides.pdf"),
    ("https://arxiv.org/pdf/1706.03762v7", "attention-is-all-you-need.pdf"),
]

def fetch(url, timeout=90):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        return urllib.request.urlopen(req, timeout=timeout).read()
    except Exception:
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        return opener.open(req, timeout=timeout).read()

def verify(path):
    try:
        import fitz
        d = fitz.open(path)
        n = d.page_count
        d.close()
        return f"{n} pages"
    except Exception as e:
        return f"verify fail: {e}"

for url, name in TARGETS:
    out = os.path.join(BASE, name)
    try:
        data = fetch(url)
        with open(out, "wb") as f:
            f.write(data)
        print(f"OK  {name}  {len(data)} bytes  {verify(out)}")
    except Exception as e:
        print(f"FAIL {name}  {type(e).__name__}: {str(e)[:180]}")
