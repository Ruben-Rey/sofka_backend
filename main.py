
from crypt import methods
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.secret_key="sofka1234"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'spaceshipsdb'
mysql = MySQL(app)


#################### API REST ########################


#### LISTAR TODAS LAS NAVES #############
@app.route('/naves/lanzadera', methods=['GET'])
def listar_lanzadera():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM lanzadera")
        data = cursor.fetchall()
        lanzadera = []
        for fila in data:
            nave = {'id': fila[0],'nombre': fila[1],'situacion': fila[2],'peso': fila[3],'empuje': fila[4],'combustible': fila[5],'objetivo': fila[6],'pais': fila[7],'fases': fila[8]}
            lanzadera.append(nave)
        print(lanzadera)
        return jsonify({'naves': lanzadera})
    except Exception as ex:
        return jsonify({'messaje': "Error"})

#### BUSCAR NAVE #############
@app.route('/naves/lanzadera/<string:id>', methods=['GET'])
def lista_nave(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM lanzadera WHERE id={id}")
        data = cursor.fetchone()

        nave = {'id': data[0],'nombre': data[1],'situacion': data[2],'peso': data[3],'empuje': data[4],'combustible': data[5],'objetivo': data[6],'pais': data[7],'fases': data[8]}
            
        return jsonify({'naves': nave})
    except Exception as ex:
        return jsonify({'messaje': "Error"})

#### ELIMINAR NAVE #############
@app.route('/naves/lanzadera/<int:id>', methods=['DELETE'])
def eliminar_nave(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(f"DELETE FROM lanzadera WHERE id={id}")
        cursor.connection.commit()
        return jsonify({'messaje': "Nave eliminada"})
    except Exception as ex:
        return jsonify({'messaje': "Error"})


#### CREAR NAVE #############
@app.route('/naves/lanzadera', methods=['POST'])
def agregar_nave():
    # try:
        nombre = request.json['nombre']
        situacion = request.json['situacion']
        peso = request.json['peso']
        empuje = request.json['empuje']
        combustible = request.json['combustible']
        objetivo = request.json['objetivo']
        pais = request.json['pais']
        fases = request.json['fases']
  

        print(nombre)
        
        cursor = mysql.connection.cursor()
        cursor.execute(f"INSERT INTO lanzadera (nombre,situacion,peso,empuje,combustible,objetivo,pais,fases) VALUES ('{nombre}','{situacion}','{peso}','{empuje}','{combustible}','{objetivo}','{pais}','{fases}')")
        cursor.connection.commit()

        
        return jsonify({
            "messaje": "Nave agregada"
        })

    # except Exception as ex:
    #     return jsonify({'messaje': "Error"})
     


#### ACTUALIZAR NAVE #############
@app.route('/naves/lanzadera/<int:id>', methods=['PUT'])
def actualizar_nave(id):
    try:
        nombre = request.json['nombre']
        situacion = request.json['situacion']
        peso = request.json['peso']
        empuje = request.json['empuje']
        combustible = request.json['combustible']
        objetivo = request.json['objetivo']
        pais = request.json['pais']
        fases = request.json['fases']
        
        cursor = mysql.connection.cursor()    
        cursor.execute(f"UPDATE lanzadera SET nombre=\"{nombre}\", situacion=\"{situacion}\", peso=\"{peso}\", empuje=\"{empuje}\", combustible=\"{combustible}\", objetivo=\"{objetivo}\", pais=\"{pais}\", fases=\"{fases}\" WHERE id=\"{id}\"")
        cursor.connection.commit()

        return jsonify({
            "messaje": "Nave modificada"
        })

    except Exception as ex:
        return jsonify({'messaje': "Error"})

def pageNoFound(error):
    return "<h1> La pàgina que intentas buscar no existe...</h1>"

##############################################################



if __name__ == '__main__':
    app.register_error_handler(404, pageNoFound)
    app.run(debug=True, port=3000)