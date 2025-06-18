from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from django.contrib import messages
# Home view
def home(request):
    return render(request, 'account/home.html')

# Login view
def login_view(request):
    if request.method == "POST":
        return redirect('customer_dashboard')
    return render(request, 'account/login.html')

# Register view
def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.is_active = False
            user.save()
            messages.success(request,'Registration successfull! Please check your email to activate your account',)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html',{'form':form})

# Password reset view
def password_reset_view(request):
    return render(request, 'account/password_reset.html')

# Password reset confirm view
def password_reset_confirm_view(request, uidb64, token):
    return render(request, 'account/password_reset_confirm.html')
