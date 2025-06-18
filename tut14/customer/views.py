from django.shortcuts import render

def customer_dashboard_view(request):
    return render(request, 'customer/dashboard.html')

def password_change_view(request):
    return render(request, 'customer/password_change.html')
