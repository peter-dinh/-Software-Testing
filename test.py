
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import  re
from urllib.parse import *


def vietlinkdangdaydu(website,a):
    try:
        if re.match('^#' ,a):
            return 0
        r = urlsplit(a)
        if r.scheme == '' and (r.netloc != '' or r.path != ''):
            d = urlunsplit(r)
            if re.match('^//' ,d):
                m = re.search('(?<=//)\S+', d)
                d = m.group(0)
                m = "https://"+d
                return m.rstrip('/')
            if re.match('^/{1}', d):
                return (website + a).rstrip('/')
        elif r.scheme == '' and r.netloc == '' and r.path != '':
            return website
        elif r.scheme == 'javascript' or r.scheme == 'mailto' or r.scheme == 'tel':
            print("IGNORE-->" + a )
        else:
            return a.rstrip('/')
    except Exception as e:
        pass


def layradanhsachlink(search):

    # tags = {'a':'href', 'img':'src', 'script':'src', 'link':'href'}
    try:
        req = urllib.request.Request(search)

        res = urllib.request.urlopen(req)
        response = res.read().decode('utf-8')
        soup = BeautifulSoup(response, 'html.parser')

        for link in soup.find_all('img'):
            if link.has_attr('src'):
                p = vietlinkdangdaydu(search, link['src'])
                if p != 0 and str(p) != 'None':
                    kiemtraketnoicualink(search=search, link=p)
   
        for link in soup.find_all('link'):
            if link.has_attr('href'):
                p = vietlinkdangdaydu(search, link['href'])
                if p != 0 and str(p) != 'None':
                    kiemtraketnoicualink(search=search, link=p)
       
        for link in soup.find_all('script'):
            if link.has_attr('src'):
                p = vietlinkdangdaydu(search, link['src'])
                if p != 0 and str(p) != 'None':
                    kiemtraketnoicualink(search=search, link=p)
        
        for link in soup.find_all('a'):
            if link.has_attr('href'):
                p = vietlinkdangdaydu(search, link['href'])
                if p != 0 and str(p) != 'None':
                    kiemtraketnoicualink(search=search, link=p)
                    
    except Exception as e:
        print ('[RELATIVE LINK] ' + "Exception-->{} {}".format(e,search))


def kiemtraketnoicualink(search, link):
    try:
        req = urllib.request.Request(url=link)

        resp = urllib.request.urlopen(req)
        if resp.status in [400, 404, 403, 408, 409, 501, 502, 503]:
            print('[' + search +'] ' + resp.status + " " + resp.reason + "-->" + link )
        else:
            print('[' + search +'] ' + "OK-->" + link)
    except Exception as e:
        print ('[' + search +'] ' + "Exception-->{} {}".format(e,link))
        pass

if __name__ == "__main__":

    layradanhsachlink("http://127.0.0.1:8000")
