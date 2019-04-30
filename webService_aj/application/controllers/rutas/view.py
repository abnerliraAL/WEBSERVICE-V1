import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, id_ruta):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_ruta) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_ruta):
    '''

    def GET(self, id_ruta):
        id_ruta = config.check_secure_val(str(id_ruta)) # HMAC id_ruta validate
        result = config.model.get_rutas(id_ruta) # search for the id_ruta data
        return config.render.view(result) # render view.html with id_ruta data
