from flask import Flask, render_template
from controllers import routes;

# Criando a instância do Flask na variável app
app = Flask(__name__, template_folder='views') # Representa o nome do arquivo

routes.init_app(app)
    
# Iniciar o servidor
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)