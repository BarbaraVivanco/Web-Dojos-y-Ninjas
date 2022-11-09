from dojos_ninjas.models.dojo import Dojo
from dojos_ninjas import app
from flask import render_template, redirect, request

# RUTAS DE LECTURA

@app.route('/')
def raiz():
    return redirect("/dojos")

@app.route('/dojos')
def dojos():
    todos_dojos = Dojo.todos_dojos()
    return render_template('dojos.html', todos_dojos=todos_dojos)


#RUTAS DE CREACION
@app.route('/creardojo', methods=['POST'])
def creardojo():
    print(request.form, "QUE CONTIENE ESTE FORMULARIO?")
    data = {
        "name":request.form['dojo_name']
    }
    Dojo.creardojo(data)
    #Dojo.creardojo(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {"id":dojo_id}
    dojo = Dojo.obtener_un_dojo(data)
    ninjas_de_un_dojo = Dojo.obtener_ninjas_del_dojo(data)
    return render_template('show.html', dojo=dojo, ninjas_de_un_dojo=ninjas_de_un_dojo)