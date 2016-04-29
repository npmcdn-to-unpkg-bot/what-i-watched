def formHelper(visual, request):
    title = request.POST.get('title')
    original_title = request.POST.get('original_title')
    douban_id = request.POST.get('douban_id')
    year = request.POST.get('year')
    rating = request.POST.get('rating')
    images = request.POST.get('images')
    summary = request.POST.get('summary')
    visual.title = title
    visual.original_title = original_title
    visual.douban_id = douban_id
    visual.year = int(year)
    visual.rating = float(rating)
    visual.images = images
    visual.summary = summary
    return visual