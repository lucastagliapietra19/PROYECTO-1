from django.urls import path
from .vistas import saludo_view, familiar_view

urlpatterns =[
    path('saludo', saludo_view.saludo),
    path('autogenerar_listar_familiares', familiar_view.autogenerar_listar_familiares )
]