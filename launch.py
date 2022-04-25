from user import UserAccount
from  credentials import  UserCredentials

def createNewUserAccount(f_name, m_name, l_name, u_name, u_email, l_password):

    newUserAccount = UserAccount(f_name, m_name, l_name, u_name, u_email, l_password,)
    return newUserAccount

def saveUserAccount(userAccount):

    userAccount.saveUserAcc()

def displayUserAccount():

    return UserAccount.displayUser()

def userLogin(u_name, l_password):

    verifiedUserAccount = UserCredentials.userVerification(u_name, l_password)
    return verifiedUserAccount

def createNewusercredential( myAccountName, u_name, l_password):

    newUserCredential = UserCredentials(myAccountName, u_name, l_password)    
    return newUserCredential

def saveUserCredential(userCredential):

    userCredential.saveCredentials()

def delCredential(credentials):

    credentials.deleteUserCred()

def displayUserCredentials():

    return UserCredentials.displayUserCredentials()

def findUserCredentials(userAccount):

    return UserCredentials.findUsercredential(userAccount)

def doCredentialsExist(account):

    return UserCredentials.doCredentialsExist(account)

def copyPass(userAccount):

    return UserCredentials.copyLoginPass(userAccount)

def systemGeneratedPassword():
    
    autoGenRandPass = UserCredentials.genRandPass()
    return autoGenRandPass