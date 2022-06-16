tablica = [                                                 #tablica sudoku 
            [0,0,0,0,0,0,6,0,9],
            [1,0,6,0,0,4,0,0,0],
            [0,0,5,3,0,6,8,2,1],
            [0,8,4,6,7,2,0,5,0],
            [0,5,7,0,0,0,9,0,0],
            [0,0,3,5,4,0,0,0,0],
            [3,7,0,4,0,5,2,0,6],
            [0,0,0,0,0,0,5,1,0],
            [0,6,0,0,2,0,0,3,7]
]


def znajdz_pusty(tab):                                      #funkcja która znajduje puste pole (0) i zwraca pozycje pola, aby je poprawić na prawidłową wartość 
    for x in range(len(tab)):                   
        for y in range(len(tab[0])):            
            if tab[x][y] == 0:                              #sprawdzamy czy pozycja wynosi 0 
                return (x,y)                                #wiersz, kolumna
    
    return None                                             #jeżeli nie ma kwadratów równych 0, żadne puste pola nie zwracają żadnego, co oznacza, że to wywoła znajdz   

def wyswietalnie(tab):                                      #funkcja która wyświetla tablice 2D w czytelny  sposób 
    for x in range(len(tab)):                               #zakres w jakim jesteśmy czyli oś x
        if x % 3 == 0 and x != 0:                           #dzelimy tablice na segmenty, % operator zwraca resztę z dzielenia, ! różnica 
            print("- - - - - - - - - - -")                  #dzielimy plansze na trzy segmenty 
        for y in range(len(tab[0])):
            if y % 3 == 0 and y != 0:                       #zakes w osi y, dzielimy tablice na segmenty co 3 znaki wyświetlamy ukośnik |    
                print("| ", end="")                         #end oznacza że nie drukujemy odwrotnego znaku, czyli nie przechodzimy do następnej linii 
            if y == 8:                                      #sprawdzamy czy jesteśmy na ostatniej pozycji, upewniamy się czy wykonał się ukośnik i wróciliśmy do następnej linii
                print(tab[x][y])
            else:
                print(str(tab[x][y]) + " ", end="")

def pozycja(tab, numer, pozycja):                           #funkcja która znajduje dana pozycje i tablica sprawdza czy jest to prawidłowe 
    for x in range(len(tab[0])):                            #sprawdzamy wiersz 
        if tab[pozycja[0]][x] == numer and pozycja[1] != x: #sprawdzamy każdą kolumnę, jeśli jest to pozycja 0 ignorujemy, ale jeśli nie jest to 0 to sprawdzamy czy nie powtórzyły się dwie takie same liczby w wierszu
            return False

    for x in range(len(tab)):                               #sprawdzamy kolumnę
        if tab[x][pozycja[1]] == numer and pozycja[0] != x: #przechodzimy pętlą przez każdy wiersz od 0 do 8, następnie sprawdzamy czy nasza obecna wartość x lub wartość kolumny jest równy tej samej liczbie, którą właśnie wstawiliśmy dla każdego wiersza i upewniamy się że nie jest to dokładna pozycja, która właśnie wstawiliśmy
            return False

    seg_x = pozycja[1] // 3                                 #sprawdzamy czy nasz segment 3 na 3 nie ma takich samych liczb
    seg_y = pozycja[0] // 3

    for y in range(seg_y * 3, seg_y * 3 + 3):               #dochodzimy do prawej strony tablicy 
        for x in range(seg_x * 3, seg_x * 3 + 3):
            if tab[y][x] == numer and (y,x) != pozycja:     #sprawdzamy czy jakikolwiek inny element w segmencie jest równy temu, który właśnie dodaliśmy i upewniamy się ze nie sprawdziliśmy tej samej pozycji, która właśnie dodaliśmy
                return False                                #jeśli to prawda to zwracamy fałsz, ponieważ zanleźliśmy duplikat

    return True                                             #zwaracamy prawdę jeśli wszystkie warunki zostały spełnione 

def rozwiązanie(tab):                                       #funkcja rozwiązująca sudoku w sposób rekurencyjny
    znajdz = znajdz_pusty(tab)
    if not znajdz:                                          #zwraca prawdę lub fałsz w zależności czy znaleźliśmy rozwiązanie 
        return True
    else:
        wiersz, kolumna = znajdz                            #w przeciwnym razie, wiersz kolumna równa się znajdz, następnie uruchomimy nasz algorytm bazowy przypadek rekurencji
    
    for x in range(1,10):                                   #sprawdź wartości od 1 do 10, upewniamy się że jeśli je dodamy do tablicy, byłoby to poprawne rozwiązanie
        if pozycja(tab, x, (wiersz, kolumna)):              #jeśli są prawidłowe dodajemy je do tablicy 
            tab[wiersz][kolumna] = x                        
            
            if rozwiązanie(tab):                            #jeśli dodamy wartość wywołujemy funkcje i będziemy próbować do skutku aż w końcu znajdziemy rozwiązanie, albo dojedziemy do punktu, w którym przeszliśmy przez różne liczby i żadna z nich nie jest poprawna 
                return True
            
            tab[wiersz][kolumna] = 0

    return False                                            #jeżli zwróci fałsz, oznacza to, że rozwiązanie nie będzie prawdziwe, wiec cofniemy się do ostatniego elementu aby sprawdzić poprawność i znowu wywołamy pętle z inna wartością


wyswietalnie(tablica)
rozwiązanie(tablica)
print("_____________________")
print(" ")
wyswietalnie(tablica)