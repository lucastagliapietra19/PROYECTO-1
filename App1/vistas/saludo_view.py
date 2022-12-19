from django.shortcuts import render

class Saludo_View:
    
    def saludo(request):
        return render(request, 'saludo.html')