# mysql connect package
# pip --> conda
import pymysql

# connect Mysql
# ip, port, username, password, database name
ip = 'localhost'  # 127.0.0.1
port = '3306'
username = 'yojulab'
password = '!yojulab*'
database =  'db_cars' 

# editor - statement
connect = pymysql.connect(host=ip, user=username, password=password, database=database)

# make select statement
sql_query = 'select * from db_cars.car_infors;'

# execute select query
import pandas 
# reture resultset and then display
df = pandas.read_sql(sql=sql_query, con=connect)

# close
connect.close()

pass