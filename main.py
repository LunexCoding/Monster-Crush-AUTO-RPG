from entrance import loginAttempt
from consoleAccess import console


if __name__ == '__main__':
    console.showMessage(loginAttempt.showMsg())
    loginAttempt.getDataFromDB()