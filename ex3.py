#ex3.py

#Class declaration
class Jungle:
    #constructor with default values
    def __init__(self, name="Unknown"):
        self.visitorName = name

    def welcomeMessage(self):
        print("Hello %s, Welcome to the Jungle" % self.visitorName)

#Create object of class Jungle
j = Jungle('Mehar')
j.welcomeMessage() # Hello Mehar, Welcome to the Jungle
#If no name is passed, the defaut value i.e Unknow will be used
k = Jungle()
k.welcomeMessage() # Hello Unknnow, welcome to the jungle