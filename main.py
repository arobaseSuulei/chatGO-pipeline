import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    user="chatgouser",
    password="123",
    dbname="chatgo"
)

print("✅ Connecté à PostgreSQL !")

# création d'un curseur
cur=conn.cursor()

# création d'une table
cur.execute("""
CREATE TABLE IF NOT EXISTS messages(
    id SERIAL PRIMARY KEY,
    sender VARCHAR(50),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

""")

#commit les changements
conn.commit()

# Optionnel : insérer une ligne
cur.execute("""
INSERT INTO messages (sender, content) VALUES (%s, %s)
""", ("Alice", "Salut le monde !"))


conn.commit()

# Récupérer le contenu pour vérifier
cur.execute("SELECT * FROM messages;")
rows = cur.fetchall()
for row in rows:
    print(row)

# Fermer la connexion
cur.close()
conn.close()
