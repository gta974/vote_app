import sqlite3

path =  "./model/" # path to created DB
DB_name = "votes.db" # DB name

def push_vote(vote, ip):
    conn = sqlite3.connect(path + DB_name) # connexion a la base de donnee
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO Main_table (vote, ip) VALUES(?,?)
                   """, (vote, ip))
    conn.commit()
    conn.close()

def get_stats(ip):
    conn = sqlite3.connect(path + DB_name) # connexion a la base de donnee
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT COUNT(ip) FROM Main_table WHERE ip = ?;
                    """,(ip,))
    resultat = cursor.fetchall()
    # print(resultat)
    nombre_de_votes_sur_ip = resultat[0][0]
    # print("nombre_vote_sur_ip = " + nombre_de_votes_sur_ip)
    # get stats
    cursor.execute("""
                    SELECT COUNT(*) FROM Main_table;
                    """)
    nombre_de_votes = cursor.fetchall()
    nombre_de_votes = nombre_de_votes[0][0]
    print("nombre_de_votes = ", nombre_de_votes)
    cursor.execute("""
                    SELECT vote, COUNT(*) FROM Main_table GROUP BY vote;
                    """)
    resultat = cursor.fetchall()
    print(resultat)
    # conn.commit()
    conn.close()
    return nombre_de_votes_sur_ip, nombre_de_votes, list(resultat)