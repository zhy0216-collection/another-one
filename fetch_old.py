# -*- coding: utf-8 -*-
import gevent.monkey;gevent.monkey.patch_socket()
from gevent.pool import Pool
import codecs
import requests
from redis import Redis
from rq import Queue
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup

from model import OneIssue

q = Queue(connection=Redis())

# q.enqueue_call(func=OneIssue.create,
#                args=(1,[]),
#                timeout=30)

# 1- 176

# url="http://news.qq.com/hanhan/one/one1.htm"

def fetch(i):
    url = "http://news.qq.com/hanhan/one/one%s.htm"%i
    r = requests.get(url)
    if r.status_code == 200:
        d = BeautifulSoup(r.content.decode("gb2312", "ignore"))
        q.enqueue_call( func=OneIssue.create,
                        args=(i,[str(one) for one in d.find_all(class_="ones")])
                      )
    
pool = Pool(50)
pool.map(fetch, xrange(1,176+1))
