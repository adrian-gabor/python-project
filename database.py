import sqlite3

# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')
con = sqlite3.connect('test.db')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()

# tworzenie tabel od nowa
cur.execute("DROP TABLE IF EXISTS logowanie;")

cur.execute("""
    CREATE TABLE IF NOT EXISTS logowanie (
        id INTEGER PRIMARY KEY ASC,
        login varchar(250) NOT NULL,
        password varchar(250) NOT NULL
    )""")



# wstawiamy kilka rekordów do bazy danych
cur.execute('INSERT INTO logowanie VALUES(NULL, "aaaa", "haslo");')
cur.execute('INSERT INTO logowanie VALUES(NULL, "bbbb", "haslo");')
cur.execute('INSERT INTO logowanie VALUES(NULL, "cccc", "haslo");')
cur.execute('INSERT INTO logowanie VALUES(NULL, ?, ?);', ("dddd", "haslo"))

con.commit()