from flask_sqlalchemy import SQLAlchemy
from flask import Flask , redirect ,render_template,request

app = Flask(__name__)

# Config: use SQLite database named todo.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)  # ✅ New field


    def __repr__(self):
        return f'<Task {self.id}>'


@app.route('/')
def home():
    tasks = Task.query.all()
    return render_template('home.html', tasks=tasks)
@app.route('/toggle/<int:id>', methods=['POST'])
def toggle(id):
    task = Task.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect('/')


@app.route('/add', methods=["POST"])
def add():
    task_text = request.form.get('task')
    if task_text:
        new_task = Task(content=task_text)
        db.session.add(new_task)
        db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    task = Task.query.get_or_404(id)

    if request.method == 'POST':
        new_text = request.form.get('task')
        if new_text:
            task.content = new_text
            db.session.commit()
        return redirect('/')

    return render_template('edit.html', task=task)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # creates the tables
    app.run(debug=True)

