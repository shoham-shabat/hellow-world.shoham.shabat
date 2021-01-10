from flask import Flask, render_template, request, session, redirect
import pandas as pd
import mysql.connector

app = Flask(__name__)
app.secret_key = '123'


from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)


@app.route('/')
def openFirstPage():
    return render_template('CV_firstPage_EX6.html')


@app.route('/contactMe')
def openContactMePage():
    return render_template('CV_Project_formPage.html')


@app.route('/contactList')
def openContactListPage():
    return render_template('contactList.html')


@app.route('/assignment8')
def assignment8Page():
    friends = ['amit', 'leorre', 'maya', 'tal']
    gender = 'male'  # male of female
    return render_template('assignment8.html', friends=friends, gender=gender)


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9Page():
    first_name = ''
    last_name = ''
    email = ''
    found = -1
    nick_name = ''
    session['nick_name'] = nick_name
    session['logged_in'] = False

    data = {'first_name': ['Michael', 'Lindsay', 'Tobias', 'Byron', 'George', 'Rachel'],
            'last_name': ['Lawson', 'Ferguson', 'Funke', 'Fields', 'Edwards', 'Howell'],
            'email': ['michael.lawson@reqres.in', 'lindsay.ferguson@reqres.in', 'tobias.funke@reqres.in',
                      'byron.fields@reqres.in', 'george.edwards@reqres.in', 'rachel.howell@reqres.in']}
    users = pd.DataFrame(data=data)
    length = len(users)
    if request.method == 'GET':
        if 'first_name' in request.args:
            if users[users['first_name'] == request.args['first_name']].index.values >= 0:
                i = users[users['first_name'] == request.args['first_name']].index.values[0]
                first_name = users.at[i, 'first_name']
                last_name = users.at[i, 'last_name']
                email = users.at[i, 'email']
                found = 1
            else:
                found = 0

    if request.method == 'POST':
        nick_name = request.form['nick_name']
        session['nick_name'] = nick_name
        session['logged_in'] = True

    return render_template('assignment9.html', request_method=request.method, first_name=first_name,
                           last_name=last_name, email=email, found=found, users=users, length=length,
                           nick_name=nick_name)


@app.route('/assignment9Logout', methods=['GET', 'POST'])
def assignment9Logout():
    if request.method == 'POST':
        nick_name = ''
        session['nick_name'] = nick_name
        session['logged_in'] = False
        return redirect('/assignment9')


if __name__ == '__main__':
    app.run(debug=True)
