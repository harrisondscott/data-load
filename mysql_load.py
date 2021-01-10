import mysql.connector
import pandas as pd

cnx = mysql.connector.connect(user='harrison', password='8hY&BZZaa@#!', host='127.0.0.1', database='weather', auth_plugin='mysql_native_password')
cursor = cnx.cursor()
csv_data = pd.read_csv('sample_data.csv') 

for row in csv_data.iterrows():
    list = row[1].values
    cursor.execute("INSERT INTO user_info(Username, Password, Favorite_Weather, ZIP) VALUES('%s','%s','%s','%s');" % tuple(list))
cnx.commit()
cursor.close() 
cnx.close() 

