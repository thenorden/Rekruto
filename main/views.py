from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == 'GET':
        name = request.GET.get('name', '')
        message = request.GET.get('message', '')
        return render(request, 'index.html', context={'name': name, 'message': message})
    else:
        return render(request, 'index.html', context={'name': '', 'message': ''})
