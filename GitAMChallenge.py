#!/usr/bin/python
import MySQLdb
from flask import Flask, request, json

app = Flask(__name__)
db = MySQLdb.connect(host="localhost",user="root",passwd="welcome",db="sys")
cursor=db.cursor()
#----------------------------------------------------------------------------------------------------------

@app.route('/', methods=['GET'])
def registrar_producto():
    if request.method == "GET":
        sql_command = """SELECT * FROM sys.workers;"""  
        cursor.execute(sql_command)
        results = cursor.fetchall()
        return(json.dumps(str(results)))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)