import requests

class LinkChecker:
    def __init__(self, url:str):
        self.url: str = url.strip()
        self.is_alive: bool | None = None
        self.status_code: int | None = None
        self.error: str | None = None
        self.redirect_to: str | None = None

    def check(self) -> None:
        try:
            response = requests.get(
                self.url,
                timeout=10,
                allow_redirects=False,
                headers={"User-Agent": "LinkReviver"}
            )
            self.status_code = response.status_code
            self.is_alive = 200 <= self.status_code < 400

            if 300 <= self.status_code < 400:
                self.redirect_to = response.headers.get("Location")

        except requests.exceptions.Timeout:
            self.error = "Time out"
            self.is_alive = False
        except requests.exceptions.SSLError:
            self.error = "SSL certificate error"
            self.is_alive = False
        except requests.exceptions.ConnectionError:
            self.error = "Connection failed (bad domain or offline)"
            self.is_alive = False
        except requests.exceptions.InvalidURL:
            self.error = "Invalid or mistyped URL"
            self.is_alive = False
        except requests.exceptions.MissingSchema:
            self.error = "Missing scheme (did you forget http(s)://?)"
            self.is_alive = False
        except requests.exceptions.TooManyRedirects:
            self.error = "Too many redirects"
            self.is_alive = False
        except requests.exceptions.RequestException as error:
            self.error = str(error)
            self.is_alive = False

    def summary(self) -> str:
        if self.error:
            return f"Error: {self.error}, URL: {self.url}"
        elif self.is_alive:
            if self.redirect_to:
                return f"Redirect: status code({self.status_code}), URL: {self.url} redirects to {self.redirect_to}"
            else:
                return f"Ok: status code({self.status_code}), URL: {self.url}"
        else:
            wayback = f"https://web.archive.org/web/*/{self.url}"
            return f"Dead: status code({self.status_code}), URL: {self.url}, Archive: {wayback}"

    def __repr__(self):
        return f"LinkChecker({self.url!r}, status={self.status_code}, alive={self.is_alive})"