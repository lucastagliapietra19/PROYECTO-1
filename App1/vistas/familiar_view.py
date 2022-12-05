from django.shortcuts import render
from App1.modelos import familiar
import datetime

class familiar_view:

    def autogenerar_listar_familiares(request):
        fm1 = familiar.create('luana', 19,datetime.date(2003, 5, 17))
        fm2 = familiar.create('leandro', 24,datetime.date(1998, 3, 10))
        fm3 = familiar.create('lucas', 30,datetime.date(1992, 1, 19))

        fm1.save()
        fm2.save()
        fm3.save()

        return render(request,'autogenerar_listar_familiares.html',{'familiares': [fm1, fm2, fm3]})