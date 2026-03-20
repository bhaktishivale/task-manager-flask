from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from models import db, Task

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['task']
        priority = request.form['priority']
        
        # Create new task
        new_task = Task(title=title, priority=priority)
        
        # Save to database
        db.session.add(new_task)
        db.session.commit()
        
        # Redirect to home page
        return redirect(url_for('home'))
    
    # GET request - show add task form
    return render_template('add.html')

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    if request.method == 'POST':
        task.title = request.form['task']
        task.priority = request.form['priority']
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('update.html', task=task)


# COMPLETE ROUTE BELOW
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('home'))

# Add Flask CLI commands for database migrations
@app.cli.command()
def db_init():
    """Initialize the database."""
    db.create_all()
    print("Database initialized.")

@app.cli.command()
def db_seed():
    """Seed the database with sample data."""
    pass

if __name__ == '__main__':
    app.run(debug=True)