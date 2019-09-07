import mysql.connector
import logging
import time
import datetime
from mysql.connector import Error


class Db:
    def __init__(self):

        # Create a connection to the database
        self.cnx = mysql.connector.connect(
            database="brexbot",
            host="198.71.225.59",
            port=3306,
            user="brexbot",
            password="6Ke04_ij")
        
        logging.info("Connected.")

        # Get a cursor
        self.cur = self.cnx.cursor()

    # Check if a user exists in the database
    def viewer_exists(self, twitchusername, channel):

        self.cur.execute(
            "SELECT twitchusername, COUNT(*) FROM viewer WHERE channel = %s GROUP BY twitchusername",
            (channel,))

        if self.cur.fetchone() is not None:
            logging.debug(twitchusername + " exists in " + channel + "'s channel.")
            self.cnx.close()
            return True
        else:
            logging.debug(twitchusername + " doesn't exist in " + channel + "'s channel.")
            self.cnx.close()
            return False

    # Add a user to the database using twitchusername and twitchuserid
    def create_viewer(self, twitchusername, channel, twitchuserid):
        try:
            sql = "INSERT INTO viewer (twitchusername, channel, twitchuserid, points) " \
                  "VALUES (%s, %s, %s, %s)"
            val = (twitchusername, channel, twitchuserid, 1000)
            self.cur.execute(sql, val)
            self.cnx.commit()
            self.cnx.close()
            logging.debug("Added user " + twitchusername)
        except Error as e:
            logging.error("Unable to create viewer.", e)

    # Used to add points to all viewers currently in the chat
    def add_points(self, viewer_list, channel, points):
        try:
            self.cur.execute("SELECT * FROM viewer")
            results = self.cur.fetchall()
            for row in results:
                if row[1] in viewer_list:
                    sql = """UPDATE viewer SET points = %s WHERE twitchusername = %s AND channel = %s"""
                    val = (points + row[4], row[1], channel)
                    self.cur.execute(sql, val)
            self.cnx.commit()
            self.cnx.close()
            logging.debug("All points added, changes committed and database closed.")
            return True
        except Error as e:
            logging.error("Unable to add points", e)
            return False

    # Used to remove points from a viewer / list of viewers
    def remove_points(self, twitchusername, channel, points):
        try:
            self.cur.execute("SELECT * FROM viewer")
            results = self.cur.fetchall()
            for row in results:
                if row[1] in twitchusername:
                    sql = """UPDATE viewer SET points = %s WHERE twitchusername = %s AND channel = %s"""
                    val = (row[4] - points, row[1], channel)
                    self.cur.execute(sql, val)
            self.cnx.commit()
            self.cnx.close()
            logging.debug("Points removed, changes committed and database closed.")
            return True
        except Error as e:
            logging.error("Unable to remove points", e)
            return False

    # Retrieve points from the database.
    # To be used with games and point checking command
    def get_points(self, twitchusername, channel):
        try:
            self.cur.execute(
                "SELECT points FROM viewer WHERE twitchusername = %s AND channel = %s",
                (twitchusername, channel))
            result = self.cur.fetchone()
            return result[0]
        except Error as e:
            logging.error("Unable to retrieve points", e)

    # Add a timestamp to the database when a viewer plays a game.
    def add_last_game_time(self, twitchusername, channel, game_type):
        try:
            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            if game_type == "dice":
                sql = """UPDATE viewer SET lastgamble = %s WHERE twitchusername = %s AND channel = %s"""
                val = (timestamp, twitchusername, channel)
                self.cur.execute(sql, val)
            elif game_type == "roulette":
                sql = """UPDATE viewer SET lastroulette = %s WHERE twitchusername = %s AND channel = %s"""
                val = (timestamp, twitchusername, channel)
                self.cur.execute(sql, val)
            self.cnx.commit()
            self.cnx.close()
        except Error as e:
            logging.error("Unable to set time stamp", e)

    # Check database for time since last gamble (minutes)
    def time_since_last_gamble(self, twitchusername, channel):
        try:
            ts = time.time()
            current_time = datetime.datetime.fromtimestamp(ts)
            self.cur.execute(
                "SELECT lastgamble FROM viewer WHERE twitchusername = %s AND channel = %s",
                (twitchusername, channel))
            result = self.cur.fetchone()
            last_gamble = result[0]
            time_difference = current_time - last_gamble
            time_in_minutes = time_difference.total_seconds() / 60
            print(time_in_minutes)
            return time_in_minutes
        except Error as e:
            logging.error("Unable to retrieve time data.")

    # Commit db changes
    def commit(self):
        try:
            self.cnx.commit()
            return True
        except Error as e:
            logging.error("Error on committing db changes: ", e)
            return False

    # Close connection
    def close(self):
        try:
            self.cnx.close()
            logging.debug("DB connection closed.")
            return True
        except Error as e:
            logging.error("Error on closing connection: ", e)
            return False
