#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#cantina challenge

import json
import requests

DOCUMENT_URL = "https://raw.githubusercontent.com/jdolan/quetoo/master/src/cgame/default/ui/settings/SystemViewController.json"

def getDocument(url):
    return requests.get(url).json()

def findLabel():
    pass
    
def harness():
    while True:
        query = input("Enter query, or \"EXIT\" to quit\n> ")
        if query == "EXIT":
            break
        
if __name__ == "__main__":
    print ((getDocument(DOCUMENT_URL)))
    #harness()
    
    