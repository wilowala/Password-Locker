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

    def saveCredentials(self):
        
        UserCredentials.credentials.append(self)

    def deleteUserCred(self):
        
        UserCredentials.credentials.remove(self)

    def genRandPass(passwordlen=8):
        
        userPassword = string.ascii_letters  + string.digits
        return "".join(random.choice(userPassword)for char in range(passwordlen))

    @classmethod
    def findUsercredential(cls,userAccount):
        
        for userCredential in cls.credentials:

            if userCredential.myAccount == userAccount:

                return userCredential

    @classmethod
    def doCredentialsExist(cls,account):
        
        for item in cls.credentials:

            if item.myAccount == account:

                return True

        return False

    @classmethod
    def displayUserCredentials(cls):

        return cls.credentials

    @classmethod
    def copyLoginPass(cls,userAccount):
        
        credFound = UserCredentials.findUsercredential(userAccount)
        pyperclip.copy(credFound.login_pass)