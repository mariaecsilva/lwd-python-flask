from flask import Flask, render_template
from controllers import routes
# Importando o model
from models.database import db
# Importando a biblioteca OS (comandos de S.O)
import os

# Criando a instância do Flask na variável app
app = Flask(__name__, template_folder='views')  # Representa o nome do arquivo
routes.init_app(app)

# Permite ler o diretório absoluto de um determinado arquivo
dir = os.path.abspath(os.path.dirname(__file__))

# Passando o diretório do banco ao SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir, 'models/games.sqlite3')

# Iniciar o servidor
if __name__ == '__main__':
    db.init_app(app=app)
    # Cria o banco de dados quando a aplicação é rodada
    with app.test_request_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
