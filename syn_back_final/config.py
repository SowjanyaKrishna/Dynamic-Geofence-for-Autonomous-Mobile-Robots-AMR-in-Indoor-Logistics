import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Secrets
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    MANAGER_PW = os.environ.get("MANAGER_PW") or "Manager"

    # SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DOMAIN = os.environ.get("DOMAIN") or "MISSING DOMAIN"
