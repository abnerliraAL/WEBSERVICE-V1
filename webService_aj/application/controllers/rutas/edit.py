import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_ruta, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_ruta) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_ruta, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_ruta) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_ruta, **k):

    @staticmethod
    def POST_EDIT(id_ruta, **k):
        
    '''

    def GET(self, id_ruta, **k):
        message = None # Error message
        id_ruta = config.check_secure_val(str(id_ruta)) # HMAC id_ruta validate
        result = config.model.get_rutas(int(id_ruta)) # search for the id_ruta
        result.id_ruta = config.make_secure_val(str(result.id_ruta)) # apply HMAC for id_ruta
        return config.render.edit(result, message) # render rutas edit.html

    def POST(self, id_ruta, **k):
        form = config.web.input()  # get form data
        form['id_ruta'] = config.check_secure_val(str(form['id_ruta'])) # HMAC id_ruta validate
        # edit user with new data
        result = config.model.edit_rutas(
            form['id_ruta'],form['nombre'],form['punto_inicio'],form['punto_final'],form['hora_inicio_labor'],form['hora_final_labor'],form['transcurso'],form['costo'],form['url_ruta'],
        )
        if result == None: # Error on udpate data
            id_ruta = config.check_secure_val(str(id_ruta)) # validate HMAC id_ruta
            result = config.model.get_rutas(int(id_ruta)) # search for id_ruta data
            result.id_ruta = config.make_secure_val(str(result.id_ruta)) # apply HMAC to id_ruta
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/rutas') # render rutas index.html
