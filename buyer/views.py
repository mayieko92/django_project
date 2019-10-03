from django.shortcuts import render
from django.contrib.auth.decorators import login_required

posts = [
    {
        'image': 'Example Of Jeans',
        'timer': '6Hrs 24mins',
        'content': 'Blue Jeans',
        'category': 'Jeans',
        'budget': '5,000',
        'location': '10Km',
    },
]

@login_required
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'buyer/home.html', context)


@login_required
def how_it_works(request):
    return render(request, 'buyer/howitworks.html', {'title': 'How It Works'})


@login_required
def my_purchases(request):
    return render(request, 'buyer/mypurchases.html', {'title': 'My Purchases'})


@login_required
def popular_products(request):
    return render(request, 'buyer/popularproducts.html', {'title': 'Popular Products'})


@login_required
def my_profile(request):
    return render(request, 'buyer/myprofile.html', {'title': 'My Profile'})