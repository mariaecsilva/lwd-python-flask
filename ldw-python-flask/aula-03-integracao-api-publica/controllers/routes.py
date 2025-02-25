from flask import render_template, request, redirect, url_for;
import urllib; #Lê uma determinada url
import json; #Converte dados para o formato json

jogadores=[]
gamelist = [{
            'titulo' : 'CS-go',
            'ano' : 2012,
            'categoria' : 'FPS Online'
        }]
        

def init_app(app):
    # Criando a primeira rota da aplicação
    @app.route('/')
    # View function -> função de visualização
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game=gamelist[0]
        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
                return redirect(url_for('games'))

        return render_template('games.html',
                                game=game,
                                jogadores=jogadores)
    
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            form_data=request.form.to_dict()
            gamelist.append(form_data)
            return redirect(url_for('cadgames'))

        return render_template('cadgames.html', gamelist=gamelist)
    
    @app.route('/apigames', methods=['GET', 'POST']) 
    @app.route('/apigames/<int:id>', methods=['GET', 'SET'])
    def apigames(id=None): #Definindo que o parametro é opcional
        url='https://www.freetogame.com/api/games'
        response = urllib.request.urlopen(url)
        #print(response) teste para ver se retorna
        data=response.read()
        gamesjson=json.loads(data) #Transforma o json em um objeto python para manipulação
        if id:
            gameInfo=[]
            for gameInfo in gamesjson:
                if gameInfo['id'] == id:
                    gameInfo=gameInfo
                    break
                if gameInfo:
                    return render_template('gameinfo.html', gameInfo=gameInfo)
                else: 
                    return f'Game com a id {id} não encontrado.' 
        return render_template('apigames.html', gamesjson=gamesjson)