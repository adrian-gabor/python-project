import sqlite3
import stdiomask
# utworzenie połączenia z bazą przechowywaną na dysku lub w pamięci (':memory:')
con = sqlite3.connect('test.db')

def login():
    input_login = input("Podaj login: ")
    cur.execute('SELECT * FROM logowanie WHERE login=?;', (input_login,) )
    wynik = cur.fetchone()
    
    # print(wynik)
    if type(wynik) != type(None):
        tuple(wynik)
        #pobieram z obiektu
        password_from_base=wynik[2]
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
        
def new_login():
    new_login = input("Podaj login:" )
    cur.execute('SELECT * FROM logowanie WHERE login=?;', (new_login,) )
    wynik1 = cur.fetchone()
    if (type(wynik1) != type(None)):
        print("Taki login już istnieje. Podaj inny login")
        new_login()
    else:
        print("Login poprawny")
        new_password = stdiomask.getpass(prompt="Podaj haslo: ")
        cur.execute('INSERT INTO logowanie VALUES(NULL, ?, ?);', (new_login, new_password))
        con.commit()


# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row
# utworzenie obiektu kursora
cur = con.cursor()
# zatwierdzamy zmiany w bazie
con.commit()


print("Witam w naszym zjebanym serwisie")
#login()
print("Załóż konto zjebie")
new_login()










