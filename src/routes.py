from ast import Try
from app import app
from flask import render_template, redirect, url_for, session, request
from flask_session import Session


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home_page():
    return render_template('home.html')


@app.route('/catalog', methods=['GET', 'POST'])
def catalog_page():
    products = [
        {"name" : "Sản phẩm 1", "image" : "img_1", "Price" : 150000},
        {"name" : "Sản phẩm 2", "image" : "img_2", "Price" : 150000},
        {"name" : "Sản phẩm 3", "image" : "img_3", "Price" : 150000},
        {"name" : "Sản phẩm 4", "image" : "img_4", "Price" : 150000},
        {"name" : "Sản phẩm 5", "image" : "img_5", "Price" : 150000},
        {"name" : "Sản phẩm 6", "image" : "img_6", "Price" : 150000},
        {"name" : "Sản phẩm 7", "image" : "img_7", "Price" : 150000},
        {"name" : "Sản phẩm 8", "image" : "img_8", "Price" : 150000},
    ]
    productsLen = len(products)
    return render_template('catalog.html', products=products, productsLen=productsLen)


@app.route('/about', methods=['GET', 'POST'])
def about_page():
    return render_template('about.html')







