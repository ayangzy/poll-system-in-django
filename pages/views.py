from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
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
        user_id = request.POST['user_id']
        if request.user.is_authenticated:
            user_id = request.user.id
            has_alreadyvoted = Contestant.objects.all().filter(user_id=user_id)
            if has_alreadyvoted:
                messages.warning(
                    request, 'Sorry! already voted. You can only vote once')
                return redirect('contestants')

        cons = get_object_or_404(Contestant, pk=contestant_id)
        cons.votes_total += 1
        cons.user_id = request.POST['user_id']
        cons.save()
        # auth.logout(request)
        messages.success(
            request, 'You have successfully polled your prefered contestant. Thanks')
        return redirect('contestants')
