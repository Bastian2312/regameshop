from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245005',
        'name': 'Bastian Adiputra Siregar',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)