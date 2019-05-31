from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import SubscriptionForm
from .models import Subscription

import json
import requests


MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'
members_endpoint = f'{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members'


def subscribe(email):
    data = {
        'email_address': email,
        'status': 'subscribed',
    }
    req = requests.post(
        members_endpoint,
        auth=('', MAILCHIMP_API_KEY),
        data=json.dumps(data),
    )
    return req.status_code, req.json()

def email_list_signup(request):
    form = SubscriptionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email_signup_qs = Subscription.objects. \
                filter(email=form.instance.email)
            if email_signup_qs.exists():
                messages.warning(request, 'You are already on our list!')
            else:
                subscribe(form.instance.email)
                messages.success(request, 'We will notfiy you when we are ready!')
                form.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def home_page(request):
    import os
    print(os.environ.get('MAILCHIMP_API_KEY'))
    form = SubscriptionForm
    context = {
        'form': form,
    }
    return render(request, 'index.html', context=context)
