from django.shortcuts import render
from .models import Publi, Category

# Create your views here.

def blog(request):
    publi = Publi.objects.all()
    return render(request, "blog/blog.html", {'publi':publi})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category':category})