import web
import config

db = config.db


def get_all_rutas():
    try:
        return db.select('rutas')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_rutas(id_ruta):
    try:
        return db.select('rutas', where='id_ruta=$id_ruta', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_rutas(id_ruta):
    try:
        return db.delete('rutas', where='id_ruta=$id_ruta', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_rutas(nombre,punto_inicio,punto_final,hora_inicio_labor,hora_final_labor,transcurso,costo,url_ruta):
    try:
        return db.insert('rutas',nombre=nombre,
punto_inicio=punto_inicio,
punto_final=punto_final,
hora_inicio_labor=hora_inicio_labor,
hora_final_labor=hora_final_labor,
transcurso=transcurso,
costo=costo,
url_ruta=url_ruta)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_rutas(id_ruta,nombre,punto_inicio,punto_final,hora_inicio_labor,hora_final_labor,transcurso,costo,url_ruta):
    try:
        return db.update('rutas',id_ruta=id_ruta,
nombre=nombre,
punto_inicio=punto_inicio,
punto_final=punto_final,
hora_inicio_labor=hora_inicio_labor,
hora_final_labor=hora_final_labor,
transcurso=transcurso,
costo=costo,
url_ruta=url_ruta,
                  where='id_ruta=$id_ruta',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
