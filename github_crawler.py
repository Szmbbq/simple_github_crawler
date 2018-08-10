from urllib import request, parse
from http import cookiejar
from bs4 import BeautifulSoup
import chardet




if __name__ == "__main__":
    # Cookie jar to save cookies
    cookie_jar = cookiejar.CookieJar()
    cookie_handler = request.HTTPCookieProcessor(cookie_jar)
    cookie_opener = request.build_opener(cookie_handler)
    # create header
    header = {}
    header["User-Agent"] = r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    header["Connection"] = "keep-alive"
    # login url
    login_page = "https://github.com/login"
    # create request object
    req = request.Request(login_page, headers=header)
    # send request to login page
    response = cookie_opener.open(req)
    html = response.read()
    # decode and soup the page
    encode_type = chardet.detect(html)
    soup = BeautifulSoup(html.decode(encode_type["encoding"]), "lxml")
    # get auth token
    auth_token = soup.find("input", attrs={"name": "authenticity_token", "type": "hidden"}).get("value")

    # login info object
    login_info = {}
    login_info["commit"] = "Sign in"
    login_info["utf8"] = "✓"
    login_info["authenticity_token"] = auth_token
    login_info["login"] = "username"
    login_info["password"] = "password"
    login_data = parse.urlencode(login_info).encode("utf-8")

    # the real login url (where you post account info)
    login_url = "https://github.com/session"
    login_req = request.Request(url=login_url, data=login_data, headers=header)
    # home page
    home_res = cookie_opener.open(login_req)
    soup = BeautifulSoup(home_res.read().decode(encode_type["encoding"]), "lxml")
    # extract repos
    repos = [li.find("a").get("href") for li in soup.find_all("li", attrs={"class": "public source "})]


    print(repos)