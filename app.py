from flask import Flask, jsonify
import cx_Oracle

# declare constants for flask app
HOST = '0.0.0.0'
PORT = 5000

# initialize flask application
app = Flask(__name__)

# db connection constants
# update below with your db credentials
DB_IP = "<database_hostname>"
DB_PORT = 1521
SID = "<database_sid>"
DB_USER = "<database_user>"
DB_PASSWORD = "<database_password>"

# make dsn and create connection to db
dsn_tns = cx_Oracle.makedsn(DB_IP, DB_PORT, SID)
connection = cx_Oracle.connect(DB_USER, DB_PASSWORD, dsn_tns)

# sample api endpoint returning data from db
@app.route('/api/test')
def test():
    data=[]
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM table"):
        data.append(row[1].rstrip(" "))
    cursor.close()
    return jsonify(status='success', db_version=connection.version, data=data)


if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,
            port=PORT)
