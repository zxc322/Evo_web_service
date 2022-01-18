from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.session import sessionmaker
engine = create_engine('sqlite:///alchemy.db', connect_args={'check_same_thread': False})
base = declarative_base()
session = sessionmaker(bind=engine)()


class Users(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)

    def __repr__(self):
        return '<Users(id="{}", name="{}", surname="{}", email"{}")>'.format(self.id, self.name, self.surname, self.email)


base.metadata.create_all(engine)


def query():
    data = session.query(Users)
    all_data = data.all()
    return all_data


def find_email_user(email):
    data = session.query(Users)
    founded_user = data.filter_by(email=email).all()
    return founded_user


