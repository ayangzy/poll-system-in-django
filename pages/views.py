from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Contestant


# Create your views here.


def index(request):

    return render(request, 'pages/index.html')


@login_required(login_url='accounts/login')
def contestants(request):
    cons = Contestant.objects.all
    return render(request, 'pages/contestants.html', {'cons': cons})


@login_required(login_url='accounts/login')
def vote(request, contestant_id):
    if request.method == 'POST':
        cons = get_object_or_404(Contestant, pk=contestant_id)
        cons.votes_total += 1
        cons.save()
        auth.logout(request)
        return redirect('index')
