import mysql.connector


mydb = mysql.connector.connect( #funkcja dzięki której łączymy się z bazą danych
  host      ="localhost",
  user      ="root",
  password  ="root",
  database  ="codemon_studia"
)

znak = '0'

while(znak != 'x'):
  print("Co chcesz zrobic z baza? ")
  print("Wyswietlic ilosc wypozyczonych ksiazek - wi")
  print("Wyswietlic wypozyczone ksiazki - ww")
  print("Dodac ksiazke do biblioteki - dk")
  print("Dodac uzytkownika biblioteki - du")
  print("Usunac ksiazke - uk")
  print("Usunac uzytkownika - uu")
  print("Wypozyczyc ksiazke - wk")
  znak = input(': ')

  mycursor = mydb.cursor()

#---------------WYŚWIETLANIE ILOSCI WYPOZYCZONYCH KSIAZEK--------------------------
  if znak == 'wi':      
    zapytanie = "SELECT * FROM ilosc_wypozyczonych;"

    mycursor.execute(zapytanie)

    myresult  = mycursor.fetchall()

    for x in myresult:
      print(x)

#---------------WYŚWIETLANIE WYPOZYCZONYCH KSIAZEK--------------------------
  if znak == 'ww':      
    zapytanie = "SELECT * FROM wypozyczone_ksiazki;"

    mycursor.execute(zapytanie)

    myresult  = mycursor.fetchall()

    for x in myresult:
      print(x)
  

#---------------DODAWANIE KSIAZKI--------------------------
  elif znak == 'dk':
    zapytanie     = "call nowa_ksiazka(%s,%s,%s)"
    tytul         = input('Tytul: ')
    autor         = input('Autor: ')
    ilosc         = input('Ilosc: ')

    dane    = (tytul,autor,ilosc)

    mycursor.execute(zapytanie,dane)

    a = input("Czy chcesz dokonać zmian? Tak-t, Nie-n ")

    if a == 't':
      mydb.commit()
    else:
      mydb.rollback()

#---------------DODAWANIE UZYTKOWNIKA--------------------------
  elif znak == 'du':
    zapytanie     = "call nowy_uzytkownik(%s,%s)"
    nazwisko      = input('Nazwisko: ')
    imie          = input('Imie: ')

    dane    = (nazwisko,imie)

    mycursor.execute(zapytanie,dane)

    a = input("Czy chcesz dokonać zmian? Tak-t, Nie-n ")

    if a == 't':
      mydb.commit()
    else:
      mydb.rollback()

 #---------------USUWANIE KSIAZKI-------------------------- 
  elif znak == 'uk':
    zapytanie     = "call usun_ksiazke(%s)"
    tytul         = input('Tytul: ')

    mycursor.execute(zapytanie,tytul)

    a = input("Czy chcesz dokonać zmian? Tak-t, Nie-n ")

    if a == 't':
      mydb.commit()
    else:
      mydb.rollback()

 #---------------USUWANIE UZYTKOWNIKA-------------------------- 
  elif znak == 'uu':
    zapytanie     = "call usun_uzytkownika(%s,%s)"
    nazwisko      = input('Nazwisko: ')
    imie          = input('Imie: ')

    dane = (nazwisko,imie)

    mycursor.execute(zapytanie,dane)

    a = input("Czy chcesz dokonać zmian? Tak-t, Nie-n ")

    if a == 't':
      mydb.commit()
    else:
      mydb.rollback()

 #---------------WYPOZYCZANIE KSIAZKI-------------------------- 
  elif znak == 'wk':
    zapytanie     = "call usun_wypozycz(%s,%s)"
    id_ksiazki    = input('ID Ksiazki: ')
    id_osoby      = input('ID Osoby: ')

    dane = (id_ksiazki,id_osoby)

    mycursor.execute(zapytanie,dane)

    a = input("Czy chcesz dokonać zmian? Tak-t, Nie-n ")

    if a == 't':
      mydb.commit()
    else:
      mydb.rollback()
  
  sprawdzenie = input("Czy chcesz wyjsc z programu? t/n: ")
  if sprawdzenie == 't':
        znak = 'x'
   



    