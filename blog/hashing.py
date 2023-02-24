""" Pass """
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    """ Pass """

    @staticmethod
    def bcrypt(password: str):
        """ pass """
        return pwd_cxt.hash(password)
