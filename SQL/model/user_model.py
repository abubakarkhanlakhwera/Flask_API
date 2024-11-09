import mysql.connector
import json
class Bwp():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host='localhost',user='root',password='qwerty.',database='abubakar')
            self.cur = self.con.cursor(dictionary=True)
            print("Connected to database")
        except :
            print("error in connection")
            
    def user_signup(self):
        self.cur.execute("SELECT * FROM abubakar.user_controller")
        result = self.cur.fetchall()
        if len(result) > 0:
            return json.dumps(result)
        else:    
            return "No user found"
    