import app as app
import cart as cart
import cur as cur
import cursor as cursor
import mysql as mysql
import pymysql as pymysql
import requests
from flask import Flask, render_template, request, url_for, redirect, session, jsonify, flash
from flask_mysqldb import MySQL
from mysql.connector import cursor
from flask_wtf import FlaskForm

from werkzeug.security import generate_password_hash
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
from flaskext.mysql import MySQL
import pymysql



app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'food_database'



# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'db': 'food_database',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor

}



# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'food_database'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# Database configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="food_database"
)
cursor = db.cursor()


mysql = MySQL(app)



@app.route('/', methods=['GET', 'POST'])
def index():


    user_logged_in = False
    connection = pymysql.connect(**db_config)

    try:
        with connection.cursor() as cursor:
            sql1 = "SELECT * FROM cities"
            cursor.execute(sql1)
            restaurants = cursor.fetchall()

            sql = "SELECT * FROM foods"
            cursor.execute(sql)
            items = cursor.fetchall()

            sql2 = "SELECT * FROM foods"
            cursor.execute(sql2)
            rows = cursor.fetchall()

            sql3 = "SELECT * FROM category"
            cursor.execute(sql3)
            cat = cursor.fetchall()

    finally:
            connection.close()




    return render_template('index.html', items=items,user_logged_in=user_logged_in,restaurants=restaurants,categorys=cat,restaurant={'name': 'Restaurant Name'},products=rows)


# Rest of your code...
@app.route('/search', methods=['GET'])
def search_food():
    query = request.args.get('query', '')

    if query:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM food WHERE name LIKE %s", ('%' + query + '%',))
        results = cur.fetchall()
        cur.close()
    else:
        results = []

    return jsonify(results)



@app.route('/search-page')
def search_page():
    return render_template('search.html')




# Simulated food data dictionary
food_data = {
    "123 Main St": ["Pizza Place", "Burger Joint"],
    "456 Elm St": ["Sushi Bar", "Thai Restaurant"],
    # Add more data as needed
}



# Logout route
@app.route("/logout")
def logout():
    global user_logged_in
    user_logged_in = False
    return redirect(url_for("login"))





# Signup route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password_hash"])
        role = "user"  # Default role for new users

        # Insert user into the database
        cursor.execute("INSERT INTO Users (username, email, password_hash, role) VALUES (%s, %s, %s, %s)",
                       (username, email, password, role))
        db.commit()
        return redirect(url_for("login"))
    return render_template("signup.html")








@app.route('/find_food', methods=['POST'])
def find_food():
    address = request.form['inputDelivery']
    food_options = find_food_options(address)

    connection = pymysql.connect(**db_config)
    items = []

    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM foods WHERE address = %s"
            cursor.execute(sql)
            items = cursor.fetchall()
    except pymysql.Error as e:
        pass
    finally:
        connection.close()

    return render_template('food_results.html', address=address, food_options=food_options, products=items)


def find_food_options(address):

    if address in food_data:
        return food_data[address]
    else:
        return []




@app.route('/convert/<float:latitude>/<float:longitude>')
def convert_coordinates(latitude, longitude):
    nominatim_url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}"

    response = requests.get(nominatim_url)
    if response.status_code == 200:
        data = response.json()
        location_code = data.get('osm_id')
        return jsonify({'location_code': location_code})
    else:
        return jsonify({'error': 'Unable to fetch location code'}), 500




