class Word:

    # Atributos
    #--------------------------------------------------------------------------------------

    complete = bool
    word = str
    indexWord = []

    # Método Constructor
    #--------------------------------------------------------------------------------------
    def __init__(self, word):
        self.word = word
        self.complete = False
        self.registerIndexWords()


    # Métodos
    #--------------------------------------------------------------------------------------
    #registerIndexWords se crea una lista cuya longitud es igual a la cantidad de caracteres que tiene la palabra del vector words[] que ingresa como parámetro 
    def registerIndexWords(self):
        longA = len(self.word)
        for letter in self.word:
            self.indexWord.append(False)

    #recibe una letra por parámetro, si reconoce esta letra dentro de la palabra en juego, pone en su indice verdadero de modo que al pintar la palabra se vean los aciertos
    def mathLetter(self, sletter):
        counter = 0
        happend = False
        for letter in self.word:
            if letter == sletter:
                self.indexWord[counter] = True
                happend = True
            counter +=1
        self.isComplete()
        return happend
    
    # retorna la palabra del objeto, como visible o no visible
    def showWord(self):
        long = 0
        palabra = ""
        for wletter in self.word:
            if self.indexWord[long] == False:
                palabra = palabra + " _"
            else:
                palabra = palabra + wletter
            long +=1
        return palabra

    # informa si la palabra ya fue descubierta o no
    def isComplete(self):
        if self.word == self.showWord():
            self.complete = True
        else:
            self.complete = False
