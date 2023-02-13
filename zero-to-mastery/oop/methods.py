
userData = dict()


class User:
    def __init(self, first_name, last_name, username, email, age, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.age = age
        self.password = password
        self.is_logged_in = False

    def signup(self):
        '''This method will allow a user to sign up'''
        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.username = input("Enter your username: ")
        self.email = input("Enter your email: ")
        self.age = input("Enter your age: ")
        self.password = input("Enter your password: ")
        userData["first_name"] = self.first_name
        userData["last_name"] = self.last_name
        userData['username'] = self.username
        userData['email'] = self.email
        userData['age'] = self.age
        userData['password'] = self.password
        userData['is_logged_in'] = False
        print("You have successfully signed up!")
        return self

    def login(self):
        '''This method will allow a user to login'''
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        self.is_logged_in = True
        print("You have successfully logged in!")
        return self

    def logout(self):
        '''This method will allow a user to logout'''
        self.is_logged_in = False
        print("You have successfully logged out!")
        return self


user_1 = User()

user_1.login()
user_1.logout()
user_1.signup()

print(userData)
