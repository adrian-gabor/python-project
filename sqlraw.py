import sqlite3
import stdiomask
# utworzenie połączenia z bazą przechowywaną na dysku lub w pamięci (':memory:')
con = sqlite3.connect('test.db')

# funkcja do logowania sie dla nauczycieli
def login():
    input_login = input(" Nauczycielu podaj login: ")
    cur.execute('SELECT * FROM teacher WHERE login=?;', (input_login,) )
    wynik = cur.fetchone()
    
    # print(wynik)
    if type(wynik) != type(None):
        tuple(wynik)
        #pobieram z obiektu
        password_from_base=wynik[4]
        print("Login poprawny")
        input_password = stdiomask.getpass(prompt="Podaj haslo: ")
        if(password_from_base == input_password):
            print("Hasło poprawne")
        else: 
            print("Hasło niepoprawne")
            login()
    else: 
        print("Login niepoprawny. WYPIERDALAJ")
        login()


# funkcja dodająca nowego ucznia 
def new_login():
    new_login = input("Podaj login:" )
    cur.execute('SELECT * FROM student WHERE login=?;', (new_login,) )
    wynik1 = cur.fetchone()
    if (type(wynik1) != type(None)):
        print("Taki login już istnieje. Podaj inny login")
        new_login()
    else:
        print("Login poprawny")
        new_first_name = input("Podaj imie: ")
        new_last_name = input("Podaj nazwisko: ")
        new_class = input("Podaj klase: ")
        new_password = stdiomask.getpass(prompt="Podaj haslo: ")
        cur.execute('INSERT INTO student VALUES(NULL,?,?,?,?,?);', (new_first_name, new_last_name, new_class, new_login, new_password))
        con.commit()


# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row
# utworzenie obiektu kursora
cur = con.cursor()
# zatwierdzamy zmiany w bazie
con.commit()

# login()
print("Witam w naszym zjebanym serwisie")
print("Załóż konto zjebie")
new_login()










