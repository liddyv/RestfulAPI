from django.shortcuts import render
from accounts.models import Account


def index(request):
    accounts = Account.objects.all()
    return render(request, 'index.html', {
        'accounts': accounts
    })


def api_first_index(request):
    return render(request, 'api-first-index.html')
