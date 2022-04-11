import pymysql
from flask_restful import Api, Resource
from app import app
from db import mysql
from flask import jsonify
from flask import request


api = Api(app)

class UserList(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("select * from user")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _name = request.form['name']
            _age = request.form['age']
            insert_user_cmd = "INSERT INTO user(nama_user, status_user) VALUES(%s, %s)"

            cursor.execute(insert_user_cmd, (_name, _age))
            conn.commit()
            print(insert_user_cmd)
            response = jsonify(message='User added successfully.',id=cursor.lastrowid)
            # response.data = cursor.lastrowid
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify({'message':'Failed to add user.', 'resp_code':400})
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)
#Get a user by id, update or delete user
class User(Resource):
    def get(self, user_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute('select * from user where id_user = %s',user_id)
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def put(self, user_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _age = request.form['status_user']
            update_user_cmd = """update user 
                                 set status_user=%s
                                 where id_user=%s"""
            cursor.execute(update_user_cmd, (_age, user_id))
            conn.commit()
            response = jsonify('User updated successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to update user.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return(response)

    def delete(self, user_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('delete from user where id_user = %s',user_id)
            conn.commit()
            response = jsonify('User deleted successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to delete user.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return(response)

#API resource routes
api.add_resource(UserList, '/users', endpoint='users')
#URL method = nama function localhost atau 127.0.0.1/user/{id}
api.add_resource(User, '/user/<int:user_id>', endpoint='user')




if __name__ == "__main__":
    app.run(debug=True)
