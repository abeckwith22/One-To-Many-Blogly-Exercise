# Application: Blogly
from flask import Flask, render_template, request, redirect
from models import User, Post, db, connect_db
from datetime import datetime

def create_app():
    DATABASE_URL = 'postgresql:///blogly_users_db'
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['DEBUG'] = True
    
    connect_db(app)
    
    return app

app = create_app()

"""Routes"""

### db_user routes

@app.route('/')
def home_page():
    """shows list of users"""
    users = User.query.all()
    return render_template('home.html', users=users)

@app.route('/users/<int:user_id>')
def show_user_info(user_id):
    """Shows verbose info for selected user including posts"""
    user = User.query.filter_by(id=user_id).first()
    user_posts = Post.query.filter(Post.user_id == user_id).all()
    return render_template('detail.html', user=user, posts=user_posts)

@app.route('/users/new', methods=['GET'])
def show_create_users_form():
    """shows new user creation form"""
    return render_template('create_user.html')
    
@app.route('/users/new', methods=['POST'])
def process_create_users_form():
    """process user creation form"""
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]
    image_url = str(image_url) if image_url else "/static/default_icon.png"
    print(f"first name: {first_name} | last name: {last_name} | image_url: {image_url}")
    add_user(first_name, last_name, image_url)
    return redirect('/')

@app.route('/users/<int:user_id>/delete')
def show_confirm_delete_page(user_id):
    """show user deletion confirmation form"""
    return render_template('delete_user_confirmation.html', user=User.query.filter_by(id=user_id).first())

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def confirmed_remove_user(user_id):
    """deletes user and redirects to / page"""
    del_user(user_id)
    return redirect('/')

@app.route('/users/<int:user_id>/edit')
def show_edit_user_page(user_id):
    """shows user edit page"""
    user = User.query.filter_by(id=user_id).first()
    return render_template('edit.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def confirmed_edit_user(user_id):
    """confirm users edit page and redirects to edited suer"""
    first_name = request.form['first_name']
    first_name = first_name if first_name else None

    last_name = request.form['last_name']
    last_name = last_name if last_name else None

    image_url = request.form['image_url']
    image_url = image_url if image_url else None

    user = User.query.filter_by(id=user_id).first()
    
    edit_user(user, first_name, last_name, image_url)
    
    return redirect(f'/users/{user_id}') # redirect to edited user to show new information

### db_post routes
@app.route('/posts/<int:post_id>')
def show_post_info(post_id):
    """shows content and created_at information about post"""
    post = Post.query.filter_by(id=post_id).first()
    return render_template('post_detail.html', post=post)

@app.route('/posts/<int:post_id>/edit')
def show_edit_post_info(post_id):
    """Show edit post form"""
    post = Post.query.filter_by(id=post_id).first()
    return render_template('edit_post.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def commit_edit_post_info(post_id):
    """Commit edit post form to update it and send to database"""
    post = Post.query.filter_by(id=post_id).first()

    title = request.form['title']
    title = title if title else None

    content = request.form['content']
    content = content if content else None

    edit_post(post, title, content)
    
    return redirect(f'/posts/{post_id}') # redirect to edited post to show new information

@app.route('/posts/<int:post_id>/delete')
def show_delete_post_info(post_id):
    post = Post.query.filter_by(id=post_id).first()
    return render_template('delete_post_confirmation.html', post=post)
    
    
@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def confirm_delete_post(post_id):
    """deletes posts and redirects to / page"""
    del_post(post_id)
    return redirect('/')

@app.route('/users/<int:user_id>/posts/new')
def show_new_post_form(user_id):
    """Shows user new post form"""
    user = User.query.filter_by(id=user_id).first()
    return render_template('create_post.html', user=user)

@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def commit_new_post_to_user(user_id):
    title = request.form['title']
    content = request.form['content']
    date = datetime.now()
    formatted_date = date.strftime("%Y-%m-%d %I:%M:%S")
    
    new_post = Post(title=title, content=content, created_at=formatted_date, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f'/users/{user_id}')
    
    

"""Logic functions"""

def add_user(first_name, last_name, image_url):
    """Logic function adding user to db"""
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

def del_user(user_id):
    """Logic function deleting user to db"""
    User.query.filter_by(id=user_id).delete() # should delete
    print(f'removed user {user_id}')
    db.session.commit()

def remove_post_id_from_user(user_id, post_id):
    """Logic function deleting post_id from user"""
    x = User.post_id.query.filter_by(id=post_id)
    print(x)

def edit_user(user, first_name=None, last_name=None, image_url=None):
    """Logic function editing user to db"""
    if first_name != None:
        user.first_name = first_name
    if last_name != None:
        user.last_name = last_name
    if image_url != None:
        user.image_url = image_url
    
    db.session.add(user)
    db.session.commit()

def edit_post(post, title=None, content=None):
    """Logic function editing post to db"""
    if title != None:
        post.title = title 
    if content != None:
        post.content = content 
    
    db.session.add(post)
    db.session.commit()

def del_post(post_id):
    """Logic function for deleting post to db"""
    # User.query.filter(User.id == Post.id).drop()
    Post.query.filter_by(id=post_id).delete()
    print(f"Removed post {post_id}")
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
