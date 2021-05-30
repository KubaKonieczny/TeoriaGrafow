 #                   TeoriaGrafow 

## Część analityczna
W pliku .pdf znajdują się rozwiązania zadań z tej części.

## Część programistyczna
W pliku Analiza algorytmu - Jakub Konieczny.docx zanjdują się omówienie metody Forda-Fulkersona 

W pliku main.py znajduje się zaimplementowany w języku Python algorytm. 

**Program używa blibliteki networkX oraz collections**

Aby program działał pliki .txt i main.py muszą być w tym samym folderze 

Pliki .txt mają format:
*  W pierwszej lini znajdują się wierzchołek początkowy oraz końcowy oddzielone spacją
   * źródło ujście
* Kolejne linie zależą od formatu pliku

  * Dla listy sąsiedztwa:

    * każada kolejna linia odpwoiada kolenym wierzchołkom 

     * każada linia zawiera naprzemiennie ciąg liczb odpowiadacych wierzcchołkowi końcowem oraz wadze również odzelonych spacją 
     * Format lini:

       * wierzchołek_końcowy_krawędzi waga_krawędzi wierzchokłek_końcowy_krawędzi waga_krawędzi ....

   * Dla listy krawędzi:

     * każda linia zawiera jedną krawędź w której dane odzielone są spacją
     
     * Format lini:

       * wierzchołek_początkowy_krawedzi wierzchołek_końcowy_krawędzi waga_krawędzi

  
