from django.shortcuts import render


def show_main(request):
    context = {
        'npm': '2406358056',
        'name': 'Christopher Evan Tanuwidjaja',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
