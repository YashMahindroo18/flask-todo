from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(app)

class TODO(DB.Model):
    sno = DB.Column(DB.Integer, primary_key=True)
    title = DB.Column(DB.String(200), nullable=False)
    desc = DB.Column(DB.String(400), nullable=False)
    date_created = DB.Column(DB.DateTime, default=datetime.datetime.now)  # ✅ No parentheses here!

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/',methods=['GET','POST'])
def hello():
    
    if request.method=='POST':
        title=request.form["Title"]
        desc= request.form["Desc"]
        todo = TODO(title=title, desc=desc)
        DB.session.add(todo)
        DB.session.commit()
    alltodo=TODO.query.all()

    return render_template('index.html',alltodo=alltodo)  # ✅ Make sure index.html exists in /templates

# @app.route('/show')
# def products():
#     alltodo=TODO.query.all()

    
#     return "Welcome to the products page"
@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo = TODO.query.filter_by(sno=sno).first()
    if request.method == 'POST':
        title = request.form["Title"]
        desc = request.form["Desc"]
        todo.title = title
        todo.desc = desc
        DB.session.commit()
        return redirect('/')
    
    return render_template('update.html', todo=todo)


@app.route('/delete/<int:sno>')
def delete(sno):
    todo_to_delete = TODO.query.filter_by(sno=sno).first()
    if todo_to_delete:
        DB.session.delete(todo_to_delete)
        DB.session.commit()
    return redirect('/')




if __name__ == "__main__":
    with app.app_context():
        DB.create_all()
    app.run(debug=True, port=8000)
