#! /usr/bin/env python
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from urlparse import urlsplit
from os.path import basename
import urllib2
import re
import requests
import os
import json
import sys
from django.core import serializers

def zhihu_get_pic(request):
    question_id = '28586345'
    url = 'https://www.zhihu.com/question/' + question_id
    
    page_size = 50
    offset = 0
    url_content = urllib2.urlopen(url).read()
    
    answers = re.findall('h3 data-num="(.*?)"', url_content)
    limits = int(answers[0])
    
    images = ''
    while offset < limits:
        post_url = "http://www.zhihu.com/node/QuestionAnswerListV2"
        params = json.dumps({
            'url_token': int(question_id),
            'pagesize': page_size,
            'offset': offset
        })
        data = {
            '_xsrf': '',
            'method': 'next',
            'params': params
        }
        header = {
            'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
            'Host': "www.zhihu.com",
            'Referer': url
        }
        response = requests.post(post_url, data=data, headers=header)
        answer_list = response.json()["msg"]
        print(answer_list)
        # img_urls = re.findall('img .*?data-original="(.*?_r.*?)"', ''.join(answer_list))
        img_urls = re.findall('img .*?src="(.*?_b.*?)"', ''.join(answer_list))
        for img_url in img_urls:
            try:
                split_list = urlsplit(img_url)
                if split_list[0] == 'https':
                    img = split_list[0] + '://' + split_list[1] + split_list[2]
                    images += '<img src="' + img + '"/>'
            except:
                pass
        offset += page_size
    return HttpResponse(images)
