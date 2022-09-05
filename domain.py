from urllib.parse import urlparse

def get_domain_name(url):
    try:
        return urlparse(url).netloc
    except Exception as e:
        return e.with_traceback


