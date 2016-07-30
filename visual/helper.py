import requests
import urllib2
import re


def formHelper(visual, request):
    title = request.POST.get('title')
    original_title = request.POST.get('original_title')
    douban_id = request.POST.get('douban_id')
    watched = request.POST.get('watched')
    year = request.POST.get('year')
    rating = request.POST.get('rating')
    images = request.POST.get('images')
    summary = request.POST.get('summary')
    visual.title = title
    visual.original_title = original_title
    visual.douban_id = douban_id
    visual.watched = watched
    visual.year = int(year)
    visual.rating = float(rating)
    visual.images = images
    visual.summary = summary
    visual = get_imdb_id(visual, douban_id)
    return visual

def importHelper(visual, data):
    visual.title = data['title']
    visual.original_title = data['original_title']
    visual.douban_id = data['id']
    visual.watched = True
    visual.year = int(data['year'])
    visual.rating = float(data['rating']['average'])
    visual.images = data['images']['large']
    visual.summary = data['summary']
    visual = get_imdb_id(visual, visual.douban_id)
    return visual

def get_imdb_id(visual, douban_id):
    #get imdb from douban detail page
    url = 'https://movie.douban.com/subject/' + douban_id
    url_content = urllib2.urlopen(url).read()
    answers = re.findall('href="http://www.imdb.com/title/(.*?)"', url_content)
    print(answers)
    if len(answers) > 0:
        visual.imdb_id = answers[0]
    return visual