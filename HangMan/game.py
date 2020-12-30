import random
from os import system
from word import Word
class Game:
    # Atributos
    #--------------------------------------------------------------------------------------

    onGame   = bool
    oportunities = int
    words = []
    selectedLetters = str

    # Método Constructor
    #--------------------------------------------------------------------------------------
    # inicializa el juego con la cantidad de intentos seleccionados por el usuario
    # Se lee el archivo txt donde se encuentran las palabras del juego y se incorporan a la lista words[] 
    def __init__(self, onGame, oportunities):
        self.onGame = onGame
        self.oportunities = oportunities
        self.selectedLetters = ""
        self.loadWords()
        self.orderRandom()
        self.get_beginGame()


    # Métodos
    #--------------------------------------------------------------------------------------
    # Lee el archivo de texto donde se encunetran registradas las palabras del juego y las incorpora a la lista words[]
    def loadWords(self):
        f = open("palabras/ListaPalabras.txt")
        for line in f.readlines():
            self.words.append(Word(line.replace("\n","")))
        f.close()

    # ordena al azar la lista words[], requiere la importación de la libreria random
    def orderRandom(self):
        random.shuffle(self.words)   


    #def inicia el juego
    def get_beginGame(self):
        tries = 0
        number = 0

        while self.onGame:
            self.get_paint(tries)
            print(self.words[number].showWord()) #aquí se debe elegir que palabra de la lista va
            if self.words[number].complete:
                self.get_paint(0)
                print("\n \n" + "FELICITACIONES HAS GANADO" + "\n \n")
                self.onGame = False
                break
            selectedLetter = input("\n \n" + self.words[number].word + " digita una letra: ")
            self.selectedLetters = self.selectedLetters + selectedLetter + " " 
            
            if self.words[number].mathLetter(selectedLetter) == False:
                tries +=1

            left = self.oportunities - tries
            if left == 0:
                self.get_paint(8)
                print("\n \n" + "HAS PERDIDO SIEMPRE TE RECORDAREMOS COMO EL PIBE QUE NO PUDO ADIVINAR, QUE LA FUERZA TE ACOMPAÑE" + "\n \n")
                self.onGame = False                


    #Pinta la horca, dependiendo de los intentos que lleve
    def get_paint(self, tries):
        system("cls")
        nameFile = "palabras/" + str(tries) + "HangMan.txt"
        f = open(nameFile,"r")
        texto = f.read()
        print(texto)
        f.close()
        print("\n \n" + self.selectedLetters + "\n \n")


# Método Main
#--------------------------------------------------------------------------------------

if __name__ == '__main__':
        
        system("cls")

        f = open("palabras/HangMan.txt","r")
        texto = f.read()
        print(texto)
        f.close()

        print("\n \nBienvenido al juego Hangman por favor elige una de las siguiente opciones \n")
        print("cantidad de oportunidades 4, 6, 8")
        
        oportunities = 0
        checked = False
        while checked == False:
            oportunities = input("elección: ")
            if oportunities == "4" or oportunities == "6" or oportunities == "8":
                print("\nHas elegido cantidad de " + str(oportunities) + " equivocaciones permitidas\n \n")
                oportunities = int(oportunities)
                checked = True
            else:
                print("\n debe seleccionar un numero de oportunidades valido, que puede ser 4, 6 o 8 \n")

        newGame = Game(True, oportunities)
