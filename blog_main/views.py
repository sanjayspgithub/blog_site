from django.http import HttpResponse
from django.shortcuts import redirect, render
from blogs.models import About, Category, Blog, Social

import random

def home(request):
    blogs = Blog.objects.filter(status='published')
    about = About.objects.get()
    social = Social.objects.all()

    all_ids = list(blogs.values_list('id', flat=True))
    random_ids = random.sample(all_ids, min(4, len(all_ids)))
    featured_blogs = blogs.filter(id__in=random_ids)

    context = {
        'blogs': blogs,
        'featured_blogs': featured_blogs,
        'about': about,
        'social': social,
        'active_category': 'all'
    }
    return render(request, 'home.html', context)


#this form is the django built-in form
# use this for default register form (from django.contrib.auth.forms import UserCreationForm)
from .form import RegistrationForm 

def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {
        'form': form
    }

    return render(request, 'register.html', context)

# ----------------------------------------------------
# there is no need of auth. for login if we use django default login auth. make changes in url.py file no need to write views for login 
# make chnages in setting.py buy adding LOGIN_REDIRECT_URL = 'page we want to redirect' and for logout LOGOUT_REDIRECT_URL = 'home-page'
# --------------------------------------------

import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@csrf_exempt
def ai_suggest(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            prompt = body.get('prompt', '')

            response = requests.post(
                'https://api.groq.com/openai/v1/chat/completions',
                headers={
                    'Authorization': f'Bearer {settings.GROQ_API_KEY}',
                    'Content-Type': 'application/json',
                },
                json={
                    'model': 'llama-3.3-70b-versatile',
                    'max_tokens': 1000,
                    'messages': [{'role': 'user', 'content': prompt}]
                },
                timeout=30
            )

            print("STATUS:", response.status_code)
            print("RESPONSE:", response.text)

            data = response.json()
            text = data['choices'][0]['message']['content']
            return JsonResponse({'result': text})

        except Exception as e:
            print("EXCEPTION:", str(e))
            return JsonResponse({'error': str(e)}, status=500)
        