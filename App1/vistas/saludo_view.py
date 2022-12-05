from django.shortcuts import render

class saludo_view:

    def saludo(request):
        return render(request, 'saludo.html')