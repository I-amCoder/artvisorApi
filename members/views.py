from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
import json


def index(request):
    options = Options()
    options.headless = True
    # ua = UserAgent()

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    # user_agent = ua.random
    # Instantiate a webdriver

    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument(f'user-agent={user_agent}')
    options.headless = True
    options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    # Load the HTML page
    link = request.GET.get(
        'url', 'https://art.co/search?query=artist&type=artworks')
    driver.get(link)
    soup = BeautifulSoup(driver.page_source)
    driver.quit()
    # el = 'script', {'id': '__NEXT_DATA__', 'type': 'application/json'}
    data = soup.find('script', {'id': '__NEXT_DATA__',
                     'type': 'application/json'}).text
    # print(json.dumps(data))
    return JsonResponse(json.loads(data))
