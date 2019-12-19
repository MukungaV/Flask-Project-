from flask import Flask  #from the module 'flask' import 'Flask" the class
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__)
#Flask class takes an arguement ' __name__'
#SQLAlchemy:this makes the interaction btwn python and DB smoother
#Flask-SQLAlchemy:this makes the interaction btwn flask and SQLAlchemy smoother

#To create a database: enter python in terminal,from app import db, db.create_all()  creates the database
#db.drop_all() deletes the table from the database

app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///sokoni.sqlite" #path to database
db = SQLAlchemy(app)

#create table for products
class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=False,nullable=False)
    size = db.Column(db.INTEGER, unique=False, nullable=False)
    color = db.Column(db.String(100),nullable=False)
    price = db.Column(db.INTEGER,nullable=False)

    def __repr__(self):
        return 'Name {}'.format(self.name)

@app.route('/')  #@ is a decorator - a function that determines what should happen to the code below it
#app is an object of the 'Flask' class
def index():
    return render_template('index.html',title='SOKONI')
#to show data on python onto html,use {{ }}

@app.route('/products',methods=['GET','POST'])
def products():
    if request.form: #if request is post
        #grab form data
        name = request.form.get('productname')
        price = request.form.get('productprice')
        size = request.form.get('productsize')
        color = request.form.get('productcolor')

        #create a product instance/object
        product = Product(name=name,price=price,size=size,color=color)

        #save data into the db
        db.session.add(product)
        db.session.commit()
    #if user is not posting show them available products
    #get the products from the db
    products = Product.query.all() #get all products from db
    return render_template('products.html', title='All Products',products=products)

@app.route('/products/shoes')
def shoes():
    return 'Shoes Page'

@app.route('/products/shoes/<int:id>') #int- specifies data type int;if not specified then string by default
def shoes_detail(id):
    return 'Shoes Page for id ' + str(id)


@app.route('/products/shoes/<name>/<int:id>') #int- specifies data type int;if not specified then string by default
def shoes_detail2(name,id):
    return 'Shoes Page for {} with id {} ' .format(name,id)




if __name__ == '__main__':
    app.run(port=3000,debug=True)

#pip freeze - checks the dependancies available in the virtual environment; if flask not available, pip install flask

#Codes used by server and browser:
        #200- success
        #404- not found
        #500- error in server

#Create a list of dictionaries:
    #'name':'Jordan'
    #'size':45
    #'colour':black
    #'price':2000