# LOGIN    Routes




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password_hash']
        user_type = request.form['role']

        if user_type == 'admin':
            cursor.execute("SELECT * FROM users WHERE username = %s AND password_hash = %s AND role = %s", (username, password,user_type))
            user = cursor.fetchone()
            if user:
                session['user_id'] = user[0]
                return redirect(url_for('admin_dashboard'))

        elif user_type == 'user':
            cursor.execute("SELECT * FROM users WHERE username = %s AND password_hash = %s AND role = %s", (username, password,user_type))
            user = cursor.fetchone()
            if user:
                session['user_id'] = user[0]
                return redirect(url_for('user_dashboard'))

        elif user_type == 'owner':
            cursor.execute("SELECT * FROM users WHERE username = %s AND password_hash = %s AND role = %s", (username, password,user_type))
            user = cursor.fetchone()
            if user:
                session['user_id'] = user[0]
                return redirect(url_for('owner_dashboard'))

        else:
            return "Invalid user type or credentials"

    return render_template('login.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'user_id' in session:

        connection = pymysql.connect(**db_config)


    else:
        return redirect(url_for('login'))

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM foods"
            cursor.execute(sql)
            data = cursor.fetchall()
    finally:
        connection.close()








        return render_template('admin_dashboard.html',students=data )


@app.route('/user_dashboard')
def user_dashboard():
    if 'user_id' in session:
        user_logged_in = True
        connection = pymysql.connect(**db_config)

    try:
        with connection.cursor() as cursor:
            sql1 = "SELECT * FROM cities"
            cursor.execute(sql1)
            restaurants = cursor.fetchall()

            sql = "SELECT * FROM foods"
            cursor.execute(sql)
            items = cursor.fetchall()

            sql2 = "SELECT * FROM foods"
            cursor.execute(sql2)
            rows = cursor.fetchall()

            sql3 = "SELECT * FROM category"
            cursor.execute(sql3)
            cat = cursor.fetchall()



    finally:
        connection.close()




    return render_template('user_dashboard.html', items=items,user_logged_in=user_logged_in,restaurants=restaurants,categorys=cat,restaurant={'name': 'Restaurant Name'},products=rows)


@app.route('/owner_dashboard')
def owner_dashboard():
    if 'user_id' in session:
        # Owner dashboard logic
        return render_template('owner_panel.html')
    else:
        return redirect(url_for('login'))












@app.route('/')
def admin_panel():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM food")
    products = cursor.fetchall()
    cursor.close()
    return render_template('admin_panel.html', products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product_form():
    if 'user_id' in session:

        connection = pymysql.connect(**db_config)


    else:
        return redirect(url_for('login'))

    try:
        with connection.cursor() as cursor:
            sql ="SELECT * FROM foods ORDER BY created_at DESC"
            cursor.execute(sql)
            data = cursor.fetchall()

            sql1 = "SELECT * FROM category"
            cursor.execute(sql1)
            data1 = cursor.fetchall()

            sql2 = "SELECT * FROM cities"
            cursor.execute(sql2)
            data2 = cursor.fetchall()

            sql3 = "SELECT * FROM restaurants"
            cursor.execute(sql3)
            data3 = cursor.fetchall()
    finally:
        connection.close()


        return render_template('add_product.html',students=data,categories=data1,cities=data2,restaurants=data3 )

@app.route('/add_category', methods=['GET', 'POST'])
def add_category_form():
    if 'user_id' in session:

        connection = pymysql.connect(**db_config)


    else:
        return redirect(url_for('login'))

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM category ORDER BY created_at DESC"
            cursor.execute(sql)
            data = cursor.fetchall()
    finally:
        connection.close()


        return render_template('add_category.html',students=data )



@app.route('/add_restaurant', methods=['GET', 'POST'])
def add_restaurant_form():
    if 'user_id' in session:

        connection = pymysql.connect(**db_config)


    else:
        return redirect(url_for('login'))

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM restaurants ORDER BY created_at DESC"
            cursor.execute(sql)
            data = cursor.fetchall()
    finally:
        connection.close()


        return render_template('add_restaurant.html',students=data )

@app.route('/add_city', methods=['GET', 'POST'])
def add_city_form():
    if 'user_id' in session:

        connection = pymysql.connect(**db_config)


    else:
        return redirect(url_for('login'))

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM cities ORDER BY created_at DESC"
            cursor.execute(sql)
            data = cursor.fetchall()
    finally:
        connection.close()


        return render_template('add_city.html',students=data )













 # ADD TO Cart

@app.route('/add', methods=['POST'])
def add_product_to_cart():
 cursor = None
 try:
  _quantity = int(request.form['quantity'])
  _code = request.form['code']
  # validate the received values
  if _quantity and _code and request.method == 'POST':
   conn = mysql.connect()
   cursor = conn.cursor(pymysql.cursors.DictCursor)
   cursor.execute("SELECT * FROM foods WHERE code=%s", _code)
   row = cursor.fetchone()

   itemArray = { row['code'] : {'name' : row['name'],
                                'price' : row['price'],
                                'image_url' : row['image_url'],
                                'created_at': None,  # You may set this to an appropriate value if needed
                                'updated_at': None,  # You may set this to an appropriate value if needed
                                'restaurant_name': None,  # You may set this to an appropriate value if needed
                                'address': None,  # You may set this to an appropriate value if needed
                                'code' : row['code'],
                                'category': None,
                                'discount': None,  # You may set this to an appropriate value if needed
                                'quantity' : _quantity,
                                'total_price': _quantity * row['price']}}


   all_total_price = 0
   all_total_quantity = 0

   session.modified = True
   if 'cart_item' in session:
    if row['code'] in session['cart_item']:
     for key, value in session['cart_item'].items():
      if row['code'] == key:
       old_quantity = session['cart_item'][key]['quantity']
       total_quantity = old_quantity + _quantity
       session['cart_item'][key]['quantity'] = total_quantity
       session['cart_item'][key]['total_price'] = total_quantity * row['price']
    else:
     session['cart_item'] = array_merge(session['cart_item'], itemArray)

    for key, value in session['cart_item'].items():
     individual_quantity = int(session['cart_item'][key]['quantity'])
     individual_price = float(session['cart_item'][key]['total_price'])
     all_total_quantity = all_total_quantity + individual_quantity
     all_total_price = all_total_price + individual_price
   else:
    session['cart_item'] = itemArray
    all_total_quantity = all_total_quantity + _quantity
    all_total_price = all_total_price + _quantity * row['price']

   session['all_total_quantity'] = all_total_quantity
   session['all_total_price'] = all_total_price

   return redirect(url_for('.products'))
  else:
   return 'Error while adding item to cart'
 except Exception as e:
  print(e)
 finally:
  cursor.close()
  conn.close()


@app.route('/cart')
def products():
 try:
  user_logged_in = False
  conn = mysql.connect()
  cursor = conn.cursor(pymysql.cursors.DictCursor)
  cursor.execute("SELECT * FROM foods")
  rows = cursor.fetchall()
  return render_template('cart.html', products=rows,user_logged_in=user_logged_in)
 except Exception as e:
  print(e)
 finally:
  cursor.close()
  conn.close()




@app.route('/empty')
def empty_cart():
 try:
  session.clear()
  return redirect(url_for('.products'))
 except Exception as e:
  print(e)

@app.route('/delete/<string:code>')
def delete_product(code):
 try:
  all_total_price = 0
  all_total_quantity = 0
  session.modified = True

  for item in session['cart_item'].items():
   if item[0] == code:
    session['cart_item'].pop(item[0], None)
    if 'cart_item' in session:
     for key, value in session['cart_item'].items():
      individual_quantity = int(session['cart_item'][key]['quantity'])
      individual_price = float(session['cart_item'][key]['total_price'])
      all_total_quantity = all_total_quantity + individual_quantity
      all_total_price = all_total_price + individual_price
    break

  if all_total_quantity == 0:
   session.clear()
  else:
   session['all_total_quantity'] = all_total_quantity
   session['all_total_price'] = all_total_price

  return redirect(url_for('.products'))
 except Exception as e:
  print(e)

def array_merge( first_array , second_array ):
 if isinstance( first_array , list ) and isinstance( second_array , list ):
  return first_array + second_array
 elif isinstance( first_array , dict ) and isinstance( second_array , dict ):
  return dict( list( first_array.items() ) + list( second_array.items() ) )
 elif isinstance( first_array , set ) and isinstance( second_array , set ):
  return first_array.union( second_array )
 return False

 # ADD TO Cart1

@app.route('/add1', methods=['POST'])
def add_product_to_cart1():
 cursor = None
 try:
  _quantity = int(request.form['quantity'])
  _code = request.form['code']
  # validate the received values
  if _quantity and _code and request.method == 'POST':
   conn = mysql.connect()
   cursor = conn.cursor(pymysql.cursors.DictCursor)
   cursor.execute("SELECT * FROM foods WHERE code=%s", _code)
   row = cursor.fetchone()

   itemArray = { row['code'] : {'name' : row['name'],
                                'price' : row['price'],
                                'image_url' : row['image_url'],
                                'created_at': None,  # You may set this to an appropriate value if needed
                                'updated_at': None,  # You may set this to an appropriate value if needed
                                'restaurant_name': None,  # You may set this to an appropriate value if needed
                                'address': None,  # You may set this to an appropriate value if needed
                                'code' : row['code'],
                                'category': None,
                                'discount': None,  # You may set this to an appropriate value if needed
                                'quantity' : _quantity,
                                'total_price': _quantity * row['price']}}


   all_total_price = 0
   all_total_quantity = 0

   session.modified = True
   if 'cart_item' in session:
    if row['code'] in session['cart_item']:
     for key, value in session['cart_item'].items():
      if row['code'] == key:
       old_quantity = session['cart_item'][key]['quantity']
       total_quantity = old_quantity + _quantity
       session['cart_item'][key]['quantity'] = total_quantity
       session['cart_item'][key]['total_price'] = total_quantity * row['price']
    else:
     session['cart_item'] = array_merge(session['cart_item'], itemArray)

    for key, value in session['cart_item'].items():
     individual_quantity = int(session['cart_item'][key]['quantity'])
     individual_price = float(session['cart_item'][key]['total_price'])
     all_total_quantity = all_total_quantity + individual_quantity
     all_total_price = all_total_price + individual_price
   else:
    session['cart_item'] = itemArray
    all_total_quantity = all_total_quantity + _quantity
    all_total_price = all_total_price + _quantity * row['price']

   session['all_total_quantity'] = all_total_quantity
   session['all_total_price'] = all_total_price

   return redirect(url_for('.products1'))
  else:
   return 'Error while adding item to cart'
 except Exception as e:
  print(e)
 finally:
  cursor.close()
  conn.close()


@app.route('/cart1')
def products1():
 try:
  user_logged_in = True
  conn = mysql.connect()
  cursor = conn.cursor(pymysql.cursors.DictCursor)
  cursor.execute("SELECT * FROM foods")
  rows = cursor.fetchall()
  return render_template('cart1.html', products=rows,user_logged_in=user_logged_in)
 except Exception as e:
  print(e)
 finally:
  cursor.close()
  conn.close()




@app.route('/empty1')
def empty_cart1():
 try:
  session.clear()
  return redirect(url_for('.products1'))
 except Exception as e:
  print(e)

@app.route('/delete1/<string:code>')
def delete_product1(code):
 try:
  all_total_price = 0
  all_total_quantity = 0
  session.modified = True

  for item in session['cart_item'].items():
   if item[0] == code:
    session['cart_item'].pop(item[0], None)
    if 'cart_item' in session:
     for key, value in session['cart_item'].items():
      individual_quantity = int(session['cart_item'][key]['quantity'])
      individual_price = float(session['cart_item'][key]['total_price'])
      all_total_quantity = all_total_quantity + individual_quantity
      all_total_price = all_total_price + individual_price
    break

  if all_total_quantity == 0:
   session.clear()
  else:
   session['all_total_quantity'] = all_total_quantity
   session['all_total_price'] = all_total_price

  return redirect(url_for('.products1'))
 except Exception as e:
  print(e)

def array_merge( first_array , second_array ):
 if isinstance( first_array , list ) and isinstance( second_array , list ):
  return first_array + second_array
 elif isinstance( first_array , dict ) and isinstance( second_array , dict ):
  return dict( list( first_array.items() ) + list( second_array.items() ) )
 elif isinstance( first_array , set ) and isinstance( second_array , set ):
  return first_array.union( second_array )
 return False







#CRUD




# Define a function to check if a file has an allowed image extension
def allowed_image(filename):
    allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        connection = pymysql.connect(**db_config)

        name = request.form['name']
        price = request.form['price']
        image_url = request.files['image_url']
        restaurant_name = request.form['restaurant_name']
        address = request.form['address']
        code = request.form['code']
        category = request.form['category']

        try:
            with connection.cursor() as cursor:
                if not allowed_image(image_url.filename):
                    return "Invalid file type. Only image files (jpg, jpeg, png, gif) are allowed."

                # If it's an image, save it to a directory or process it further
                # Example: image_url.save("path_to_save_uploaded_image.jpg")

                # Insert other data into the database
                sql = "INSERT INTO foods (name, price, image_url, restaurant_name, `address`, `code`, `category`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (name, price, image_url.filename, restaurant_name, address, code, category)
                cursor.execute(sql, values)
                connection.commit()

            return redirect(url_for('add_product_form'))
        except Exception as e:
            # Handle exceptions (e.g., database errors)
            print(f"Error: {e}")
            connection.rollback()  # Rollback the transaction in case of an error
        finally:
            connection.close()

@app.route('/insert_category', methods=['POST'])
def insert_category():
    if request.method == "POST":
        connection = pymysql.connect(**db_config)

        name = request.form['name']
        image_url = request.files['image_url']


        try:
            with connection.cursor() as cursor:
                if not allowed_image(image_url.filename):
                    return "Invalid file type. Only image files (jpg, jpeg, png, gif) are allowed."

                # If it's an image, save it to a directory or process it further
                # Example: image_url.save("path_to_save_uploaded_image.jpg")

                # Insert other data into the database
                sql = "INSERT INTO category (name, image_url) VALUES (%s, %s)"
                values = (name, image_url.filename)
                cursor.execute(sql, values)
                connection.commit()

            return redirect(url_for('add_category_form'))
        except Exception as e:
            # Handle exceptions (e.g., database errors)
            print(f"Error: {e}")
            connection.rollback()  # Rollback the transaction in case of an error
        finally:
            connection.close()



@app.route('/insert_restaurant', methods=['POST'])
def insert_restaurant():
    if request.method == "POST":
        connection = pymysql.connect(**db_config)

        name = request.form['name']
        image_url = request.files['image_url']


        try:
            with connection.cursor() as cursor:
                if not allowed_image(image_url.filename):
                    return "Invalid file type. Only image files (jpg, jpeg, png, gif) are allowed."

                # If it's an image, save it to a directory or process it further
                # Example: image_url.save("path_to_save_uploaded_image.jpg")

                # Insert other data into the database
                sql = "INSERT INTO restaurants (name, image_url) VALUES (%s, %s)"
                values = (name, image_url.filename)
                cursor.execute(sql, values)
                connection.commit()

            return redirect(url_for('add_restaurant_form'))
        except Exception as e:
            # Handle exceptions (e.g., database errors)
            print(f"Error: {e}")
            connection.rollback()  # Rollback the transaction in case of an error
        finally:
            connection.close()

@app.route('/insert_city', methods=['POST'])
def insert_city():
   if request.method == "POST":
        connection = pymysql.connect(**db_config)

        name = request.form['name']
        image_url = request.files['image_url']


        try:
            with connection.cursor() as cursor:
                if not allowed_image(image_url.filename):
                    return "Invalid file type. Only image files (jpg, jpeg, png, gif) are allowed."

                # If it's an image, save it to a directory or process it further
                # Example: image_url.save("path_to_save_uploaded_image.jpg")

                # Insert other data into the database
                sql = "INSERT INTO cities (name, image_url) VALUES (%s, %s)"
                values = (name, image_url.filename)
                cursor.execute(sql, values)
                connection.commit()

            return redirect(url_for('add_city_form'))
        except Exception as e:
            # Handle exceptions (e.g., database errors)
            print(f"Error: {e}")
            connection.rollback()  # Rollback the transaction in case of an error
        finally:
            connection.close()

@app.route('/delete_food/<string:pid_data>', methods=['GET'])
def delete_food(pid_data):
    try:
        connection = pymysql.connect(**db_config)
        cur = connection.cursor()
        cur.execute("DELETE FROM foods WHERE pid = %s", (pid_data,))
        connection.commit()
        flash("Record has been deleted successfully", "success")
    except Exception as e:
        # Handle exceptions (e.g., database errors)
        flash(f"Error: {e}", "error")
    finally:
        cur.close()
        connection.close()

    return redirect(url_for('add_product_form'))



@app.route('/delete_category/<string:cid_data>', methods=['GET'])
def delete_category(cid_data):
    try:
        connection = pymysql.connect(**db_config)
        cur = connection.cursor()
        cur.execute("DELETE FROM category WHERE cid = %s", (cid_data,))
        connection.commit()
        flash("Record has been deleted successfully", "success")
    except Exception as e:
        # Handle exceptions (e.g., database errors)
        flash(f"Error: {e}", "error")
    finally:
        cur.close()
        connection.close()

    return redirect(url_for('add_category_form'))

@app.route('/delete_restaurant/<string:id_data>', methods=['GET'])
def delete_restaurant(id_data):
    try:
        connection = pymysql.connect(**db_config)
        cur = connection.cursor()
        cur.execute("DELETE FROM restaurants WHERE id = %s", (id_data,))
        connection.commit()
        flash("Record has been deleted successfully", "success")
    except Exception as e:
        # Handle exceptions (e.g., database errors)
        flash(f"Error: {e}", "error")
    finally:
        cur.close()
        connection.close()

    return redirect(url_for('add_restaurant_form'))

@app.route('/delete_city/<string:id_data>', methods=['GET'])
def delete_city(id_data):
    try:
        connection = pymysql.connect(**db_config)
        cur = connection.cursor()
        cur.execute("DELETE FROM cities WHERE id = %s", (id_data,))
        connection.commit()
        flash("Record has been deleted successfully", "success")
    except Exception as e:
        # Handle exceptions (e.g., database errors)
        flash(f"Error: {e}", "error")
    finally:
        cur.close()
        connection.close()

    return redirect(url_for('add_city_form'))






@app.route('/update_food', methods=['POST'])
def update_food():
    if request.method == 'POST':
        connection = pymysql.connect(**db_config)
        try:
            with connection.cursor() as cursor:
                pid_data = request.form['pid']
                name = request.form['name']
                price = request.form['price']
                image_url = request.form['image_url']
                restaurant_name = request.form['restaurant_name']
                address = request.form['address']
                code = request.form['code']
                category = request.form['category']

                # Execute the UPDATE query with parameterized values
                cursor.execute("UPDATE foods SET name=%s, price=%s, image_url=%s, restaurant_name=%s, `address`=%s, `code`=%s, `category`=%s WHERE pid=%s", (name, price, image_url, restaurant_name, address, code, category, pid_data))

                connection.commit()
                flash("Data Updated Successfully")
        except Exception as e:
            # Handle exceptions (e.g., database errors)
            print(f"Error: {e}")
            connection.rollback()  # Rollback the transaction in case of an error
        finally:
            connection.close()
    return redirect(url_for('add_product_form'))


@app.route('/update_category', methods=['POST'])
def update_category():
    if request.method == 'POST':
        connection = pymysql.connect(**db_config)
        try:
            with connection.cursor() as cursor:
                cid_data = request.form['cid']  # Use the correct field name
                name = request.form['name']
                image_url = request.form['image_url']
                # Execute the UPDATE query with parameterized values
                cursor.execute("UPDATE category SET name=%s, image_url=%s WHERE cid=%s", (name, image_url, cid_data))

                connection.commit()
                flash("Data Updated Successfully")
        except Exception as e:
            # Handle exceptions (e.g., database errors)
            print(f"Error: {e}")
            connection.rollback()  # Rollback the transaction in case of an error
        finally:
            connection.close()
    return redirect(url_for('add_category_form'))


@app.route('/update_restaurant', methods=['POST'])
def update_restaurant():
    if request.method == 'POST':
        connection = pymysql.connect(**db_config)
        try:
            with connection.cursor() as cursor:
                id_data = request.form['id']  # Use the correct field name
                name = request.form['name']
                image_url = request.form['image_url']
                # Execute the UPDATE query with parameterized values
                cursor.execute("UPDATE restaurants SET name=%s, image_url=%s WHERE id=%s", (name, image_url, id_data))

                connection.commit()
                flash("Data Updated Successfully")
        except Exception as e:
            # Handle exceptions (e.g., database errors)
            print(f"Error: {e}")
            connection.rollback()  # Rollback the transaction in case of an error
        finally:
            connection.close()
    return redirect(url_for('add_restaurant_form'))




@app.route('/update_city', methods=['POST'])
def update_city():
    if request.method == 'POST':
        connection = pymysql.connect(**db_config)
        try:
            with connection.cursor() as cursor:
                id_data = request.form['id']  # Use the correct field name
                name = request.form['name']
                image_url = request.form['image_url']
                # Execute the UPDATE query with parameterized values
                cursor.execute("UPDATE cities SET name=%s, image_url=%s WHERE id=%s", (name, image_url, id_data))

                connection.commit()
                flash("Data Updated Successfully")
        except Exception as e:
            # Handle exceptions (e.g., database errors)
            print(f"Error: {e}")
            connection.rollback()  # Rollback the transaction in case of an error
        finally:
            connection.close()
    return redirect(url_for('add_city_form'))



#Checkout

@app.route('/insert1', methods=['POST'])
def insert1():
    if request.method == "POST":
        if 'user_id' in session:  # Check if user is logged in
            user_id = session['user_id']  # Retrieve the user_id from the session
            connection = pymysql.connect(**db_config)
            total_amount = request.form['total_amount']
            address = request.form['address']

            try:
                with connection.cursor() as cursor:
                    sql = "INSERT INTO orders (user_id, total_amount, address) VALUES (%s, %s, %s)"
                    values = (user_id, total_amount, address)
                    cursor.execute(sql, values)
                    connection.commit()
                flash('Order placed successfully!', 'success')
                return redirect(url_for('user_dashboard'))
            except Exception as e:
                # Handle exceptions (e.g., database errors)
                print(f"Error: {e}")
                connection.rollback()  # Rollback the transaction in case of an error
            finally:
                connection.close()
        else:
            flash('Please log in first.', 'danger')
            return redirect(url_for('login'))



@app.route('/city', methods=['GET', 'POST'])
def city():
    if 'user_id' in session:
        user_logged_in = True
        connection = pymysql.connect(**db_config)
        address = request.args.get('address')  # Retrieve the "address" parameter from the URL


    try:
        with connection.cursor() as cursor:

            sql = "SELECT * FROM foods WHERE address = %s"

            cursor.execute(sql, (address,))
            items = cursor.fetchall()




    finally:
        connection.close()




    return render_template('result_city.html', products=items,user_logged_in=user_logged_in)


@app.route('/category', methods=['GET', 'POST'])
def category():
    if 'user_id' in session:
        user_logged_in = True
        connection = pymysql.connect(**db_config)
        address = request.args.get('category')  # Retrieve the "address" parameter from the URL


    try:
        with connection.cursor() as cursor:

            sql = "SELECT * FROM foods WHERE category = %s"

            cursor.execute(sql, (address,))
            items = cursor.fetchall()

            sql1 = "SELECT * FROM category"

            cursor.execute(sql1)
            category = cursor.fetchall()




    finally:
        connection.close()




    return render_template('result_category.html', products=items, category=category,user_logged_in=user_logged_in)



@app.route('/admin_orders', methods=['GET', 'POST'])
def admin_orders():
    if 'user_id' in session:

        connection = pymysql.connect(**db_config)


    else:
        return redirect(url_for('login'))

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM orders,users"
            cursor.execute(sql)
            data = cursor.fetchall()
    finally:
        connection.close()


        return render_template('admin_orders.html',students=data )



if __name__ == '__main__':
    app.run(debug=True)
