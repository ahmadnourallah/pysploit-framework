import sys, urllib.request
from bs4 import BeautifulSoup
from utilities.color import *
from core.module_obtainer import obtainer

# information
info = {
        'author'            :'Ahmad Nourallah',
        'date'              :'2017/6/5',
        'rank'              :'Good',
        'category'          :'Excellent',
        'path'              :'module/gather/ip_lookup.py',
        'license'           :'GPL V3',
        'description'       :'module to make whois on specific target',
        'references'        :['www.crummy.com/software/BeautifulSoup/bs4/doc/']
}
options = {
        'target'                :['Yes', 'use to set target','']
}
required = {
        'check_required'        :'False',
        'start_required'        :'True'
}

def exploit():
    """ main exploit function """
    try:
        url = "https://dig.whois.com.au/ip/" + obtainer.options['target'][2]
        openurl = urllib.request.urlopen(url)
        html_content = str(openurl.read(100000000))
        soup = BeautifulSoup(html_content, 'html.parser')
        for i in soup.find_all("td", attrs={"data-label": "Country"}):
            print(red("# IP Country:\n            ") + i.text)
        for i in soup.find_all("td", attrs={"data-label": "ASN"}):
            print(red("# IP ASN:\n            ") + i.text)
    except urllib.error.HTTPError:
        print(red("\n[!]") + " Enter the realy target.\n")
    except TypeError:
        print(red("\n[!]") + " target option is require.\n")
    except IndexError:
        print('\n' + red('[!]') + green(' You') + " should enter the target option\n")
    except urllib.error.URLError:
        print('\n' + red("[!]") + " check your internet connection.\n")
