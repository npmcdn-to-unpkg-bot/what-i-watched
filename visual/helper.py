import requests


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
    return visual

# def getIMDB(douban_id):
#     douban_url = 'https://movie.douban.com/subject/' + douban_id
#     page = requests.get(douban_url)
#     tree = html.fromstring(page.content)
#     buyers = tree.xpath('//div[@class="buyer-name"]/text()')
#     imdb_id = douban_id
#     return imdb_id