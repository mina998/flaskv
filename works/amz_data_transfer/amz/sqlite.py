from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from configure import SQLALCHEMY_DATABASE_URI

# print(SQLALCHEMY_DATABASE_URI)

class Db:

    __instance = None

    def __new__(cls, *args, **kwargs):

        if cls.__instance == None:

            engine = create_engine(SQLALCHEMY_DATABASE_URI)

            Session = sessionmaker(bind=engine)

            cls.session = Session()

            cls.__instance = object.__new__(cls)

        return cls.__instance
    

session = Db().session


# print(session)