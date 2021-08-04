from django.shortcuts import redirect,render
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        next_item_text = request.POST['item_text']
        Item.objects.create(text=next_item_text)
        return redirect('/')

    return render(request, 'home.html')
