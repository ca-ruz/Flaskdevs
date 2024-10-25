from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)


fakedb = [
    {"id": 1,
     "shirtsize": "L"
     },
    {"id": 2,
     "shirtsize": "XS"
    }
]

@app.route("/")
def hello_world():
    return "<p>Hello, Car!</p>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    result = ''
    for i in range(post_id + 1):
        result += f'Post {i}\n'
    return result

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

def show_the_login_form():
    return render_template_string('''
    <form action="/login" method="POST">
    <input type="text" name="username"
placeholder="Username" required>
    <input type="password" name="password"
placeholder="Password" required>
        <button type="submit">Login</button>
</form>                              ''')

def do_the_login():
    return 'Do the login'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
@app.route('/search')
def search():
    query = request.args.get('q')
    return f'You searched for: {query}'

def get_current_user(id):
    return fakedb[id]

def get_all_users():
    return fakedb

@app.route("/user/<int:id>")
def me_api(id):
    user = get_current_user(id)
    return {
        "a": user["id"],
        "b": user["shirtsize"]
    }

@app.route("/users")
def users_api():
    users = get_all_users()
    return users
