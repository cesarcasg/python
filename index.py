import mysql.connector #import conector to mysql
print "Hello world"
""" #multiple line comments
cnx = mysql.connector.connect(user='aofreew', password='H3sti4.12',
                              host='192.168.2.112',
                              database='avisox')
cnx.close()
"""
#import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'test',
  'raise_on_warnings': True,
  'use_pure': False,
}

cnx = mysql.connector.connect(**config)

cnx.close()
print "end"
