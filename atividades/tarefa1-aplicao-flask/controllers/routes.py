from flask import render_template, request, redirect, url_for;
import urllib
import json

records=[]

def init_app(app):

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            title = request.form.get('title')
            price = request.form.get('price')
            time = request.form.get('time')

            if request.form.get('title'):
                records.append({'title': title, 'price': price, 'time': time})
                return redirect(url_for('register'))
        
        return render_template('register.html', records=records)

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