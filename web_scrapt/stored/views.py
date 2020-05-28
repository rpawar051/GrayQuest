from django.http import HttpResponse
from django.shortcuts import render
from stored.models import Web_data

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
# import lxml

def value(urllink="https://websites.co.in/sitemap"):
    html = requests.get(urllink)
    return BeautifulSoup(html.content, "lxml")


# Create your views here.
def scrapt(request):
    postdata = request.POST

    if request.method =="POST":
        d_link = postdata.get("url_link")
        html = requests.get(d_link)
        bsObj = BeautifulSoup(html.content, "lxml")

        data = {
            "a_tag": bsObj.findAll("a"),
            "p_tag": bsObj.findAll("p"),
            "img_tag": bsObj.findAll("img"),
            "h1_tag": bsObj.findAll("h1"),
            "h2_tag": bsObj.findAll("h2"),
            "h3_tag": bsObj.findAll("h3"),
            "h4_tag": bsObj.findAll("h4"),
            "h5_tag": bsObj.findAll("h5"),
            "table_tag": bsObj.findAll("table")
        }
    else:
        html = requests.get("https://websites.co.in/sitemap")
        bsObj = BeautifulSoup(html.content, "lxml")

        data = {
            "a_tag": bsObj.findAll("a"),
            "p_tag": bsObj.findAll("p"),
            "img_tag": bsObj.findAll("img"),
            "h1_tag": bsObj.findAll("h1"),
            "h2_tag": bsObj.findAll("h2"),
            "h3_tag": bsObj.findAll("h3"),
            "h4_tag": bsObj.findAll("h4"),
            "h5_tag": bsObj.findAll("h5"),
            "table_tag": bsObj.findAll("table")
        }
    return render(request, 'index.html', data)

def insert(request):
    bsObj = value("https://websites.co.in/sitemap")
    insert_value = ""
    for j in range(1, 11):
        # business_name, link, category, city = ""
        business_name = bsObj.findAll("table")[0].findAll("tr")[j].findAll("td")[0].get_text().strip()

        e = bsObj.findAll("table")[0].findAll("tr")[j].findAll("td")[0].findAll("a")
        for i in e:
            if 'href' in i.attrs:
                link = i.attrs['href']

        category = bsObj.findAll("table")[0].findAll("tr")[j].findAll("td")[1].get_text()
        city = bsObj.findAll("table")[0].findAll("tr")[j].findAll("td")[2].get_text()
        Web_data.objects.create(business_name = business_name, web_url = link, category = category, city = city)
        # print(insert_value)

    all_data = Web_data.objects.all()
    # all_data.delete()
    data = {
        "output_data":  all_data
    }
    return render(request, 'list.html', data)