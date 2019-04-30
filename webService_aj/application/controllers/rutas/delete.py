import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_ruta, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_ruta) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_ruta, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_ruta) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_ruta, **k):

    @staticmethod
    def POST_DELETE(id_ruta, **k):
    '''

    def GET(self, id_ruta, **k):
        message = None # Error message
        id_ruta = config.check_secure_val(str(id_ruta)) # HMAC id_ruta validate
        result = config.model.get_rutas(int(id_ruta)) # search  id_ruta
        result.id_ruta = config.make_secure_val(str(result.id_ruta)) # apply HMAC for id_ruta
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_ruta, **k):
        form = config.web.input() # get form data
        form['id_ruta'] = config.check_secure_val(str(form['id_ruta'])) # HMAC id_ruta validate
        result = config.model.delete_rutas(form['id_ruta']) # get rutas data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_ruta = config.check_secure_val(str(id_ruta))  # HMAC user validate
            id_ruta = config.check_secure_val(str(id_ruta))  # HMAC user validate
            result = config.model.get_rutas(int(id_ruta)) # get id_ruta data
            result.id_ruta = config.make_secure_val(str(result.id_ruta)) # apply HMAC to id_ruta
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/rutas') # render rutas delete.html 
