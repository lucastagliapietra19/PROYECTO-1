from django.shortcuts import render
from App1.modelos import Familiar
from App1.formularios import Familiar_Form
import datetime

class Familiar_View:
    
    def autogenerar_listar_familiares(request):
        fm1 = Familiar.create('luana', 19, datetime.date(2003, 5, 17))
        fm2 = Familiar.create('leandro', 19, datetime.date(2003, 5, 17))
        fm3 = Familiar.create('lucas', 19, datetime.date(2003, 5, 17))

        fm1.save()
        fm2.save()
        fm3.save()

        return render(request, 'autogenerar_listar_familiares.html', {'familiares': [fm1, fm2, fm3]})

    # CRUD = Create, Read, Update, Delete

    ## Create
    def crearFamiliar(request):
        if request.method == 'POST':
            f = Familiar_Form(request.POST)
            if f.is_valid():
                info = f.cleaned_data

                familiar = Familiar.create(info['nombre'], info['edad'], info['fecha_nacimiento'])

                try:
                    familiar.save()
                except Exception as e:
                    print(e)
                    print("No se ha podido guardar el familiar")

                return render(request, 'creado_exitosamente.html')
        elif request.method == 'GET':
            f = Familiar_Form()
            return render(request, 'crear_familiar.html', {'form': f})

    ## Read
    def listar_familiares(request):
        familiares = Familiar.objects.all()
        return render(request, 'listar_familiares.html', {"familiares": familiares})

    ## Update
    def modificar_familiar(request, id=0):
        
        if request.method == 'GET':
            familiar = Familiar.objects.get(id = id)
            form = Familiar_Form().fill_form(familiar)

            return render(request, 'modificar_familiar.html', {'form': form})
        
        elif request.method == 'POST':
            data = Familiar_Form(request.POST)
            if data.is_valid():
                familiar = data.cleaned_data
                Familiar.objects.filter(id = familiar['id']).update(**familiar)
                return render(request, 'modificacion_exitosa.html')
            else:
                return render(request, 'mod_fallida.html')

    ## Delete
    def borrar_familiar(request, id):
        familiar = Familiar.objects.get(id = id)
        familiar.delete()
        return render(request, 'borrado_exitoso.html')