import 

conn =.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    vip_status INTEGER DEFAULT 0
)
""")

conn.commit()
conn.close()