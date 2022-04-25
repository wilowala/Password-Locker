from operator import le
import unittest
from user import  UserAccount
from credentials import UserCredentials

class TestUserAccount (unittest.TestCase):
    
    def setUp(self):
        
        self.newUserAccount = UserAccount ("William","Billy","Owalla","wilieb","owallabilly@gmail.com","@!vW1lie")
     
     
    def tearDown(self):
        
        UserAccount.userAccounts=[]   
     
    def test_init(self):
        
        self.assertEqual(self.newUserAccount.f_name,'William')
        self.assertEqual(self.newUserAccount.m_name,'Billy')
        self.assertEqual(self.newUserAccount.l_name,'Owalla')
        self.assertEqual(self.newUserAccount.u_name,'wilieb')
        self.assertEqual(self.newUserAccount.u_email,'owallabilly@gmail.com')
        self.assertEqual(self.newUserAccount.l_password,'@!vW1lie')
        
        
    def test_saveUserAcc(self):
        
        self.newUserAccount.saveUserAcc()
        self.assertEqual(len(UserAccount.userAccounts),1)
        
      
    def test_saveMultipleAccounnts(self):
        
        self.newUserAccount.saveUserAcc()
        testUserAcc = UserAccount('TestUserFirstname','TestUserMiddleName','TestUserLastName','TestUsername', 'test@gmail.com','testPassword')
        testUserAcc.saveUserAcc()
        self.assertEqual(len(UserAccount.userAccounts),2)
        
       
    def test_deleteUserAccount(self):
        
        self.newUserAccount.saveUserAcc()
        testUserAcc = UserAccount('TestUserFirstname','TestUserMiddleName','TestUserLastName','TestUsername', 'test@gmail.com','testPassword')
        testUserAcc.saveUserAcc()
        self.newUserAccount.deleteUserAccount()
        self.assertEqual(len(UserAccount.userAccounts),1)


class TestUserCredentials(unittest.TestCase):
    def setUp(self):
        
        self.newUserCredential =UserCredentials('WeChat','Aivwilie','Ow@l@123')

    def tearDown(self):
        
        UserCredentials.credentials=[]
        
              
    def test_init(self):
         
         self.assertEqual(self.newUserCredential.myAccount,'WeChat')
         self.assertEqual(self.newUserCredential.username,'Aivwilie')
         self.assertEqual(self.newUserCredential.login_pass,'Ow@l@123')
       
    def test_saveCredentials(self):

        self.newUserCredential.saveCredentials()
        self.assertEqual(len(UserCredentials.credentials),1)
       
    def testSaveMultipleUserAcc(self):
        
        self.newUserCredential.saveCredentials()
        testUserCredential =UserCredentials('Telegram','Wilieb','Ow@l@123')
        testUserCredential.saveCredentials()
        self.assertEqual(len(UserCredentials.credentials),2)
       
    def test_deleteUserCred(self):
        
        self.newUserCredential.saveCredentials()
        testUserCredential =UserCredentials('Telegram','Wilieb','Ow@l@123')
        testUserCredential.saveCredentials()
        self.newUserCredential.deleteUserCred()
        self.assertEqual(len(UserCredentials.credentials),1)
        
    def test_doCredentialsExist(self):

        self.newUserCredential.saveCredentials()
        testUserCredential =UserCredentials('Telegram','Wilieb','Ow@l@123')
        testUserCredential.saveCredentials()
        userCredentialExist= UserCredentials.doCredentialsExist('Telegram')
        self.assertTrue(userCredentialExist)  

    def test_findUsercredential(self):
        
        self.newUserCredential.saveCredentials()
        testUserCredential =UserCredentials('Telegram','Wilieb','Ow@l@123')
        testUserCredential.saveCredentials()
        userCred = UserCredentials.findUsercredential('Telegram')
        self.assertEqual(userCred.myAccount, testUserCredential.myAccount)
                
        
if __name__ == '__main__':
    unittest.main()