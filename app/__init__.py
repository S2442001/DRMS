from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from flask_mail import Mail


# initalizing extension objects
db=SQLAlchemy()
login_manager=LoginManager()
login_manager.login_view = 'auth.login'  
mail=Mail()

def create_app():
    app=Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    @app.after_request
    def add_header(response):
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response




   # from app.routes import auth ,sos, admin
    from app.routes.auth  import auth as auth_bp
    from app.routes.sos import sos  as sos_bp
    from app.routes.admin import admin as admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(sos_bp)
    app.register_blueprint(admin_bp)

    # app.register_blueprint(auth)
    # app.register_blueprint(sos)
    # app.register_blueprint(admin)


    return app



