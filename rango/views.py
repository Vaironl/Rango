from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category, Page


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


def show_category(request, category_name_slug):
    # Create context dictionary which we can pass to the rendering engine
    context_dict = {}

    try:
        # Can we find a category name slug with the given name
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all associated pages
        pages = Page.objects.filter(category=category)

        # Add our result list to the template context under the name pages
        context_dict['pages'] = pages
        # Also add the category object from the database
        # to the context dictionary.
        # We'll use this in the template to verify the category
        # Exists
        context_dict['category'] = category

    except Category.DoesNotExist:
        # If we did not find the specified category don't do anything
        context_dict['category'] = None
        context_dict['pages'] = None

    # Render the response and return it to the client
    return render(request, 'rango/category.html', context_dict)


def about(request):
    context_dict = {'aboutmessage': "We sell djangos for a rango"}

    return render(request, 'rango/about.html', context=context_dict)
