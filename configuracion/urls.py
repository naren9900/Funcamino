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

    # DEPARTAMENTO
    path('configuracion/departamentos/', views.config_departamentos, name='conf_departamento'),
    path('configuracion/departamentos/registrar/', views.config_departamentos_registrar, name='conf_departamento_registrar'),
    path('configuracion/departamentos/editar/<int:departamento_id>', views.config_departamentos_editar, name='conf_departamento_editar'),
    path('configuracion/departamentos/borrar/<int:departamento_id>', views.config_departamentos_borrar, name='conf_departamento_borrar'),

    #MUNICIPIO
    path('configuracion/municipios/', views.config_municipios, name='conf_municipio'),
    path('configuracion/municipios/registrar/', views.config_municipios_registrar, name='conf_municipio_registrar'),
    path('configuracion/municipios/editar/<int:municipio_id>', views.config_municipios_editar, name='conf_municipio_editar'),
    path('configuracion/municipios/borrar/<int:municipio_id>', views.config_municipios_borrar, name='conf_municipio_borrar'),

]