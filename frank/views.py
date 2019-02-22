from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, get_user_model
import requests
# import json
from django.conf import settings

User = settings.AUTH_USER_MODEL


def home(request):
    data = {}
    data['crypto_data'] = get_crypto_data()
    return render(request, 'home.html', data)

def get_crypto_data():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"
    try:
        data = requests.get(api_url).json()
    except Exception as e:
        print(e)
        data = dict()
    return data

from django.core.mail import send_mail
from contact.forms import ContactForm

def contact_page(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            sender_name = contact_form.cleaned_data['name']
            sender_email = contact_form.cleaned_data['email']

            content = "{0} has sent you a new message:\n\n{1}".format(sender_name, contact_form.cleaned_data['content'])
            send_mail('New Enquiry', content, sender_email, ['jeloblistext@gmail.com'])
            return HttpResponseRedirect('success')

    else:
        contact_form = ContactForm()
    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    context = {
        "title":"Contact",
        "content":" Welcome to the contact page.",
        "form": contact_form,
    }
    return render(request, "contact/view.html", context)

def success(request):
    user = request.user
    return render(request, 'contact/success.html', {'contact':user})