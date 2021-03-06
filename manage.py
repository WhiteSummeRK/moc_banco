import os

from app import app
from flask_script import Manager

manager = Manager(app)


@manager.command
def runserver():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == "__main__":
    manager.run()
