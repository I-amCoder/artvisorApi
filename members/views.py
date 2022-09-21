from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json


def index(request):
    options = Options()
    # options.headless = True
    # Instantiate a webdriver
    driver = webdriver.Chrome(options=options)
    # Load the HTML page
    link = request.GET.get(
        'url', 'https://art.co/search?query=artist&type=artworks')
    driver.get(link)
    print(link)
    # Parse processed webpage with BeautifulSoup
    soup = BeautifulSoup(driver.page_source)
    # print(soup)
    driver.quit()
    # el = 'script', {'id': '__NEXT_DATA__', 'type': 'application/json'}
    data = soup.find('script', {'id': '__NEXT_DATA__',
                     'type': 'application/json'}).text
    # print(json.dumps(data))
    return JsonResponse(json.loads(data))
