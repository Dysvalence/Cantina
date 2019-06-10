#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#cantina challenge

import json
import requests
import pprint
#subview contentview input control can contaain further stuff
# class =/= className, identifier
#

CAN_CONTAIN = ["subviews", "contentView", "input", "control"]

DOCUMENT_URL = "https://raw.githubusercontent.com/jdolan/quetoo/master/src/cgame/default/ui/settings/SystemViewController.json"

def getDocument(url):
    return requests.get(url).json()

def search(query, doc):
    #doc will either be a dict, or a list
    #wait nvm, the nests would be under CAN_CONTAIN
    def helper(query, doc, querytype):
        retval = []
        #print("POOTIS")
        #print(type(doc))
        if isinstance(doc, list):
            #print("list found, len "+str(len(doc)))
            for x in doc:
                if isinstance(x, dict):
                    retval.extend(helper(query, x, querytype))
                else:
                    print ("anomaly"+str(type(x)))
            

        if isinstance(doc, dict):
            #print("dict found")
            #print(doc.keys())

            #if querytype in doc and doc[querytype]==query:
            if querytype in doc:
                if doc[querytype]==query:
                    retval.append(doc)
                    #print("KEY FOUND")
                else:
                    pass
                    #print (doc[querytype])
            for x in CAN_CONTAIN:
                if x in doc and doc[x] is not None and len(doc[x])!=0: # or doc[x] type is idk whatever
                    retval.extend(helper(query, doc[x], querytype))
                    #helper(query, doc[x], querytype, retval)
            
        return retval 
        
    if query[0] == "#":
        return helper(query, doc, "identifier")
    elif query[0] == ".": #classname
        return helper(query, doc, "className")
    else: #class
        return helper(query, doc, "class")


def prettyprint(views):
    for x in views:
        pprint.pprint(x)
        print("\n")
        
    
def harness(doc):
    while True:
        query = input("Enter query, or \"EXIT\" to quit\n> ")      
        if query == "EXIT":
            break    
        views = search(query, doc)
        prettyprint(views)

        
        
        
        
if __name__ == "__main__":
    #pprint.pprint(getDocument(DOCUMENT_URL))
    harness(getDocument(DOCUMENT_URL))
    
    