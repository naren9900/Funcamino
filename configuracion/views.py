from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from configuracion.models import *

# Create your views here.
# Continentes
def config_continentes(request):
    # Render  administracion.html
    if request.method == 'GET':

        lista_continentes = Continentes.objects.all()

        # if usuario_datos.perfiles.consultar_localizacion == False:
        # messages.add_message(request, messages.ERROR, 'No tienes permitido el acceso a ese modulo')
        # return HttpResponseRedirect('/administracion/')

        return render(request, "config_continentes.html", {'lista_continentes': lista_continentes,})
    else:
        pass
def config_continentes_registrar(request):
    # Render  administracion.html
    if request.method == 'GET':


        # if usuario_datos.perfiles.registrar_localizacion == False:
        # messages.add_message(request, messages.ERROR, 'No tienes permisos para registrar en este modulo')
        # return HttpResponseRedirect('/configuracion/continentes/')

        return render(request, "config_continentes_registrar.html")

    elif request.method == 'POST':
        current_user = request.user
        # usuario_datos = Usuarios_datos.objects.filter(usuario_id=current_user.id).first()

        # if usuario_datos.perfiles.registrar_localizacion == False:
        # messages.add_message(request, messages.ERROR, 'No tienes permisos para registrar en este modulo')
        # return HttpResponseRedirect('/configuracion/continentes/')

        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']

        lista_continentes = Continentes.objects.all()
        lista_continentes = lista_continentes.filter(codigo=codigo)
        if lista_continentes.exists():
            messages.error(request, f"Registro ya existe con el código {codigo}")
            return redirect('configuracion:conf_continente_registrar')


        continentes = Continentes(

            codigo=codigo,
            descripcion=descripcion,

        )
        continentes.save()

        messages.info(request, f"Se ha registrado el Continente {descripcion.strip()} satisfactoriamente.")

        return redirect('configuracion:conf_continente')
def config_continentes_editar(request, continente_id):
    # Render  administracion.html
    if request.method == 'GET':
        continente = Continentes.objects.get(pk=continente_id)
        return render(request, "config_continentes_editar.html", {'continente': continente})
    elif request.method == 'POST':
        id = request.POST['id']
        continente = Continentes.objects.get(pk=continente_id)
        lista_continentes = Continentes.objects.all()
        codigo = request.POST['codigo']
        lista_continentes = lista_continentes.filter(codigo=codigo)
        if continente:
            if len(lista_continentes) == 1 and lista_continentes.id == id:

                continente.codigo = request.POST['codigo']
                continente.descripcion = request.POST['descripcion']
                continente.save()

                messages.success(request, f"Se ha editado el Continente {continente.descripcion.strip()} satisfactoriamente.")

                return redirect('configuracion:conf_continente')

            else:
                messages.error(request, f"Registro ya existe con el código {codigo}")
                return redirect('configuracion:conf_continente_editar', continente_id=continente_id)
def config_continentes_borrar(request, continente_id):
    if request.method == 'GET':
        continente = Continentes.objects.get(pk=continente_id)
        if continente.paises_set.all().exists():
            messages.error(request, f"No se puede borrar el continente {continente.descripcion} porque tiene uno o varios pais asociado")
            return redirect('configuracion:conf_continente')

        else:
            description = continente.descripcion
            continente.delete()
            messages.success(request,f"Se ha borrado el Continente {description} satisfactoriamente.")
            return redirect('configuracion:conf_continente')


# Paises
def config_paises(request):
    # Render  administracion.html
    if request.method == 'GET':
        lista_paises = Paises.objects.all()
        return render(request, "config_paises.html", {'lista_paises': lista_paises})
    else:
        pass
def config_paises_registrar(request):
    # Render  administracion.html
    if request.method == 'GET':
        lista_continentes = Continentes.objects.all()
        return render(request, "config_paises_registrar.html", {'lista_continentes': lista_continentes})

    elif request.method == 'POST':
        continentes = request.POST['continentes']
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']

        lista_pais = Paises.objects.all()
        lista_pais = lista_pais.filter(codigo=codigo)
        if lista_pais.exists():
            messages.error(request, f"Registro ya existe con el código {codigo}")
            return redirect('configuracion:conf_pais_registrar')


        paises = Paises(
            continentes_id=int(continentes),
            codigo=codigo,
            descripcion=descripcion,

        )
        paises.save()


        messages.info(request, f"Se ha registrado el Pais {descripcion} satisfactoriamente.")
        return redirect('configuracion:conf_paises')
def config_paises_editar(request, pais_id):
    # Render  administracion.html
    if request.method == 'GET':
        paises = Paises.objects.get(pk=pais_id)
        lista_continentes = Continentes.objects.all()


        return render(request, "config_paises_editar.html", {'lista_continentes': lista_continentes,
                                                             'paises': paises,})
    elif request.method == 'POST':
        id = request.POST['id']
        continentes = request.POST['continentes']
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']
        pais = Paises.objects.get(pk=pais_id)
        duplicado = Paises.objects.filter(codigo=codigo).exclude(pk=pais_id).exists()

        if pais:
            if not duplicado:
                pais.continentes_id = int(continentes)
                pais.codigo = codigo
                pais.descripcion = descripcion
                pais.save()

                messages.success(request,f"Se ha editado el país {pais.descripcion.strip()} satisfactoriamente.")
                return redirect('configuracion:conf_paises')

            else:
                messages.error(request, f"El código {codigo} ya existe")
                return redirect('configuracion:conf_pais_editar', pais_id=pais_id)
