 #                   TeoriaGrafow 

## Część analityczna
W pliku .pdf znajdują się rozwiązania zadań z tej części.

## Część programistyczna
W pliku Analiza algorytmu - Jakub Konieczny.docx zanjduje się omówienie metody Forda-Fulkersona 

W pliku main.py znajduje się zaimplementowany w języku Python algorytm. 

**Program używa blibliteki networkX oraz collections**

Aby program działał pliki .txt i main.py muszą być w tym samym folderze 

Pliki .txt mają format:
*  W pierwszej lini znajdują się wierzchołek początkowy oraz końcowy oddzielone spacją
   * źródło ujście
* Kolejne linie zależą od formatu pliku

  * Dla listy sąsiedztwa:

    * każda kolejna linia odpowiada kolenym wierzchołkom 

     * każda linia zawiera naprzemiennie ciąg liczb odpowiadacych wierzchołkowi końcowemu krawędzi oraz wadze również oddzielonych spacją 
     * Format lini:

       * wierzchołek_końcowy_krawędzi waga_krawędzi wierzchołek_końcowy_krawędzi waga_krawędzi ....

   * Dla listy krawędzi:

     * każda linia zawiera jedną krawędź w której dane oddzielone są spacją
     
     * Format lini:

       * wierzchołek_początkowy_krawedzi wierzchołek_końcowy_krawędzi waga_krawędzi


 * przykład listy sąsiedztwa:
``` 
1 4
2 2 3 5 4 6 3 4
1 6 2 5 4 2
1 8 2 4 4 1
1 3 2 7
```

  
  * Przykład listy krawędzi:

```1 5
1 2 3
1 3 4
4 2 6
5 2 2
2 3 5
3 5 7
1 4 6
2 3 2
```
  
  

  
