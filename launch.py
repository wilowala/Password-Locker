from user import UserAccount
from  credentials import  UserCredentials

def createNewUserAccount(f_name, m_name, l_name, u_name, u_email, l_password):
    
    newUserAccount = UserAccount(f_name, m_name, l_name, u_name, u_email, l_password,)
    return newUserAccount