def config_paises_borrar(request, pais_id):
    if request.method == 'GET':
        pais = Paises.objects.get(pk=pais_id)
        if pais.departamentos_set.all().exists():
            messages.error(request,f"No se puede borrar el país {pais.descripcion} porque tiene uno o varios pais asociado")
            return redirect('configuracion:conf_paises')

        else:
            description = pais.descripcion
            pais.delete()
            messages.success(request, f"Se ha borrado el país {description} satisfactoriamente.")
            return redirect('configuracion:conf_paises')

# Departamentos
def config_departamentos(request):
    # Render  administracion.html
    if request.method == 'GET':
        lista_departamentos = Departamentos.objects.all()
        return render(request, "config_departamentos.html", {'lista_departamentos': lista_departamentos})
    else:
        pass
def config_departamentos_registrar(request):
    # Render  administracion.html
    if request.method == 'GET':
        lista_paises = Paises.objects.all()
        return render(request, "config_departamentos_registrar.html", {'lista_paises': lista_paises})

    elif request.method == 'POST':

        current_user = request.user

        paises = request.POST['paises']
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']
        lista_departamentos = Departamentos.objects.all()
        lista_departamentos = lista_departamentos.filter(codigo=codigo)
        if lista_departamentos.exists():
            messages.error(request, f"Ya existe un registro con el código {codigo}")
            return redirect('configuracion:conf_departamento_registrar')

        departamentos = Departamentos(
            paises_id=int(paises),
            codigo=codigo,
            descripcion=descripcion,

        )
        departamentos.save()

        messages.info(request, f"Se ha registrado el Departamento {descripcion} satisfactoriamente.")
        return redirect('configuracion:conf_departamento')
def config_departamentos_editar(request, departamento_id):
    # Render  administracion.html
    if request.method == 'GET':
        departamentos = Departamentos.objects.get(pk=departamento_id)
        lista_paises = Paises.objects.all()

        return render(request, "config_departamentos_editar.html", {'lista_paises': lista_paises,
                                                                    'departamentos': departamentos
                                                                    })
    elif request.method == 'POST':
        id = request.POST['id']
        paises = request.POST['paises']
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']

        departamento = Departamentos.objects.get(pk=departamento_id)
        duplicado = Departamentos.objects.filter(codigo=codigo).exclude(pk=departamento_id).exists()

        if departamento:
            if not duplicado:
                departamento.paises_id = int(paises)
                departamento.codigo = codigo
                departamento.descripcion = descripcion

                departamento.save()

                messages.success(request, f"Se ha editado el departamento {departamento.descripcion.strip()} satisfactoriamente.")
                return redirect('configuracion:conf_departamento')

            else:
                messages.error(request, f"El código del departamento:  {codigo} ya existe")
                return redirect('configuracion:conf_departamento_editar', departamento_id=departamento_id)
def config_departamentos_borrar(request, departamento_id):
    if request.method == 'GET':
        departamento = Departamentos.objects.get(pk=departamento_id)
        if departamento.municipios_set.all().exists():
            messages.error(request,f"No se puede borrar el departamento {departamento.descripcion} porque tiene uno o varios pais asociado")
            return redirect('configuracion:conf_departamento')
        else:
            description = departamento.descripcion
            departamento.delete()
            messages.success(request, f"Se ha borrado el departamento {description} satisfactoriamente.")
            return redirect('configuracion:conf_departamento')


# Municipios
def config_municipios(request):
    # Render  administracion.html
    if request.method == 'GET':
        lista_municipios = Municipios.objects.all()
        return render(request, "config_municipios.html", {'lista_municipios': lista_municipios})
    else:
        pass
def config_municipios_registrar(request):
    # Render  administracion.html
    if request.method == 'GET':
        lista_departamentos = Departamentos.objects.all()
        return render(request, "config_municipios_registrar.html", {'lista_departamentos': lista_departamentos})

    elif request.method == 'POST':
        current_user = request.user
        departamentos = request.POST['departamentos']
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']

        lista_municipios = Municipios.objects.all()
        lista_municipios = lista_municipios.filter(codigo=codigo)
        if lista_municipios.exists():
            messages.error(request, f"Ya existe un registro con el código {codigo}")
            return redirect('configuracion:conf_municipio_registrar')

        municipios = Municipios(
            departamentos_id=int(departamentos),
            codigo=codigo,
            descripcion=descripcion,

        )
        municipios.save()

        messages.info(request, f"Se ha registrado el Municipio {descripcion} satisfactoriamente.")
        return redirect('configuracion:conf_municipio')
def config_municipios_editar(request, municipio_id):
    # Render  administracion.html
    if request.method == 'GET':
        municipios = Municipios.objects.get(pk=municipio_id)
        lista_departamentos = Departamentos.objects.all()

        return render(request, "config_municipios_editar.html", {'lista_departamentos': lista_departamentos,
                                                                 'municipios': municipios,})
    elif request.method == 'POST':

        id = request.POST['id']
        departamentos = request.POST['departamentos']
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']

        municipio = Municipios.objects.get(pk=municipio_id)
        duplicado = Municipios.objects.filter(codigo=codigo).exclude(pk=municipio_id).exists()
        if municipio:
            if not duplicado:
                municipio.departamentos_id = int(departamentos)
                municipio.codigo = codigo
                municipio.descripcion=descripcion
                municipio.save()

                messages.success(request,f"Se ha editado el municipio {municipio.descripcion.strip()} satisfactoriamente.")
                return redirect('configuracion:conf_municipio')

            else:
                messages.error(request, f"El código del municipio:  {codigo} ya existe")
                return redirect('configuracion:conf_municipio_editar', municipio_id=municipio_id)



def config_municipios_borrar(request, municipio_id):
    if request.method == 'GET':
        municipio = Municipios.objects.get(pk=municipio_id)
        description = municipio.descripcion
        municipio.delete()
        messages.success(request, f"Se ha borrado el municipio {description} satisfactoriamente.")
        return redirect('configuracion:conf_municipio')

