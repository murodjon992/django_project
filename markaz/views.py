from django.shortcuts import redirect,render


def HOME(request):
    return  render(request, 'home.html')
def MASTER(request):
    return  render(request, 'admin/auth_login.html')