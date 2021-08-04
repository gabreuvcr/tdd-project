from django.shortcuts import render
from lists.models import Item

def home_page(request):
    next_item_text = ''
    if request.method == 'POST':
        next_item_text = request.POST['item_text']
        Item.objects.create(text=next_item_text)

    return render(request, 'home.html', {
        'new_item_text': next_item_text,
    })
