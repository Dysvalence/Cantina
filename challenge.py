#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#cantina challenge

import requests
import pprint


CAN_CONTAIN = ["subviews", "contentView", "input", "control"]

DOCUMENT_URL = "https://raw.githubusercontent.com/jdolan/quetoo/master/src/cgame/default/ui/settings/SystemViewController.json"

IDENTIFIER = "identifier"
CLASSNAMES = "classNames"
CLASS = "class"


def getDocument(url):
    return requests.get(url).json()


def multipleSelectorSearch(query, doc):
    if '#' in query and query[0] != '#' and query[-1] != '#':
        s = query.split("#")
        return search(("#" + s[1]), search(s[0],doc))             
                       
    if '.' in query and query[0] != '.' and query[-1] != '.':
        s = query.split(".")
        return search(("." + s[1]), search(s[0],doc)) 
    
    return(search(query, doc))


def search(query, doc):

    def helper(query, doc, querytype):
        retval = []
        
        if isinstance(doc, list):
            for x in doc:
                if isinstance(x, dict):
                    retval.extend(helper(query, x, querytype))
                
        if isinstance(doc, dict):
            if querytype in doc:
                #todo: this is causing duplicates when chaining classes and classNames
                if isinstance(doc[querytype], list):
                    for x in doc[querytype]:
                        if x == query:
                            retval.append(doc)
                elif doc[querytype] == query:
                    retval.append(doc)

            for x in CAN_CONTAIN:
                if x in doc and doc[x] is not None and len(doc[x])!=0:
                    retval.extend(helper(query, doc[x], querytype))
            
        return retval 
        
    if query[0] == "#":
        return helper(query[1:], doc, IDENTIFIER)
    elif query[0] == ".": 
        return helper(query[1:], doc, CLASSNAMES) 
    else: 
        return helper(query, doc, CLASS)


def prettyprint(views):
    for x in views:
        pprint.pprint(x)
        print("\n")
        
    
def harness(doc):
    while True:
        query = input("Enter query, or \"EXIT\" to quit\n> ")      
        if query == "EXIT":
            break    
        views = multipleSelectorSearch(query, doc)
        if len(views) == 0:
            print("QUERY NOT FOUND")
        else:
            prettyprint(views)
  
        
if __name__ == "__main__":
    harness(getDocument(DOCUMENT_URL))
    
    