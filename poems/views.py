from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from poems.models import Poem
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CreatePoemForm, CreateReviewPoemForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render
from .utils.decorators import require_pro, require_premium, require_account_type

# Декоратор для Free акаунтів
require_free = require_account_type('free')


@require_free
def only_for_free_users(request):
    return render(request, 'free_feature.html')


@require_pro
def upload_image(request):
    return render(request, 'upload.html')


@require_premium
def advanced_analytics(request):
    return render(request, 'analytics.html')


@require_pro
def upload_image(request):
    return render(request, 'upload.html')

@require_premium
def advanced_analytics(request):
    return render(request, 'analytics.html')

def index(request):
    theme = request.user.theme if request.user.is_authenticated else "light"
    return render(request, 'poems/index.html', {'theme': theme})

def index(request):
    theme = "lightre"
    if request.user.is_authenticated:
        theme = request.user.theme
    return render(request, "poems/index.html", {"theme": theme, "now": timezone.now()})

def home(request):
    poems = Poem.objects.all()
    user = request.user

    paginator = Paginator(poems, 3)
    page_number = request.GET.get('page')
    poem_paginated = paginator.get_page(page_number)

    context = {
        "poems": poem_paginated,
        "user": user,
    }
    return render(request, "poems/home.html", context)


@login_required(login_url="poems:home")
def poem_create(request):
    if request.method == "POST":
        form = CreatePoemForm(request.POST)
        if form.is_valid():
            poem = form.save()
            username = request.POST.get('author', None)
            author = get_object_or_404(User, username=username)
            poem.author = author
            poem.save()

    form = CreatePoemForm()
    context = {
        "form": form
    }

    return render(request, "poems/create_poem.html", context)


def poem_detail(request, pk):
    user = request.user

    if request.method == "POST" and user.is_authenticated:
        form = CreateReviewPoemForm(request.POST)
        if form.is_valid():
            review = form.save()
            username = request.POST.get('author_id', None)
            author = get_object_or_404(User, username=username)
            poem = get_object_or_404(Poem, pk=pk)
            review.author_id = author
            review.poem.add(poem)
            review.save()
    if request.method == "POST" and not user.is_authenticated:
        messages.error(
            request,
            'User must be authorized'
        )
    poem = get_object_or_404(Poem, pk=int(pk))
    reviews = poem.review.all()

    context = {
        'poem': poem,
        "reviews": reviews
    }
    return render(request, 'poems/poem.html', context)

from .utils.customizer import apply_theme
from django.shortcuts import redirect

def set_theme(request, theme_name):
    apply_theme(request.user, theme_name)
    return redirect('index')