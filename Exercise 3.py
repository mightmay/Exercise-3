# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 02:37:36 2019

"""

from lxml import html
import requests


while True:
    twitterurl = input("Enter Twitter URL: ")
    url = twitterurl
    
    # request Twitter web page
    page = requests.get(url)
    tree = html.fromstring(page.content)

    # search for the Profile Nav Bar using Xpath
    navBar = tree.xpath('//span[@class="ProfileNav-value"]/text()')
    
    # the follower number is 3rd item
    number_follower=navBar[2]
    
    # print the follower
    print("Follower:" ,str(number_follower))