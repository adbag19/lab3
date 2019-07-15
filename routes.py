from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, User
from forms import UsersForm
from tables import Results
from flask_heroku import Heroku
app = Flask(__name__)
heroku=Heroku(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Gudia7545!@localhost/usersdb'
db.init_app(app)

app.secret_key = "e14a-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():

    form = UsersForm()
    if request.method == 'GET':
        return render_template('add_user.html', form=form)
    else:
        if form.validate_on_submit():
            first_name = request.form['first_name']
            age = request.form['age']
            new_user = User(first_name=first_name, age=age)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
@app.route('/view-user')
def view():
    all=User.query.all()
    table=Results(all)
    table.border= True
    return render_template('view-user.html', table=table)
@app.route('/edit/<int:user_id>', methods=['GET','POST'])
def edit(user_id):
    userdetails=User.query.get(user_id)
    if request.method=="POST":
        userdetails.age=request.form['age']
        userdetails.first_name=request.form["first_name"]
        db.session.commit()
        return redirect('/view-user') 
    else:
        return render_template('edit.html', userdetails=userdetails)
@app.route('/delete/<int:user_id>', methods=['GET','POST'])
def delete(user_id):
    userdetails=User.query.get(user_id)
    if request.method=="POST":
        db.session.delete(userdetails)
        db.session.commit()
        return redirect('/view-user') 
    else:
        return render_template('delete.html', userdetails=userdetails)
if __name__ == "__main__":
  app.run(debug=True)
  