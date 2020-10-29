import os
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.dialects.sqlite import \
            BLOB, BOOLEAN, CHAR, DATE, DATETIME, DECIMAL, FLOAT, \
            INTEGER, NUMERIC, JSON, SMALLINT, TEXT, TIME, TIMESTAMP, \
            VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import stdiomask
from datetime import date


if os.path.exists('test.db'):
    os.remove('test.db')
# tworzymy instancję klasy Engine do obsługi bazy
baza = create_engine('sqlite:///test.db')  # ':memory:'

# klasa bazowa
BazaModel = declarative_base()


class Student(BazaModel):
    __tablename__ = 'student'
    id_student = Column(Integer, primary_key = True)
    first_name = Column(VARCHAR(100), nullable = False)
    last_name = Column(String(100), nullable = False)
    group = Column(Integer, nullable = False)
    login = Column(String(100), nullable = False)
    password = Column(String(100), nullable = False)
    godziny = relationship('Hours', backref = 'student')
    
    
class Teacher(BazaModel):
    __tablename__ = 'teacher'
    id_teacher = Column(Integer, primary_key = True)
    first_name = Column(String(100), nullable = False)
    last_name = Column(String(100), nullable = False)
    login = Column(String(100), nullable = False)
    password = Column(String(100), nullable = False)
    godziny = relationship('Hours', backref = 'teacher')
    

class Hours(BazaModel):
    __tablename__ = 'hours'
    id_hours = Column(Integer, primary_key = True)
    value = Column(Integer, nullable = False)
    date = Column(DATE, nullable = False)
    id_student = Column(Integer, ForeignKey('student.id_student'))
    id_teacher = Column(Integer, ForeignKey('teacher.id_teacher'))
    
    
# tworzymy tabele
BazaModel.metadata.create_all(baza)
    
# tworzymy sesję, która przechowuje obiekty i umożliwia "rozmowę" z bazą
BDSesja = sessionmaker(bind=baza)
sesja = BDSesja()


# dodajemy dane wielu uczniów
sesja.add_all([
    Student(first_name='Tomasz', last_name='Nowak', group=5, login='aaaa', password='haslo'),
    Student(first_name='Jan', last_name='Kos', group=5, login='bbbb', password='haslo'),
    Student(first_name='Piotr', last_name='Kowalski', group=5, login='cccc', password='haslo'),
    Student(first_name='Oskar', last_name='Ukleja', group=5, login='dddd', password='haslo'),
    Student(first_name='Adam', last_name='Debil', group=5, login='eeee', password='haslo'),
    ])  
    
    
sesja.add_all([
    Teacher(first_name='Andrzej', last_name='Kowalski', login='aaaa', password='haslo'),
    Teacher(first_name='Tomasz', last_name='Kos', login='bbbb', password='haslo'),
    Teacher(first_name='Kuba', last_name='Nowak', login='cccc', password='haslo'),
    Teacher(first_name='Oskar', last_name='Elo', login='dddd', password='haslo'),
    Teacher(first_name='Marek', last_name='Frajer', login='eeee', password='haslo'),
    ])      
    


sesja.add_all([
    Hours(value='2', date=date(2014,10,6), id_student='1', id_teacher='4'),
    Hours(value='4', date=date(2014,10,8), id_student='2', id_teacher='1'),
    Hours(value='2', date=date(2014,10,7), id_student='3', id_teacher='1'),
    Hours(value='1', date=date(2014,10,8), id_student='1', id_teacher='3'),
    Hours(value='3', date=date(2014,10,8), id_student='4', id_teacher='2'),
    ])     
    
sesja.commit()


#funkcja logowania dla nauczyciela
def login():
    print("Witamy w naszym zjabanym serwisie")
    input_login = input("Podaj login:")
    found_teacher = sesja.query(Teacher).filter_by(login=input_login).one_or_none()
    print(type(found_teacher))
    if type(found_teacher) != type(None):
        input_password = stdiomask.getpass(prompt="Podaj hasełko: ")
        if input_password == found_teacher.password:
            print("Gratulacje kurwa")
        else:
            print("Złe hasło")
            login()
    else:
        print("Zły login")
        login()

# funkcja do usuwania rekordów z dowolnej tabeli
# PROBLEM że jak ktoś wpisze indeks którego nie ma to wypierdoli błąd 
def delete_record():
    table = input("Z jakiej tabeli usunąć rekord:")
    #Wyświtlamy naszą tabele i pytamy o indeks rekordu który chcemy usunąć
    show_table(table)
    record = input("Który wiersz usunąć:")
    #Za pomocą funkcji eval() zmieniamy obiekt klast String na obiekt klasy wartości naszego stringa
    sesja.delete(sesja.query(eval(table)).get(int(record)))
    show_table(table)
    sesja.commit()



#funkcja wyswietlająca tabele ale brzydko i do poprawy :(
def show_table(input_table):
    table = input_table
    for godziny in sesja.query(eval(table)).all():
        print(godziny.__dict__.values())


   
# def czytajdane():
    # for godziny in sesja.query(Hours).join(Student).join(Teacher).all():
        # print(godziny.value, godziny.date, godziny.student.first_name, godziny.teacher.first_name, godziny.teacher.last_name)

# problemy
def change_field():
    table = input("W jakiej tabeli chcesz dokonań zmian:")
    show_table(table)
    field_to_change = input("Jakie pole zmodyfikować:")
    zmiana = sesja.query(eval(table)).filter_by( = 1).one()
    zmiana.id_student = sesja.query(Student.id_student).filter_by(id_student = 2).scalar()



# print(type(Student.login))
change_field()
# sesja.close()
# login()













