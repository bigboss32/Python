from App import app
from config import config
from flask_wtf.csrf import CSRFProtect
from flask import redirect,url_for

csrf = CSRFProtect()
def status_401(error):

    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__=="__main__":
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()