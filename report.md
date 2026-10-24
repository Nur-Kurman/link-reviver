# Link Report

Checked 17 link(s).

- Ok: status code(200), URL: https://www.python.org
- Ok: status code(200), URL: https://github.com
- Ok: status code(200), URL: https://httpbin.org/status/200
- Dead: status code(404), URL: https://httpbin.org/status/404, Archive: https://web.archive.org/web/*/https://httpbin.org/status/404
- Dead: status code(410), URL: https://httpbin.org/status/410, Archive: https://web.archive.org/web/*/https://httpbin.org/status/410
- Dead: status code(404), URL: https://www.python.org/this-page-does-not-exist, Archive: https://web.archive.org/web/*/https://www.python.org/this-page-does-not-exist
- Redirect: status code(302), URL: https://httpbin.org/redirect/1 redirects to /get
- Redirect: status code(302), URL: https://httpbin.org/redirect/20 redirects to /relative-redirect/19
- Redirect: status code(301), URL: http://github.com redirects to https://github.com/
- Error: Connection failed (bad domain or offline), URL: https://this-domain-definitely-does-not-exist-12345.com
- Error: Time out, URL: https://httpbin.org/delay/15
- Dead: status code(403), URL: https://httpbin.org/status/403, Archive: https://web.archive.org/web/*/https://httpbin.org/status/403
- Dead: status code(500), URL: https://httpbin.org/status/500, Archive: https://web.archive.org/web/*/https://httpbin.org/status/500
- Dead: status code(418), URL: https://httpbin.org/status/418, Archive: https://web.archive.org/web/*/https://httpbin.org/status/418
- Error: Missing scheme (did you forget http(s)://?), URL: python.org
- Error: SSL certificate error, URL: https://expired.badssl.com
- Error: SSL certificate error, URL: https://self-signed.badssl.com
