import string, random
from user import UserAccount

class UserCredentials:

    credentials=[]

    @classmethod
    def userVerification(cls,u_name,l_password):
       
        _user = " "
        for user in UserAccount.userAccounts:
            if user.u_name == u_name and user.l_password ==l_password:
                _user == user.u_name
        return _user

    