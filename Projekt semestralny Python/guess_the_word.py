import random  #Importowanie modułu random do losowego wyboru słowa z listy
from words import words  #Importowanie listy słów z pliku words.py
from pictures import picture  #Importowanie X-ów obrazujących życia
import string 

#Funkcja losująca słowo z listy słów
def get_word(words):
    word = random.choice(words)
    return word.upper()

#Główna funkcja gry wisielec. Losuje słowo, pozwala zgadywać litery, wyświetla stan gry, liczbę żyć oraz użyte litery.
def guess_the_word():
    word = get_word(words)  #Losowanie słowa
    first_letter = word[0]  #Pierwsza litera słowa
    word_letters = set(word)  #Zbiór liter w słowie
    word_letters.remove(first_letter)  #Usunięcie pierwszej litery ze zbioru liter do odgadnięcia
    alphabet = set(string.ascii_uppercase)  #Zbiór liter alfabetu
    used = {first_letter}  #Zbiór użytych liter, zawierający pierwszą literę

    lives = 7 

    #Pętla gry, która trwa dopóki nie utracimy wszystkich żyć lub nie odganiemy hasła
    while len(word_letters) > 0 and lives > 0:
        print('Pozostało', lives, 'żyć')
        print('Użyte litery: ', ' '.join(used))

        #Wyświetlanie słowa z odgadniętymi literami
        word_list = [letter if letter in used else '-' for letter in word]
        print(picture[lives])
        print('Twoje słowo: ', ' '.join(word_list))

        #Pobieranie litery od użytkownika
        provided = input('Podaj litere: ').upper()
        if provided in alphabet - used:
            used.add(provided)  #Dodanie litery do zbioru użytych liter
            if provided in word_letters:
                word_letters.remove(provided)  #Usunięcie litery ze zbioru liter
                print('')
            else:
                lives -= 1  #Odjęcie życia jeśli litery nie ma w haśle
                print('\nPodana litera,', provided, 'nie jest zawarta w słowie.')

        elif provided in used:
            print('\nPróbowałes już tej litery!.')

        else:
            print('\nNiestety to niepoprawna litera.')

    #Informacja o zakończeniu gry
    if lives == 0:
        print(picture[lives])
        print('Niestety nie zgadłeś! Poprawne hasło to: ', word)
    else:
        print('Gratulacje! Odgadłeś hasło:', word, '!')

while True:
    guess_the_word()  #Rozpoczęcie gry

    #Pytamy użytkownika, czy chce zagrać raz jeszcze
    print("Czy chcesz zagrać raz jeszcze?: 1 - TAK    2 - NIE")
    onemore = input('Odpowiedź: ')
    if onemore != '1':
        print("Dzięki za grę i do następnego razu!")
        break
