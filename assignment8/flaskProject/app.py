from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
