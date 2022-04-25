import string, random
from user import UserAccount

class UserCredentials:

    credentials=[]

    @classmethod
    def userVerification(cls, u_name, l_password):
       
        _user = " "
        for user in UserAccount.userAccounts:
            if user.u_name == u_name and user.l_password ==l_password:
                _user == user.u_name
        return _user

    def __init__(self,myAccount, u_name, l_password):
        '
        self.myAccount = myAccount        
        self.u_name = u_name
        self.l_password = l_password