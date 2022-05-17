from django.shortcuts import render


# Create your views here.

def table(request):
    return render(request, 'table.html', context={'color': [(i + 1) * 5 for i in range(50)]})
