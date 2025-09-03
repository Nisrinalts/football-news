from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406354000',
        'name': 'Nisrina Fatimah',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
