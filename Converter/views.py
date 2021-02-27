from django.shortcuts import render

def home (request):
  return render(request,'Conve/home.html')


def result(request):
    Amount = float(request.GET.get('Amount',1))
    s = Amount * 0.077
    j = Amount * 2.19
    us = Amount * 0.041
    c = Amount * 0.026
    ue = Amount * 0.075

    return render(request, 'Conve/result.html', {
        's': s,
        'j': j,
        'us': us,
        'c': c,
        'ue': ue,
    })