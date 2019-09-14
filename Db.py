from models.User import User

__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

import mysql.connector
import logging
import time
import datetime
import Config
from mysql.connector import Error
from datetime import datetime
import TwitchApi

logging.basicConfig(level=logging.DEBUG)

class Db:
    # database="brexbot", host="198.71.225.59", port=3306, user="brexbot", password="6Ke04_ij"
    def __init__(self, host=Config.HOST, database=Config.DATABASE, username=Config.USERNAME, password=Config.PASSWORD, port=Config.PORT):
        # Create a connection to the database
        self.cnx = mysql.connector.connect(
            database=database,
            host=host,
            port=port,
            user=username,
            password=password)
        
        logging.info("Connected.")

        # Get a cursor
        self.cur = self.cnx.cursor()

    # Check if a user exists in the database
    def viewer_exists(self, viewer, channel):
        self.cur.execute(
            "SELECT viewer, COUNT(*) FROM viewer WHERE channel = %s GROUP BY viewer",
            (channel,))

        if self.cur.fetchone() is not None:
            logging.debug(viewer + " exists in " + channel + "'s channel.")
            return True
        else:
            logging.debug(viewer + " doesn't exist in " + channel + "'s channel.")
            return False

    # Add a user to the database using twitchusername and twitchuserid
    def create_viewer(self, twitchusername, channel, twitchuserid):
        try:
            sql = "INSERT INTO viewer (viewer, channel, viewer_id, points) " \
                  "VALUES (%s, %s, %s, %s)"
            val = (twitchusername, channel, twitchuserid, 0)
            self.cur.execute(sql, val)
            self.cnx.commit()
            logging.debug("Added user " + twitchusername)
        except Error as e:
            logging.exception("Unable to create viewer.", e)

    def remove_viewer(self, twitchusername, channel, twitchuserid):
        try:
            sql = "DELETE FROM viewer where viewer_id = " + str(twitchuserid) + " AND channel = '" + channel + "'" + " AND viewer = '" + twitchusername + "'"
            self.cur.execute(sql)
            self.cnx.commit()
            logging.debug("removed user " + twitchusername)
        except Error as e:
            logging.exception("Unable to remove viewer.", e)

    # Used to add points to all viewers currently in the chat
    def add_points(self, viewer_list, channel, points):
        try:
            self.cur.execute("SELECT * FROM viewer")
            results = self.cur.fetchall()
            for row in results:
                if row[1] in viewer_list:
                    sql = """UPDATE viewer SET points = %s WHERE viewer = %s AND channel = %s"""
                    val = (points + row[4], row[1], channel)
                    self.cur.execute(sql, val)
            self.cnx.commit()
            logging.debug("All points added, changes committed and database closed.")
            return True
        except Error as e:
            logging.exception("Unable to add points", e)
            return False

    # Used to remove points from a viewer / list of viewers
    def remove_points(self, twitchusername, channel, points):
        try:
            self.cur.execute("SELECT * FROM viewer")
            results = self.cur.fetchall()
            for row in results:
                if row[1] in twitchusername:
                    sql = """UPDATE viewer SET points = %s WHERE viewer = %s AND channel = %s"""
                    val = (row[4] - points, row[1], channel)
                    self.cur.execute(sql, val)
            self.cnx.commit()
            logging.debug("Points removed, changes committed and database closed.")
            return True
        except Error as e:
            logging.exception("Unable to remove points", e)
            return False

    # Retrieve points from the database.
    # To be used with games and point checking command
    def get_points(self, twitchusername, channel):
        try:
            self.cur.execute(
                "SELECT points FROM viewer WHERE viewer = %s AND channel = %s",
                (twitchusername, channel))
            result = self.cur.fetchone()
            return result[0]
        except Error as e:
            logging.exception("Unable to retrieve points", e)

    # Add a timestamp to the database when a viewer plays a game.
    def add_last_game_time(self, twitchusername, channel, game_type):
        try:
            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            if game_type == "dice":
                sql = """UPDATE viewer SET lastgamble = %s WHERE viewer = %s AND channel = %s"""
                val = (timestamp, twitchusername, channel)
                self.cur.execute(sql, val)
            elif game_type == "roulette":
                sql = """UPDATE viewer SET lastroulette = %s WHERE viewer = %s AND channel = %s"""
                val = (timestamp, twitchusername, channel)
                self.cur.execute(sql, val)
            self.cnx.commit()
        except Error as e:
            logging.exception("Unable to set time stamp", e)

    # Check database for time since last gamble (minutes)
    def time_since_last_gamble(self, twitchusername, channel):
        try:
            ts = time.time()
            current_time = datetime.datetime.fromtimestamp(ts)
            self.cur.execute(
                "SELECT lastgamble FROM viewer WHERE viewer = %s AND channel = %s",
                (twitchusername, channel))
            result = self.cur.fetchone()
            last_gamble = result[0]
            time_difference = current_time - last_gamble
            time_in_minutes = time_difference.total_seconds() / 60
            print(time_in_minutes)
            return time_in_minutes
        except Error as e:
            logging.exception("Unable to retrieve time data.", e)

    #####################################################################################
    # USER functions
    #####################################################################################
    # get user from database
    # parameter: username as string
    def get_user(self, username):
        """

        :type username: username String
        """
        try:
            self.cur.execute("SELECT * FROM app_user WHERE username = %s", (username,))
            result = self.cur.fetchone()
            if result is not None:
                user = User(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])
                logging.info("Got user: " + user.username + " from database")
            else:
                user = None
            return user
        except Error as e:
            logging.exception("Error getting user: " + username)

    # create user in database
    # parameter: User object
    def create_user(self, user: User):
        try:
            sql = "INSERT INTO app_user (username, password, channel, bot_name, bot_oauth, channel_token, created, last_active) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (user.username, user.password, None, None, None, None, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            res = self.cur.execute(sql, val)
            self.commit()
            logging.info("Created user: " + user.username + " in database")
            return res
        except Error as e:
            logging.exception("Error creating user: " + user.username)

    # delete user from database
    # parameter: User object
    def remove_user(self, user: User):
        try:
            res = self.cur.execute("DELETE FROM app_user where username = '" + user.username + "'")

            # delete all other channel data in all tables
            if(user.channel != None):
                self.cur.execute("DELETE FROM command where channel = '" + user.channel + "'")
                self.cur.execute("DELETE FROM giveaway where channel = '" + user.channel + "'")
                self.cur.execute("DELETE FROM media_request where channel = '" + user.channel + "'")
                self.cur.execute("DELETE FROM loyalty where channel = '" + user.channel + "'")
                self.cur.execute("DELETE FROM poll where channel = '" + user.channel + "'")
                self.cur.execute("DELETE FROM quote where channel = '" + user.channel + "'")
                self.cur.execute("DELETE FROM viewer where channel = '" + user.channel + "'")
                
            self.commit()
            logging.info("Removed user: " + user.username + " from database")
            return res
        except Error as e:
            logging.exception("Error deleting user: " + user.username)

    #####################################################################################
    # Media Functions
    #####################################################################################

    def load_media(self, _id, channel):
        sql = 'SELECT * FROM media_request WHERE id = ' + str(_id) + ' AND channel = \"' + channel + '\"'
        self.cur.execute(sql)
        return self.cur.fetchone()

    def load_all(self, channel):
        sql = 'SELECT * FROM media_request WHERE channel = \"' + channel + '\"'
        self.cur.execute(sql)
        return self.cur.fetchall()

    def save_media(self, keys, values):
        self.cur.execute("INSERT INTO media_request (" + keys + ") VALUES (" + values + ")")
        self.commit()

    def delete_media(self, _id):
        self.cur.execute("DELETE FROM media_request where id = '" + _id + "'")
        self.commit()

    #####################################################################################
    # Helper functions
    # Commit db changes
    def commit(self):
        try:
            self.cnx.commit()
            return True
        except Error as e:
            logging.exception("Error on committing db changes: ", e)
            return False

    # Close connection
    def close(self):
        try:
            self.cnx.close()
            logging.debug("DB connection closed.")
            return True
        except Error as e:
            logging.exception("Error on closing connection: ", e)
            return False
