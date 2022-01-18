from alchemy import engine, base, session, Users, query, find_email_user
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
base.metadata.create_all(engine)
answer = ['Fill the form']


@app.route('/main', methods=['GET'])
def main():
    return render_template('index.html', answer=answer)


@app.route('/show_users', methods=['GET'])
def show_users():
    try:
        users = query()
    except:
        return 'Error while trying to read DB'
    return render_template('show_users.html', users=users)


@app.route('/find_user', methods=['POST'])
def find_user():
    try:
        email = request.form['email']
        founded_user = find_email_user(email=email)
        if founded_user:
            return render_template('index.html', founded_user=founded_user)
        else:
            miss = ("user wasn't found",)
            return render_template('index.html', miss=miss)
    except:
        return "Oops, smth wrong"


@app.route('/say_hallo', methods=['POST'])
def sey_hallo():
    user_name = request.form['user_name']
    if len(user_name) < 2:
        answer[0] = 'Длина имени не может быть меньше чем 2 символа'
        return redirect(url_for('main'))
    user_surname = request.form['user_surname']
    if len(user_surname) < 2:
        answer[0] = 'Длина фамилии не может быть меньше чем 2 символа'
        return redirect(url_for('main'))
    user_email = request.form['user_email']
    if len(user_email) < 5:
        answer[0] = 'Название почты не может быть меньше пяти символов'
        return redirect(url_for('main'))
    que = session.query(Users).filter_by(email=user_email)
    find = que.first()
    if find:
        try:
            hallo_again = 'Уже видились, {}'.format(user_name)
            answer[0] = hallo_again
        except:
            return 'Oops, smth wrong'
    else:
        try:
            user = Users(name=user_name, surname=user_surname, email=user_email)
            session.add(user)
            session.commit()
            nice_to_meet_u = 'Привет, {}'.format(user_name)
            answer[0] = nice_to_meet_u
        except:
            return 'Oops, smth wrong'
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run()
