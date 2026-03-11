from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from core.configuration.continent import Continent
from core.configuration.country import Country
from core.configuration.department import Department
from core.configuration.municipality import Municipality

# Create your views here.
# Continent
def config_continent(request):
    # Render  administracion.html
    if request.method == 'GET':

        continents = Continent.objects.all()

        # if usuario_datos.perfiles.consultar_localizacion == False:
        # messages.add_message(request, messages.ERROR, 'No tienes permitido el acceso a ese modulo')
        # return HttpResponseRedirect('/administracion/')

        return render(request, "config_continent.html", {'lista_Continent': continents})

def config_continent_register(request):
    # Render  administracion.html
    if request.method == 'GET':


        # if usuario_datos.perfiles.registrar_localizacion == False:
        # messages.add_message(request, messages.ERROR, 'No tienes permisos para registrar en este modulo')
        # return HttpResponseRedirect('/configuracion/Continent/')

        return render(request, "config_continent_register.html")

    elif request.method == 'POST':
        current_user = request.user
        # usuario_datos = Usuarios_datos.objects.filter(usuario_id=current_user.id).first()

        # if usuario_datos.perfiles.registrar_localizacion == False:
        # messages.add_message(request, messages.ERROR, 'No tienes permisos para registrar en este modulo')
        # return HttpResponseRedirect('/configuracion/Continent/')

        code = request.POST['codigo']
        description = request.POST['descripcion']

        continents = Continent.objects.all()
        continents = continents.filter(code=code)
        if continents.exists():
            messages.error(request, f"Registro ya existe con el código {code}")
            return redirect('configuration:conf_continent_register')

        continent = Continent(
            code = code,
            description = description,
        )
        continent.save()
        messages.info(request, f"Se ha registrado el Continente {description.strip()} satisfactoriamente.")

        return redirect('configuration:conf_continent')

def config_continent_edit(request, continent_id):
    # Render  administracion.html
    if request.method == 'GET':
        continent = Continent.objects.get(pk=continent_id)
        return render(request, "config_continent_edit.html", {'continente': continent})

    elif request.method == 'POST':
        id = request.POST['id']
        continent = Continent.objects.get(pk=continent_id)
        code = request.POST['codigo']
        duplicado = Continent.objects.filter(code=code).exclude(pk=continent_id).exists()
        if continent:
            if continent.id == int(id) and not duplicado :

                continent.code = request.POST['codigo']
                continent.description = request.POST['descripcion']
                continent.save()

                messages.success(request, f"Se ha editado el Continente {continent.description.strip()} satisfactoriamente.")

                return redirect('configuration:conf_continent')

            else:
                messages.error(request, f"Registro ya existe con el código {code}")
                return redirect('configuration:conf_continent_edit', continent_id = continent_id)

def config_continent_delete(request, continent_id):
    if request.method == 'GET':
        continent = Continent.objects.get(pk=continent_id)
        if continent.country_set.all().exists():
            messages.error(request, f"No se puede borrar el continente {continent.description} porque tiene uno o varios pais asociado")
            return redirect('configuration:conf_continent')

        else:
            description = continent.description
            continent.delete()
            messages.success(request,f"Se ha borrado el Continente {description} satisfactoriamente.")
            return redirect('configuration:conf_continent')


# Paises
def config_country(request):
    # Render  administracion.html
    if request.method == 'GET':
        countries = Country.objects.all()
        return render(request, "config_country.html", {'lista_paises': countries})

def config_country_register(request):
    # Render  administracion.html
    if request.method == 'GET':
        continents = Continent.objects.all()
        return render(request, "config_country_register.html", {'lista_continent':continents})

    elif request.method == 'POST':
        continent = request.POST['continente']
        code = request.POST['codigo']
        description = request.POST['descripcion']

        countries = Country.objects.all()
        countries = countries.filter(code=code)
        if countries.exists():
            messages.error(request, f"Registro ya existe con el código {code}")
            return redirect('configuration:conf_country_register')

        country = Country(
            continent = Continent.objects.filter(pk=int(continent)).first(),
            code = code,
            description = description
        )
        country.save()
        messages.info(request, f"Se ha registrado el Pais {description} satisfactoriamente.")
        return redirect('configuration:conf_country')

def config_country_edit(request, country_id):
    # Render  administracion.html
    if request.method == 'GET':
        country = Country.objects.get(pk=country_id)
        continents = Continent.objects.all()

        return render(request, "config_country_edit.html", {'lista_Continent': continents,
                                                             'paises': country,})

    elif request.method == 'POST':
        id = request.POST['id']
        continent = request.POST['continente']
        code = request.POST['codigo']
        description = request.POST['descripcion']
        country = Country.objects.get(pk=country_id)
        duplicado = Country.objects.filter(code = code).exclude(pk=country_id).exists()

        if country:
            if not duplicado:
                country.continent = Continent.objects.filter(pk=int(continent)).first()
                country.code = code
                country.description = description
                country.save()

                messages.success(request,f"Se ha editado el país {country.description.strip()} satisfactoriamente.")
                return redirect('configuration:conf_country')

            else:
                messages.error(request, f"El código {code} ya existe")
                return redirect('configuration:conf_country_edit', country_id = country_id)

