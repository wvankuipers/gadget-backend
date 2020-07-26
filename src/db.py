from sqlalchemy import create_engine

db_connect = create_engine('sqlite:///chinook.db')

class Database():
  def __init__(self):
    self.conn = db_connect.connect()

  def query(self, query):
    print(query)
    return self.conn.execute(query)
