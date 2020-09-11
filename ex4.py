# ex4.py

# class declaration

from jungleBook import Jungle, RateJungle


def main():
    # crete object of class jungle
    r = RateJungle

    r.printRating()
    r.welcomeMessage()
    j = Jungle("Meher")
    j.welcomeMessage()  # Hello Meher,Welcome to the jungle

    # if no name is passed, the value i.e Unknown will be used
    k = Jungle()
    k.welcomeMessage()

    # Standard boileplate to set 'main' as starting function

    if __name__ == '__main__':
        main()
