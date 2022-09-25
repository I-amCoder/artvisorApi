from urllib import request

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
import os


def index(request):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

    chrome_options = Options()
    # # pr = '75.119.206.48:15745'
    # options.add_argument(f'user-agent={user_agent}')
    # options.binary_location = os.environ.get('GOOGLE_CHROME_BIN ')
    # # options.add_argument('--proxy-server=%s' % pr)
    # options.headless = True

    # Instantiate a webdriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get(
        "CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    # Load the HTML page
    link = request.GET.get(
        'url', 'https://art.co/search?query=artist&type=artworks')
    driver.get(link)

    # Parse processed webpage with BeautifulSoup
    soup = BeautifulSoup(driver.page_source)
    driver.quit()
    data = soup.find('script', {'id': '__NEXT_DATA__',
                                'type': 'application/json'}).text
    return JsonResponse(json.loads(data))
