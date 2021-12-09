from flask import Flask, render_template, url_for, request, flash, session, redirect, url_for, abort


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ac84d52fdb01fbf1d27f0d0ec2be9ac29a62fd8c'
menu = [{"name": "Установка", "url": "install"},
        {"name": "Приложение", "url": "first"},
        {"name": "Обратная связь", "url": "contact"}]

@app.route("/")
@app.route("/index")
def index():
    print( url_for('index')) #возращает только первый(ближний) адресс
    return render_template("index.html", title="Main page", menu=menu)



@app.route("/contact", methods=["POST", "GET"])
def contact():
    # print(url_for('contact'))
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            if len(request.form['email']) > 5:
                flash('Message sent', category='success')
            else:
                flash('Fill in the data correctly', category='error')
        else:
            flash('Fill in the data correctly', category='error')
        print(request.form['username'])

    return render_template("contact.html", title="Обратная связь", menu=menu)

@app.route("/password", methods=["POST", "GET"])
def password():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "IIII" and request.form['psw'] == "1111":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('password.html', title="Авторизация", menu=menu)



@app.route("/profile/<path:username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f"User: {username}"

if __name__ == "__main__":
    app.run(debug=True) #после отладки на фолс

# with app.test_request_context():
#     print( url_for('about'))
#     print( url_for('index'))
