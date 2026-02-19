from django.urls import path
from . import views


app_name = 'configuracion'

urlpatterns = [
    path('configuracion/continentes/', views.config_continentes, name='conf_continente'),
    path('configuracion/continentes/registrar/', views.config_continentes_registrar, name='conf_continente_registrar'),
    path('configuracion/continentes/editar/<int:continente_id>', views.config_continentes_editar, name='conf_continente_editar'),
    path('configuracion/continentes/borrar/<int:continente_id>', views.config_continentes_borrar, name='conf_continente_borrar'),

    # PAISES
    path('configuracion/pais/', views.config_paises, name='conf_paises'),
    path('configuracion/pais/registrar/', views.config_paises_registrar, name='conf_pais_registrar'),
    path('configuracion/pais/editar/<int:pais_id>', views.config_paises_editar, name='conf_pais_editar'),
    path('configuracion/pais/borrar/<int:pais_id>', views.config_paises_borrar, name='conf_pais_borrar'),

]