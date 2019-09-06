import mysql.connector
import logging
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

    def viewer_exists(self, twitchusername):

        self.cur.execute(
            "SELECT twitchusername, COUNT(*) FROM viewer WHERE twitchusername = %s GROUP BY twitchusername",
            (twitchusername,))

        if self.cur.fetchone() is not None:
            logging.debug(twitchusername + " exists!")
            return True
        else:
            logging.debug(twitchusername + " doesn't exist!")
            return False

    def create_viewer(self, twitchusername, twitchuserid):
        try:
            sql = "INSERT INTO viewer (twitchusername, twitchuserid, points) " \
                  "VALUES (%s, %s, %s)"
            val = (twitchusername, twitchuserid, 1000,)
            self.cur.execute(sql, val)
            self.cnx.commit()
            self.cnx.close()
            logging.debug("Added user " + twitchusername)
        except Error as e:
            logging.error("Unable to create viewer.", e)


logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')

con = Db()
con.create_viewer("tomisme", 1)