def config_country_delete(request, country_id):
    if request.method == 'GET':
        country = Country.objects.get(pk=country_id)
        if country.department_set.all().exists():
            messages.error(request,f"No se puede borrar el país {country.description} porque tiene uno o varios pais asociado")
            return redirect('configuracion:conf_country')

        else:
            description = country.description
            country.delete()
            messages.success(request, f"Se ha borrado el país {description} satisfactoriamente.")
            return redirect('configuration:conf_country')

# Departamentos
def config_department(request):
    # Render  administracion.html
    if request.method == 'GET':
        departments = Department.objects.all()
        return render(request, "config_department.html", {'lista_departamentos': departments})

def config_department_register(request):
    # Render  administracion.html
    if request.method == 'GET':
        countries = Country.objects.all()
        return render(request, "config_department_register.html", {'lista_paises': countries})

    elif request.method == 'POST':

        #current_user = request.user
        country = request.POST['paises']
        code = request.POST['codigo']
        description = request.POST['descripcion']
        departments = Department.objects.all()
        departments = departments.filter(code = code)
        if departments.exists():
            messages.error(request, f"Ya existe un registro con el código {code}")
            return redirect('configuration:conf_department_register')

        department = Department(
            country = Country.objects.filter(pk=int(country)).first(),
            code = code,
            description = description,
        )
        department.save()

        messages.info(request, f"Se ha registrado el Departamento {department.description} satisfactoriamente.")
        return redirect('configuration:conf_department')

def config_department_edit(request, department_id):
    # Render  administracion.html
    if request.method == 'GET':
        department = Department.objects.get(pk=department_id)
        countries = Country.objects.all()

        return render(request, "config_department_edit.html", {'lista_paises': countries,
                                                                    'departamentos': department
                                                                    })
    elif request.method == 'POST':
        #id = request.POST['id']
        country = request.POST['paises']
        code = request.POST['codigo']
        description = request.POST['descripcion']

        department = Department.objects.get(pk=department_id)
        duplicado = Department.objects.filter(code = code).exclude(pk=department_id).exists()

        if department:
            if not duplicado:
                department.country = Country.objects.filter(pk=int(country)).first()
                department.code = code
                department.description = description

                department.save()

                messages.success(request, f"Se ha editado el departamento {department.description.strip()} satisfactoriamente.")
                return redirect('configuration:conf_department')

            else:
                messages.error(request, f"El código del departamento:  {code} ya existe")
                return redirect('configuration:conf_department_edit', departamento_id = department_id)

def config_department_delete(request, department_id):
    if request.method == 'GET':
        department = Department.objects.get(pk=department_id)
        if department.municipality_set.all().exists():
            messages.error(request,f"No se puede borrar el departamento {department.description} porque tiene uno o varios pais asociado")
            return redirect('configuration:conf_department')
        else:
            description = department.description
            department.delete()
            messages.success(request, f"Se ha borrado el departamento {description} satisfactoriamente.")
            return redirect('configuration:conf_department')


# Municipios
def config_municipality(request):
    # Render  administracion.html
    if request.method == 'GET':
        municipalities = Municipality.objects.all()
        return render(request, "config_municipality.html", {'lista_municipios': municipalities})

def config_municipality_register(request):
    # Render  administracion.html
    if request.method == 'GET':
        departments = Department.objects.all()
        return render(request, "config_municipality_register.html", {'lista_departamentos': departments})

    elif request.method == 'POST':
        department = request.POST['departamentos']
        code = request.POST['codigo']
        description = request.POST['descripcion']

        municipalities = Municipality.objects.all()
        municipalities = municipalities.filter(code = code)
        if municipalities.exists():
            messages.error(request, f"Ya existe un registro con el código {code}")
            return redirect('configuration:conf_municipality_register')

        municipality = Municipality(
            department = Department.objects.filter(pk=int(department)).first(),
            code = code,
            description = description,
        )
        municipality.save()

        messages.info(request, f"Se ha registrado el Municipio {description} satisfactoriamente.")
        return redirect('configuration:conf_municipality')

def config_municipality_edit(request, municipality_id):
    # Render  administracion.html
    if request.method == 'GET':
        municipality = Municipality.objects.get(pk=municipality_id)
        departments = Department.objects.all()

        return render(request, "config_municipality_edit.html", {'lista_departamentos': departments,
                                                                 'municipios': municipality,})
    elif request.method == 'POST':

        id = request.POST['id']
        department = request.POST['departamentos']
        code = request.POST['codigo']
        description = request.POST['descripcion']

        municipality = Municipality.objects.get(pk=municipality_id)
        duplicado = Municipality.objects.filter(code = code).exclude(pk=municipality_id).exists()
        if municipality:
            if not duplicado:
                municipality.department = Department.objects.filter(pk=int(department)).first()
                municipality.code = code
                municipality.description = description
                municipality.save()

                messages.success(request,f"Se ha editado el municipio {municipality.description.strip()} satisfactoriamente.")
                return redirect('configuration:conf_municipality')

            else:
                messages.error(request, f"El código del municipio:  {code} ya existe")
                return redirect('configuration:conf_municipality_edit', municipality_id = municipality_id)

def config_municipality_delete(request, municipality_id):
    if request.method == 'GET':
        municipality = Municipality.objects.get(pk=municipality_id)
        description = Municipality.description
        municipality.delete()
        messages.success(request, f"Se ha borrado el municipio {description} satisfactoriamente.")
        return redirect('configuration:conf_municipality')

