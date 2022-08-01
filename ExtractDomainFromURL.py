import re


def domain_name(url):
    pattern = "/\/(.*?).\"
    domain = re.search(pattern, str(url)).group(1)
    print(domain)

domain_name("http://google.com")