import sqlite3

conn = sqlite3.connect("bot_data.db")
cursor = conn.cursor()

print("Usuarios:")
for fila in cursor.execute("SELECT * FROM usuarios"):
    print(fila)

print("\nConversaciones:")
for fila in cursor.execute("SELECT * FROM conversaciones"):
    print(fila)

conn.close()
