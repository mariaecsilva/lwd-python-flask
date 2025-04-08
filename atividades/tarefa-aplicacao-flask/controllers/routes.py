from flask import render_template, request, redirect, url_for, flash;
from models.database import db, Register
import urllib
import json
import os
import uuid

records=[]

def init_app(app):

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/register', methods=['GET', 'POST'])
    @app.route('/register/delete/<int:id>')
    def register(id=None):
        if id:
            register = Register.query.get(id)
            if register:
                db.session.delete(register)
                db.session.commit()
            return redirect(url_for('register'))

        if request.method == 'POST':
            new_register = Register(
                title=request.form['title'], 
                price=float(request.form['price']), 
                time=float(request.form['time'])
            )
            db.session.add(new_register)
            db.session.commit()
            return redirect(url_for('register'))
        
        else:
            page = request.args.get('page', 1, type=int)
            per_page = 5
            registers_page = Register.query.paginate(page=page, per_page=per_page)
            return render_template('register.html', recordsregister=registers_page)  

    @app.route('/catalog', methods=['GET', 'POST']) 
    @app.route('/catalog/<int:id>', methods=['GET', 'SET'])
    def catalog(id=None): 
        url = 'https://fakestoreapi.com/products'
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = response.read()
            productsjson = json.loads(data)
        if id:
            product=[]
            for product in productsjson:
                if product ['id'] == id:
                    product=product
                    break
                if product:
                    return render_template('product.html', product=product)
                else: 
                    return f'Produto com a id {id} não encontrado.' 
        return render_template('catalog.html', productsjson=productsjson)
    
    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    def edit(id):
        register = Register.query.get(id)
        if request.method == 'POST':
            register.title = request.form['title']
            register.price = request.form['price']
            register.time = request.form['time']
            db.session.commit()
            return redirect(url_for('register'))
        return render_template('registeredit.html', register=register)
    

    FILE_TYPES = set(['png', 'jpg', 'jpeg', 'gif'])
    def arquivos_permitidos(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_TYPES


    @app.route('/galeria', methods=['GET', 'POST'])
    def galeria():
        if request.method == 'POST':
            file = request.files['file']
            if not arquivos_permitidos(file.filename):
                flash("Utilize os tipos de arquivos referentes a imagem.", 'danger')
                return redirect(request.url)
            
            filename = str(uuid.uuid4())
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("Imagem enviada com sucesso!", 'success')
        
        return render_template('galeria.html')
