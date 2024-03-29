__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

import random
from Db import Db
import logging
import random
from random import shuffle

logging.basicConfig(level=logging.DEBUG)


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
    def __init__(self, twitchusername, bet):

        # Create the connection the database and retrieve viewers current points
        con = Db()
        points = con.get_points(twitchusername)
        if points < bet:
            # This will be a twitch message when using an API
            logging.error("You do not have enough points to make this bet")
        else:
            logging.info("Running bet")
            number_rolled = random.randint(1, 100)
            if number_rolled <= 50:
                con.remove_points(twitchusername, bet)
                logging.info(twitchusername + " lost.")
            elif 51 <= number_rolled <= 95:
                con.add_points(twitchusername, bet)
                logging.info(twitchusername + " won.")
            else:
                big_win = bet * 1.5
                con.add_points(twitchusername, big_win)
                logging.info(twitchusername + " won the big one.")


# class GangWars:
#     def __init__(self, channel, bet):
#         self.channel = channel
#         self.bet = bet
#         self.gang_names = ['Cali Cartel', 'Norte', 'North Coast Cartel', 'Leticia Cartel', 'Los Rastrojos', 'New Generation', 'Los Nevados', 'Los Machos', 'Bloque Meta', 'Libertadores', 'Black Eagles']
#         self.gang_selection = random.sample(self.gang_names, 2)
#         self.viewers = []
#         self.shuffle = shuffle(self.gang_names)














