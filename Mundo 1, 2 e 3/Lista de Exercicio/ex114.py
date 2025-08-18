# teste_pudim.py

def site_acessivel(url: str = "http://pudim.com.br", timeout: int = 5) -> bool:
    try:
        import requests  # tipo: ignore
        try:
            resp = requests.get(url, timeout=timeout)
            return resp.status_code < 400
        except requests.RequestException:
            return False
    except ImportError:
        import urllib.request
        import urllib.error
        try:
            with urllib.request.urlopen(url, timeout=timeout) as resp:
                return 200 <= resp.getcode() < 400
        except (urllib.error.URLError, urllib.error.HTTPError):
            return False



if site_acessivel():
    print("O site Pudim está acessível.")
else:
    print("Não foi possível acessar o site Pudim deste computador.")