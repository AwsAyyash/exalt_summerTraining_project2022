import os
import time
from pathlib import Path

import connexion
import MySQLdb
# for _ in range(100):
#     time.sleep(10)

from database.database import db


def change_pwd_to_current():
    script_location = Path(__file__).absolute().parent  # this is the current directory of this file (this script)
    os.chdir(script_location)


if __name__ == '__main__':
    # from resurent_apis.chef_api import ..llsk

    change_pwd_to_current()
    connexion_app = connexion.FlaskApp(__name__, specification_dir='open_api_restaurant')
    connexion_app.add_api('restaurant_api.yaml', validate_responses=True)

    app = connexion_app.app

    #file_path = os.path.abspath(os.getcwd()) + "\database.db"

    app.config['MYSQL_HOST'] = '0.0.0.0'
    app.config['MYSQL_USER'] = 'admin'
    app.config['MYSQL_PASSWORD'] = '123456789'
    app.config['MYSQL_DB'] = 'exalt22_summer'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://admin:123456789@localhost/exalt22_summer"

   # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:********@localhost/abc'




    db.init_app(app)  # the ORM database (SQLAlchemy)

    with app.app_context():
        db.create_all()

    app.run(debug=True, host='0.0.0.0')



# steps:
# docker build -t
# docker compose up --build
# docker run
#wie geht's
