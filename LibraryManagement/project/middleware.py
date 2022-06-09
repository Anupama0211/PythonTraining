from datetime import datetime


def before():
    print('Time Before Request ', datetime.now())


def after(req):
    print('Time After Request ', datetime.now())
    return req


def init_middlewares(app):
    app.before_request(before)
    app.after_request(after)
