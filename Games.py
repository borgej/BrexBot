import random


class Roulette:
    def __init__(self, user):
        self.user = user

        bullet_position = random.randint(1, 6)
        trigger_pulled = random.randint(1, 6)

        print(user + " places the gun to their head and pulls the trigger....")

        if trigger_pulled == bullet_position:
            # print call to be replaced with Twitch chat message post
            print("The gun fires and blows " + user + "'s brains all over the floor!!")
            # Replace below code with Twitch API call to time out user.
            # user.timeout(60)
        else:
            print("Click... " + user + " survived!!")


class Dice:
    def __init__(self, user, loot, bet):
        # Retrieve viewers loot from the data base
        # .......some database code call here......
        # The bet will also be determined from the viewers gamble message
        number_rolled = random.randint(1, 100)

        bet_string = str(bet)
        roll_string = str(number_rolled)

        if number_rolled <= 50:
            print(user + " rolled a " + roll_string + ". And lost " + bet_string + ".")
            loot -= bet
        elif 51 <= number_rolled <= 95:
            print(user + " rolled a " + roll_string + ". And won " + bet_string + ".")
            loot += bet
        else:
            big_win = bet * 1.5
            big_string = str(big_win)
            print(user + " rolled a " + roll_string + ". And won " + big_string + ". High Roller!")
            loot += big_win













