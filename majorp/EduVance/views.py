from django.shortcuts import render, redirect

def main(request):
    return render(request, 'main.html')
def login(request):
    return render(request, 'login.html')
def admin(request):
    return render(request, 'admin.html')