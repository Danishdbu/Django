from django.shortcuts import render, redirect

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
    return render(request, 'account/register.html')

# Password reset view
def password_reset_view(request):
    return render(request, 'account/password_reset.html')

# Password reset confirm view
def password_reset_confirm_view(request, uidb64, token):
    return render(request, 'account/password_reset_confirm.html')
