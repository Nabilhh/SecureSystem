from flask import Flask, redirect, url_for, request
from flask_principal import Principal, Permission, RoleNeed

app = Flask(__name__)
Principal(app)

admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))

@app.route('/')
def index():
    return 'Welcome to SecureSuite'

@app.route('/admin')
@admin_permission.require(http_exception=403)
def admin():
    return 'Welcome, Admin!'

@app.route('/user')
@user_permission.require(http_exception=403)
def user():
    return 'Welcome, User!'

if __name__ == '__main__':
    app.run()
