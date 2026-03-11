from django.urls import path
from . import views


app_name = 'configuration'

urlpatterns = [
    path('configuracion/continente/', views.config_continent, name='conf_continent'),
    path('configuracion/continente/registrar/', views.config_continent_register, name='conf_continent_register'),
    path('configuracion/continente/editar/<int:continent_id>', views.config_continent_edit, name='conf_continent_edit'),
    path('configuracion/continente/borrar/<int:continent_id>', views.config_continent_delete, name='conf_continent_delete'),

    # PAISES
    path('configuracion/pais/', views.config_country, name='conf_country'),
    path('configuracion/pais/registrar/', views.config_country_register, name='conf_country_register'),
    path('configuracion/pais/editar/<int:country_id>', views.config_country_edit, name='conf_country_edit'),
    path('configuracion/pais/borrar/<int:country_id>', views.config_country_delete, name='conf_country_delete'),

    # DEPARTAMENTO
    path('configuracion/departamentos/', views.config_department, name='conf_department'),
    path('configuracion/departamentos/registrar/', views.config_department_register, name='conf_department_register'),
    path('configuracion/departamentos/editar/<int:department_id>', views.config_department_edit, name='conf_department_edit'),
    path('configuracion/departamentos/borrar/<int:department_id>', views.config_department_delete, name='conf_department_delete'),

    #MUNICIPIO
    path('configuracion/municipios/', views.config_municipality, name='conf_municipality'),
    path('configuracion/municipios/registrar/', views.config_municipality_register, name='conf_municipality_register'),
    path('configuracion/municipios/editar/<int:municipality_id>', views.config_municipality_edit, name='conf_municipality_edit'),
    path('configuracion/municipios/borrar/<int:municipality_id>', views.config_municipality_delete, name='conf_municipality_delete'),

]