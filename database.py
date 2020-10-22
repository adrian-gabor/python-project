import sqlite3

# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')
con = sqlite3.connect('test.db')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()

# tworzenie tabel od nowa
cur.execute("DROP TABLE IF EXISTS student;")
cur.execute("DROP TABLE IF EXISTS teacher;")
cur.execute("DROP TABLE IF EXISTS hours;")


cur.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id_student INTEGER PRIMARY KEY ASC,
        first name varchar(250) NOT NULL,
        last name varchar(250) NOT NULL,
        class varchar(250) NOT NULL,
        login varchar(250) NOT NULL,
        password varchar(250) NOT NULL
    )""")


cur.execute("""
    CREATE TABLE IF NOT EXISTS teacher (
        id_teacher INTEGER PRIMARY KEY ASC,
        first name varchar(250) NOT NULL,
        last name varchar(250) NOT NULL,
        login varchar(250) NOT NULL,
        password varchar(250) NOT NULL
    )""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS hours (
        id_hours INTEGER PRIMARY KEY ASC,
        id_student INTEGER,
        id_teacher INTEGER,
        date date NOT NULL,
        value INTEGER NOT NULL,
        FOREIGN KEY(id_student) REFERENCES student(id_student),
        FOREIGN KEY(id_teacher) REFERENCES teacher(id_teacher)
    )""")


uczniowie = (
    (None, 'Tomasz', 'Nowak', '6', 'aaaa', 'haslo'),
    (None, 'Jan', 'Kos', '6', 'bbbb', 'haslo'),
    (None, 'Piotr', 'Kowalski', '6', 'cccc', 'haslo'),
    (None, 'Oskar', 'Ukleja', '6', 'dddd', 'haslo')
)

nauczyciele = (
    (None, 'Andrzej', 'Kowalski', 'aaaa', 'haslo'),
    (None, 'Adam', 'Kos', 'bbbb', 'haslo'),
    (None, 'Piotr', 'Kłos', 'cccc', 'haslo'),
    (None, 'Kuba', 'Nowak', 'dddd', 'haslo')
)


godziny = (
    (None, '1', '2', '2014-10-08', '2'),
    (None, '2', '4', '2014-10-06', '4'),
    (None, '1', '1', '2014-10-08', '2'),
    (None, '3', '2', '2014-10-09', '1')
)


# wstawiamy wiele rekordów
cur.executemany('INSERT INTO student VALUES(?,?,?,?,?,?)', uczniowie)
cur.executemany('INSERT INTO teacher VALUES(?,?,?,?,?)', nauczyciele)
cur.executemany('INSERT INTO hours VALUES(?,?,?,?,?)', godziny)

# wstawiamy kilka rekordów do bazy danych
# cur.execute('INSERT INTO student VALUES(NULL, "aaaa", "haslo");')
# cur.execute('INSERT INTO student VALUES(NULL, ?, ?, ?, );', ("dddd", "haslo"))

con.commit()