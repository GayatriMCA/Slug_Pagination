from django.shortcuts import render
from pag_app.models import Blog_Website
from pag_app.forms import Blog_WebsiteForm
from django.views.generic import DetailView
from django.core.paginator import Paginator

# Create your views here.

def Enter_data(request):
    form = Blog_WebsiteForm()
    if request.method == "POST":
        form = Blog_WebsiteForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'Insert.html', {'form':form})

def fetch_data(request):
    data = Blog_Website.objects.all()

    p = Paginator(data, 2)
    page_no = request.GET.get('page')
    page_obj = p.get_page(page_no)

    context = {
        'page_obj':page_obj
    }
    return render(request, 'main.html', context)

class Display_Data(DetailView):
    model = Blog_Website

