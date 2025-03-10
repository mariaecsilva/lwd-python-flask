from flask import render_template, request, redirect, url_for
import urllib
import json

productlist = []  
product_id_counter = 1  

def init_app(app):

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/catalog', methods=['GET'])
    def catalog():
        url = 'https://fakestoreapi.com/products'
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        try:
            response = urllib.request.urlopen(req)
            data = response.read()
            productsjson = json.loads(data)
        except urllib.error.HTTPError as e:
            return f"Erro ao acessar a API: {e}"

        all_products = productsjson + productlist
        
        return render_template('catalog.html', productsjson=all_products)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        global product_id_counter 
        if request.method == 'POST':
            title = request.form.get('title')
            value = request.form.get('value')
            category = request.form.get('category')
            description = request.form.get('description')
            image = request.form.get('image')
            
            if title and value and category and image:
                productlist.append({
                    'id': product_id_counter, 
                    'title': title,
                    'value': value,
                    'category': category,
                    'description': description,
                    'image': image
                })
                product_id_counter += 1 
            return redirect(url_for('catalog'))  

        return render_template('register.html', productlist=productlist)

    @app.route('/product/<int:id>', methods=['GET'])
    def product(id):
        product_info = next((prod for prod in productlist if prod['id'] == id), None)

        if product_info:
            return render_template('product.html', productInfo=product_info)
        else:
            return f'Produto com a id {id} não encontrado.'
