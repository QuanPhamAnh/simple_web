from flask import Flask
from ast import Try
from flask import render_template, redirect, url_for, session, request
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

products = [
    {"id": "01", "name" : "Sản phẩm 1", "image" : "img_1.jpg", "price" : "150.000 VND", "desc" : "Sản phẩm này dùng để ...."},
    {"id": "02", "name" : "Sản phẩm 2", "image" : "img_2.jpg", "price" : "150.000 VND", "desc" : "Sản phẩm này dùng để ...."},
    {"id": "03", "name" : "Sản phẩm 3", "image" : "img_3.jpg", "price" : "150.000 VND", "desc" : "Sản phẩm này dùng để ...."},
    {"id": "04", "name" : "Sản phẩm 4", "image" : "img_4.jpg", "price" : "150.000 VND", "desc" : "Sản phẩm này dùng để ...."},
    {"id": "05", "name" : "Sản phẩm 5", "image" : "img_5.jpg", "price" : "150.000 VND", "desc" : "Sản phẩm này dùng để ...."},
    {"id": "06", "name" : "Sản phẩm 6", "image" : "img_6.jpg", "price" : "150.000 VND", "desc" : "Sản phẩm này dùng để ...."},
    {"id": "07", "name" : "Sản phẩm 7", "image" : "img_7.jpg", "price" : "150.000 VND", "desc" : "Sản phẩm này dùng để ...."},
    {"id": "08", "name" : "Sản phẩm 8", "image" : "img_8.jpg", "price" : "150.000 VND", "desc" : "Sản phẩm này dùng để ...."},
]
productsLen = len(products)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        session['store_questions'] = request.form['question']
        return redirect(url_for('catalog_page'))
    else:
        return render_template('home.html')


@app.route('/catalog', methods=['GET', 'POST'])
def catalog_page():
    if request.method == 'POST':
        question = request.form['question']
    else:
        try:
            question = session['store_questions']
        except:
            question = ''
    return render_template('catalog.html', products = products, productsLen = productsLen)


@app.route('/about', methods=['GET', 'POST'])
def about_page():
    return render_template('about.html')


@app.route('/product/01', methods=['GET', 'POST'])
def product_page_01():
    return render_template('product01.html')

@app.route('/product/02', methods=['GET', 'POST'])
def product_page_02():
    return render_template('product02.html')

@app.route('/product/03', methods=['GET', 'POST'])
def product_page_03():
    return render_template('product03.html')

@app.route('/product/04', methods=['GET', 'POST'])
def product_page_04():
    return render_template('product04.html')

@app.route('/product/05', methods=['GET', 'POST'])
def product_page_05():
    return render_template('product05.html')

@app.route('/product/06', methods=['GET', 'POST'])
def product_page_06():
    return render_template('product06.html')

@app.route('/product/07', methods=['GET', 'POST'])
def product_page_07():
    return render_template('product07.html')

@app.route('/product/08', methods=['GET', 'POST'])
def product_page_08():
    return render_template('product08.html')

#Checks if the app.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)
    
