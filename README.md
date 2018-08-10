# Web Crawler For Github Repos

This is simple web crawler which simulate the user login process and return this user's existing repositories as output.

## Dependencies
1. `BeautifulSoup`
2. `http`
3. `chardet`

## Usage
You need to have a working [Github](https://github.com/) account and replace the `username` and `password` in the script `github_crawler.py`. Then execute it via terminal and should be able to see the result printed out.

## Implementation
1. Create a cookie jar to store your access cookies.
2. Then using the cookie jar you've just created to build an opener. (Urls that you wish to visit should be sent through this opener)
3. Set up headers.
4. Request the [login page](https://github.com/login/) and extract the authenticity token (`value` of an `input` tag named `authenticity_token`, which will be needed for the login form submission in the following step) from response html. 
5. Submit login information to the "real" login url, which is [this](https://github.com/session/).
6. Once logged in, you can extract repositories and do other stuffs.