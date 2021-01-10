from flask import Flask, render_template, request, session, redirect, Blueprint
import mysql.connector
import numpy as np


assignment10 = Blueprint(
    'assignment10', __name__,
    static_folder='static',
    static_url_path='/assignment10',
    template_folder='templates'
)


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost', user='root', password='root', database='assignment10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assignment10.route('/assignment10')
def assignment10Page():
    query = "SELECT * FROM users"
    query_result = interact_db(query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)


@assignment10.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    message = ''
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        query = "INSERT INTO users(first_name, last_name, email) VALUES ('%s', '%s', '%s')" % (first_name, last_name, email)
        interact_db(query=query, query_type='commit')
        message = 'The user was inserted!'
        query = "SELECT * FROM users"
        query_result = interact_db(query, query_type='fetch')
        return render_template('/assignment10.html', insert_message=message, users=query_result)
    message = 'Something went wrong, the user was not inserted! Please try again.'
    return render_template('/assignment10.html', insert_message=message)


@assignment10.route('/delete_user')
def delete_user():
    if request.method == 'GET':
        b = False
        user_id = int(request.args['id'])
        query = "SELECT id FROM users"
        query_result_all = interact_db(query, query_type='fetch')
        for u in query_result_all:
            if user_id == u.id:
                b = True
        if b:
            query = "DELETE FROM users WHERE id='%s';" % user_id
            interact_db(query, query_type='commit')
            delete_message = f'user with id {user_id} is deleted'
        else:
            delete_message = f'user with id {user_id} was not found. Please try again.'
    query = "SELECT * FROM users"
    query_result_all = interact_db(query, query_type='fetch')
    return render_template('/assignment10.html', delete_message=delete_message, users=query_result_all)


@assignment10.route('/update_user', methods=['GET', 'POST'])
def update_user():
    if request.method == 'POST':
        b = False
        user_id = int(request.form['id'])
        user_id_s = request.form['id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        query = "SELECT id FROM users"
        query_result = interact_db(query, query_type='fetch')
        for u in query_result:
            if user_id == u.id:
                b = True
        if b:
            query = "UPDATE users SET first_name='%s', last_name='%s', email='%s'" \
                    "WHERE id='%s'" %(first_name, last_name, email, user_id_s)
            query_result = interact_db(query, query_type='commit')
            update_message = f'user with id {user_id_s} was updated.'
        else:
            update_message = f'user with id {user_id_s} was not found. Please try again.'
        query = "SELECT * FROM users"
        query_result_all = interact_db(query, query_type='fetch')

    return render_template('/assignment10.html', update_message=update_message, users=query_result_all)



