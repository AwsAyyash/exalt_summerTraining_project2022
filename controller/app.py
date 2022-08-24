import os
from pathlib import Path

import connexion

from database.database import db


def change_pwd_to_current():
    script_location = Path(__file__).absolute().parent  # this is the current directory of this file (this script)
    os.chdir(script_location)


if __name__ == '__main__':
    # from resurent_apis.chef_api import ..llsk

    change_pwd_to_current()
    connexion_app = connexion.FlaskApp(__name__, specification_dir='../open_api_restaurant')
    connexion_app.add_api('restaurant_api.yaml', validate_responses=True)

    app = connexion_app.app

    file_path = os.path.abspath(os.getcwd()) + "\database.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path

    db.init_app(app)  # the ORM database (SQLAlchemy)

    with app.app_context():
        db.create_all()

    app.run(debug=True)
