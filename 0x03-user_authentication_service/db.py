"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import User, Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Creates New User instance and
        saves them to database.
        Args:
            - email
            - hashed_password
        Return:
            - new User object
        """
        session = self._session
        user = User(email=email, hashed_password=hashed_password)
        session.add(User)
        session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        find user
        """
        if not kwargs:
            raise InvalidRequestError
        try:
            user - self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoRsultFound
            return user
        except InvalidRequestError:
            raise InvalidRequestError
        except NoResultFound:
            raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                raise ValueError
        self._session.commit()
