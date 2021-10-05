import os


class Config:
    DEBUG = False
    DEVELOPMENT = False
    SQLALCHEMY_DATABASE_URI = "postgresql://dom:05081998@localhost/ToDoDb"
    SECRET_KEY = os.getenv("SECRET_KEY", "this_should_be_a_random_characters_key")


class ProductionConfig(Config):
    pass


class StagingConfig(Config):
    DEBUG = True


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
