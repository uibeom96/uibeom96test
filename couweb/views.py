from django.shortcuts import render, get_object_or_404
from couweb.models import Webs, Category

def get_url(request, slug = None):
    current_category = None
    categorys = Category.objects.all()

    if slug is not None:
        current_category = get_object_or_404(Category, slug=slug)
    
    return render(request, "couweb/main.html", {
        "current_category": current_category,
        "categorys": categorys,
        })
