from django.urls import path
from .vistas import Saludo_View, Familiar_View

urlpatterns = [
    path('saludo', Saludo_View.saludo),
    path('autogenerar_listar_familiares', Familiar_View.autogenerar_listar_familiares),
    path('crear', Familiar_View.crearFamiliar, name="crear"),
    path('listar', Familiar_View.listar_familiares, name="listar"),
    path('modificar', Familiar_View.modificar_familiar, name="editar"),
    path('modificar/<int:id>', Familiar_View.modificar_familiar),
    path('eliminar/<int:id>', Familiar_View.borrar_familiar)
]