class UserAccount:

    userAccounts=[]

    def __init__(self,f_name,m_name,l_name,u_name,u_email,l_password ):
        
        self.f_name = f_name 
        self.m_name = m_name 
        self.l_name = l_name 
        self.u_name = u_name 
        self.u_email = u_email
        self.l_password = l_password 
    
    def saveUserAcc(self):

        UserAccount.userAccounts.append(self)

    def deleteUserAccount(self):
        
        UserAccount.userAccounts.remove(self)
    
     @classmethod   
    def displayUser(cls):
        
        return cls.userAccounts