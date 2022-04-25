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

def main():

    print("Wilkomen to our password locker app\n")
    print("Please enter your name")
    username= input()
    print(f"Hi {username}, use the following codes to get you started")
    print("CA: To create a new account")
    print("LI: To  login into your account")
    comands= input().upper().strip()
    
    if comands == "CA":

        print("==="*10)
        print("Enter Your First Name: ")
        f_name = input()
        print("Enter Your Middle Name: ")
        m_name = input()
        print("Enter Your Last Name: ")
        l_name = input()
        print("Enter Your Email: ")
        usermail = input()
        print("Enter preffered Username: ")
        username= input()
        
        while True:

            print("MP: To enter your password")
            print("GP: To generate password")
            command= input().upper().strip()

            if command == "MP":

                print("PLease enter password: ")
                login_pass= input()
                break

            elif command == "GP":

                login_pass= systemGeneratedPassword()
                break

            else:

                print("Please select a valid option")

        saveUserAccount(createNewUserAccount(f_name,m_name,l_name,username,usermail,login_pass))
        print("="*30)
        print(f" Thank you {username}. You have successfully signed up ")
        displayUserAccount()

    elif comands =="LI":

        print("Enter username and password to sign in: ")
        username= input("Username:  ")
        login_pass= input("Password:  ")
        userlogins = userLogin(username,login_pass)
        if userLogin == userlogins:
            print(f"Hi, {username}. Welcome back to PasswordLocker\n")

    while True:

        print("Please key in any of the following to proceed \n")
        print("CC: Create new user Credential")
        print("DC: Display existing Account credentials")
        print("FC: Find User Credential")
        print("GP: Auto generated Password")
        print("DEL: Delete account credential")
        print("X: Exit application")

        command= input().upper().strip()

        if command == "CC":

            print("Create new user Account Credential")
            print("="*30)
            print("Enter account Name : ")
            userAccountName = input().upper().strip()

            print("Username for above account")
            accUsername =input().strip()

            while True:

                print("1 - Type Password ")
                print("2 - Use system Generated Password")
                p_choice= input().strip()

                if p_choice == "1":

                    print("Type Password : ")
                    password = input()
                    break

                elif p_choice == "2":

                    password= systemGeneratedPassword()
                    break

                else:
                    print(" Incorrect command choice. Try again")

            saveUserCredential(createNewusercredential(userAccountName,accUsername,password))
            print("\n")
            print(f"Credential for {userAccountName}  Username: {accUsername} and Password: {password} have been successfully")
            print("\n")

        elif command == "DC" :

            if displayUserCredentials():

                print("Available Accounts: ")

                for acc in displayUserCredentials():

                    print(f"Account: {acc.myAccount}")
                    print(f"Username: {username}")
                    print(f"Password: {password}")

                print("---"*10)

            else:

                print("Error! The entered credentials do not exist! ")

        elif command == "FC":

            print("Enter account to find: ")
            accountName = input().upper().strip

            if findUserCredentials(accountName):

                searchAcc = findUserCredentials(accountName)
                print(f"Account : {searchAcc.myAccount} \n")
                print(f"Username: { searchAcc.username} \n")

            else:

                print(f"accountName doesnt exist \n")

        elif command == "GP":

            password = systemGeneratedPassword()
            print(f"Your generated password is : {password}")

        elif command == "DEL":

            print("Enter Account to Delete ")
            accountName = input().upper().strip()

            if findUserCredentials(accountName):

                searchAcc = findUserCredentials(accountName)
                print("")
                searchAcc.deleteUserCred()
                print(f"{ searchAcc.myAccount} deleted successfully \n")

            else:

                print(f"{accountName} Fatal: The account does not exist \n")

        elif command == "X":

            print("Goodbye....\n")
            print("="*20)
            break

        else:

            print("I didn't get that, really. Please enter a valid command!")
                
    
if __name__ == "__main__":
    main()