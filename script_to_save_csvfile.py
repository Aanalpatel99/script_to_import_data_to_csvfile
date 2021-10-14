import mysql.connector
import pandas as pd

cnx = mysql.connector.connect(user='root', password='mysql21',
                              host='127.0.0.1',
                              port=3306,
                              database='gamescore')

cur = cnx.cursor()
cur.execute("""SELECT userid, score FROM error""")

df = pd.DataFrame(cur.fetchall(), columns = ["userid","score"])
df.to_csv("data.csv", index=False)
