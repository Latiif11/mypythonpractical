#jungleBook.py

#class declaration
class Jungle:
    #Condtructor with default value
   def __init__(self, name='Unknown'):
       self.visitorName= name

   def welcomeMessage(self):
       print('Hello %s, welcome to the Jungle' % self.visitorName)

class RateJungle(Jungle):
    def __init__(self, name, feedback):
        # feddback (1-10)
        self.feedback = feedback # Publick attribute

        super().__init__(name)

        # using parent class attribute i.e visitorname
        def printRating(self):
            print('Thanks %s for your beedback'% self.visitorName)