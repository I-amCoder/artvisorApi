from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json


def index(request):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

    options = Options()
    options.add_argument(f'user-agent={user_agent}')
    options.headless = True
    # Instantiate a webdriver
    driver = webdriver.Chrome(options=options)
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
