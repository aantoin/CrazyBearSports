from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


from .forms import LoginForm
from .models import Sponsor,Ticker,Update

# Create your views here.
def index(request):
    context = {}
    context['tickers']=Ticker.objects.all()
    context['sponsors']=Sponsor.objects.order_by("?")
    context['updates']=Update.objects.order_by("-created")[:10]
    return render(request, 'home/home.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    invalid_login = False
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            # redirect to a new URL:
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('index')
        invalid_login = True

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form, 'invalid_login': invalid_login})


def logout_page(request):
    logout(request)
    return render(request, 'user/logout.html', {})