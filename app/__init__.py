from flask import Flask
from app.models.customer import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    # Importar después de inicializar para evitar circular imports
    from app.controllers.customer_controller import customer_bp
    app.register_blueprint(customer_bp)
    
    with app.app_context():
        db.create_all()
    
    return app