from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .tests import chatbot

def home(request):
    return render(request, 'chatbot/home.html')

def get_response(request):
    user_text = request.GET.get('msg')
    bot_response = chatbot.get_response(user_text)
    return JsonResponse({'response': str(bot_response)})
