from django.shortcuts import render,redirect
from .forms import UserRegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        print("form")
        form = UserRegisterForm(request.POST)
       
        if form.is_valid():
            
            form.save()
            print("valid")
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})
