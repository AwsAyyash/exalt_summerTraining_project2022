from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # this is just a marker as
# if it is inside another (some models of the server) it will produce circular import!
