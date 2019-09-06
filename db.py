import mysql.connector


class DatabaseConnection:
    def __init__(self):

        # Create a connection to the database
        self.cnx = mysql.connector.connect(
            database="brexbot",
            host="198.71.225.59",
            port=3306,
            user="brexbot",
            password="6Ke04_ij")

        # Get a cursor
        self.cur = self.cnx.cursor()

    def check_exists(self, viewer):

        self.cur.execute(
            "SELECT twitchusername, COUNT(*) FROM viewer WHERE twitchusername = %s GROUP BY twitchusername",
            (viewer,))

        if self.cur.fetchone() is not None:
            print(viewer + " already exists in the database.")
        else:
            print(viewer + " does not currently exist. Adding " + viewer + ".....")
            sql = "INSERT INTO viewer (twitchusername, twitchuserid, points) " \
                  "VALUES (%s, %s, %s)"
            val = (viewer, 1, 1000,)
            self.cur.execute(sql, val)
        self.cnx.commit()
        self.cnx.close()

    def loot_check(self,):


db = DatabaseConnection()

db.check_exists("bob")





