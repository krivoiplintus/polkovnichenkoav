class User:

    def __init__(self, first_name, last_name):

        self.userfirstname = first_name
        self.userlastname = last_name

    def sayname(self):
        print(self.userfirstname)

    def saylastname(self):
        print(self.userlastname)

    def say(self):
        print(self.userfirstname, self.userlastname)
