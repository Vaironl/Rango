from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category


# Create your views here.

def index(request):
    # Query the database for all of the categories
    # Order the categories by the no. of likes in descending order
    # Only retrieve the top 5 categories or all if less than 5
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # return rendered response
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'aboutmessage': "We sell djangos for a rango"}

    return render(request, 'rango/about.html', context=context_dict)
