# Evo web service

### To your attention is a simple web service that saves in the database all users who press `say hallo` button.

### Writed with flask and sqlalchemy

## Main function

**To say hello, you must fill in all three fields (name, surname and email), and press `say hallo`**

*The name and surname must contain at least two characters, and mail at least five.*

```python
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
```        

**After filling out the form and pressing the `say hello` button user will see a greeting on the screen and his data will be entered into the database.**

**If user's email is already in the database, he will see the message `already met`.**

```python
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
```


## Function 'Show_users'

**On the main page you can find link `Show all users`**
*You will redirect to page with all users in database by clicking it*

```python
def query():
    data = session.query(Users)
    all_data = data.all()
    return all_data
```

```python
def show_users():
    try:
        users = query()
    except:
        return 'Error while trying to read DB'
    return render_template('show_users.html', users=users)
```

## Function 'Find user'

**You also can find any user in data base by filling form and clicking the 'Search' button**

```python
def find_email_user(email):
    data = session.query(Users)
    founded_user = data.filter_by(email=email).all()
    return founded_user
```

```python
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
```    
