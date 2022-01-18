# Evo web service

### To your attention is a simple web service that saves in the database all users who press "say hallo" button.

### Writed with flask and sqlalchemy

## Main function

**To say hello, you must fill in all three fields (name, surname and mail), and press "say hallo"**

*The name and surname must contain at least two characters, and mail at least five.*

'''python
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
      '''

**After filling out the form and pressing the "say hello" button, the user will see a greeting on the screen and his data will be entered into the database.**

**If the user's mail is already in the database, he will see the message "already met".**
