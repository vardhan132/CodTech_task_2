import requests
from bs4 import BeautifulSoup

def scan_for_sql_injection(url):
    payload = "' OR '1'='1"
    response = requests.get(f"{url}?id={payload}")
    if "SQL syntax" in response.text:
        print("Possible SQL Injection vulnerability detected!")

def scan_for_xss(url):
    payload = "<script>alert('XSS')</script>"
    response = requests.get(url, params={"q": payload})
    if payload in response.text:
        print("Possible XSS vulnerability detected!")
