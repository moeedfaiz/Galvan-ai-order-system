Order Handling System (Flask + MySQL)
This project is a simple backend web application built using Flask and MySQL that enables users to perform basic order management operations such as adding, editing, marking as delivered, and deleting orders. 

- Features
Add new orders with key details
Edit existing orders
Mark orders as delivered
Delete orders
Log all actions with timestamps and user info


- Tech Stack
Python
Flask (Jinja2 templating)
MySQL (with mysql-connector-python or SQLAlchemy)


- Create the MySQL Database
CREATE DATABASE order_db;

USE order_db;

(write the above sql query to create a database)

- Configure DB Connection
<!-- app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@localhost/order_db' -->#   G a l v a n - a i - o r d e r - s y s t e m  
 