# -------------------------------------- Power Play 4 ---------------------------------- # 
# Applied Software 2024 - Project

    # Interface
    
from tkinter import *

    # Game class

class Can(Canvas):

    def __init__(self):
        
            #Variables
        
        self.cases      = [] # Boxes already filled
        self.listerouge = [] # List of red boxes
        self.listejaune = [] # List of yellow boxes
        self.dgagnantes = [] # Boxes already winning and therefore cannot be won again (see "Continue")
        self.running    = 1  # Current game type
        self.couleur    = ["Red", "Yellow"]
        self.color      = ["red", "#EDEF3A"]
        
            #Interface
        
        self.clair      = "light blue"
        self.fonce      = "navy blue"
        self.police1    = "Times 17 normal"
        self.police2    = "Arial 10 normal"
        self.police3    = "Times 15 bold"
        self.can        = Canvas.__init__(self, width =446, height = 430, bg=self.fonce, bd=0)
        
        self.grid(row = 1, columnspan = 5)

            # Current player
        
        self.joueur = 1
        self.create_rectangle(20,400,115,425,fill = self.clair)
        self.create_text(35, 405, text ="Player :", anchor = NW, fill = self.fonce, font= self.police2)
        self.indiccoul = self.create_oval(85, 405, 100, 420, fill = self.color[1])
        
            #New Game Button
        
        self.create_rectangle(330,400,420,425,fill=self.clair)
        self.create_text(340, 405, text ="New Game", anchor = NW, fill = self.fonce, font= self.police2)
        
            #Creation of boxes
        
        self.ovals = []
        for y in range(10, 390, 55):
            for x in range(10, 437, 63):
                self.ovals.append(self.create_oval(x, y, x + 50, y + 50 , fill= "white"))
                
            #In case of click
                
        self.bind("<Button-1>", self.click)
        
            # To connect the coordinates of the centers of the boxes to the end
        
        self.coordscentres = []
        
            # Accounting for sequences of parts
        
        self.rouges, self.jaunes = 0,0
        
            # Dictionnaire de reconnaissance
        
        self.dictionnaire = {}
        v = 0
        for y in range(10, 390, 55):
            for x in range(10, 437, 63):
                self.dictionnaire[(x, y, x + 50, y + 50)] = v
                v += 1
                self.coordscentres.append((x + 25, y + 25))

    def click(self,event): #In case of click
        if 330 < event.x and 400 < event.y and event.x < 420 and event.y < 425:
            self.new()# =>New Game
            
            #Game in progress: Recognition of the square played
            
        else :
            if self.running != 0:
                for (w, x, y, z) in self.dictionnaire:
                    if event.x > (w, x, y, z)[0] and event.y >(w, x, y, z)[1] and event.x < (w, x, y, z)[2] and event.y < (w, x, y, z)[3]:
                        self.colorier(self.dictionnaire[(w, x, y, z)]) # => Play

                
    def colorier(self, n, nb=0): #Manages the coloring of boxes
        
        if n in self.cases : return # A colored square can no longer change color
           
        if n + 7 not in self.cases and n + 7 < 49: #If the box below is empty and exists, we try to color that one first
            self.colorier(n+7)
            
        else:
            
                #Otherwise we color this one
            
            self.itemconfigure(self.ovals[n], fill = self.color[self.joueur])
            self.cases.append(n)
            self.color[self.joueur] == 'red' and self.listerouge.append(n) or self.listejaune.append(n)
            self.listejaune = [case for case in self.listejaune if case not in self.listerouge]
            self.verif(n)
            
                #Change of player
            
            self.joueur = [0,1][[0,1].index(self.joueur)-1]
            self.itemconfigure(self.indiccoul, fill = self.color[self.joueur])

                #We look at all the boxes are filled
            
            self.verificationFinale()        
        
        return

    
    def verif(self, n): # Checks if the added piece aligns with three others already placed
        
        if self.running == 0 : return
        
        if n in self.listerouge and n+7  in self.listerouge and n+14  in self.listerouge and n+21 in self.listerouge: # First vertically,
                                                                                            # separately because proximity to an edge is uninteresting
            liste=[n, n+7, n+14, n+21] # To manage “multi-winner” games
            if self.gagnantes(liste) : self.win("red", liste[0],liste[3])
            return
        
            #same for yellow
        
        if n in self.listejaune and n+7 in self.listejaune and n+14 in self.listejaune and n+21 in self.listejaune:
            liste=[n, n+7, n+14, n+21]
            if self.gagnantes(liste) : self.win("yellow", liste[0],liste[3])
            return
        
        for x in (1,-6,8):
            
            if n in self.listerouge: # ensuring that they are not too close to the edges (so as not to end up on the other side of the board)
                if n % 7 != 6 and n+x in self.listerouge:
                    if n % 7 != 5 and n+ 2*x in self.listerouge:
                        if n % 7 != 4 and n + 3*x in self.listerouge:
                            liste = [n, n+x, n+2*x, n+3*x]
                            if self.gagnantes(liste) : self.win("red", liste[0],liste[3])
                            return
                        if n%7 > 0 and (n-x) in self.listerouge:
                            liste = [n-x,n, n+x, n+2*x]
                            if self.gagnantes(liste) : self.win("red", liste[0],liste[3])
                            return
                    if n%7 > 1 and (n-x) in self.listerouge:
                        if n%7 > 2 and n-(2*x) in self.listerouge:
                            liste = [n-2*x, n-x,n, n+x]
                            if self.gagnantes(liste) : self.win("red", liste[0],liste[3])
                            return
                        
                #Same for the yellows
                        
            if n in self.listejaune:
                if n % 7 != 6 and n+x in self.listejaune:
                    if n % 7 != 5 and n+ 2*x in self.listejaune:
                        if n % 7 != 4 and n + 3*x in self.listejaune:
                            liste = [n, n+x, n+2*x, n+3*x]
                            if self.gagnantes(liste) : self.win("yellow", liste[0],liste[3])
                            return
                        if n%7 > 0 and (n-x) in self.listejaune:
                            liste = [n-x,n, n+x, n+2*x]
                            if self.gagnantes(liste) : self.win("yellow", liste[0],liste[3])
                            return
                    if n%7 > 1 and (n-x) in self.listejaune:
                        if n%7 > 2 and n-(2*x) in self.listejaune:
                            liste = [n-2*x, n-x,n, n+x]
                            if self.gagnantes(liste) : self.win("yellow", liste[0],liste[3])
                            return
                        
        
        for x in (-1,6,-8):
            
            if n in self.listejaune:
                if n % 7 != 0 and (n+x) in self.listejaune:
                    if n % 7 != 1 and n+(2*x) in self.listejaune:
                        if n % 7 != 2 and n + (3*x) in self.listejaune:
                            liste = [n, n+x, n+2*x, n+3*x]
                            if self.gagnantes(liste) : self.win("yellow", liste[0],liste[3])
                            return
                        if n%7 <6 and (n-x) in self.listejaune:
                            liste = [n-x,n, n+x, n+2*x]
                            if self.gagnantes(liste) : self.win("yellow", liste[0],liste[3])
                            return
                    if n%7 < 5 and (n-x) in self.listejaune:
                        if n%7 < 4 and n-(2*x) in self.listejaune:
                            liste = [n-2*x, n-x,n, n+x]
                            if self.gagnantes(liste) : self.win("yellow", liste[0],liste[3])
                            return
                        
            if n in self.listerouge:
                if n % 7 != 0 and (n+x) in self.listerouge:
                    if n % 7 != 1 and n+(2*x) in self.listerouge:
                        if n % 7 != 2 and n + (3*x) in self.listerouge:
                            liste = [n, n+x, n+2*x, n+3*x]
                            if self.gagnantes(liste) : self.win("red", liste[0],liste[3])
                            return
                        if n%7 <6 and (n-x) in self.listerouge:
                            liste = [n-x,n, n+x, n+2*x]
                            if self.gagnantes(liste) : self.win("red", liste[0],liste[3])
                            return
                    if n%7 < 5 and (n-x) in self.listerouge:
                        if n%7 < 4 and n-(2*x) in self.listerouge:
                            liste = [n-2*x, n-x,n, n+x]
                            if self.gagnantes(liste) : self.win("red", liste[0],liste[3])
                            return

    def verificationFinale(self): # When all boxes are filled
        
        if len(self.cases)==49: # We count the points
            typ =self.plus() # Type of game won
            if typ[1]==0:
                self.texte2 = Label(fen, text = "The " + typ[0] + " definitely won !", bg= self.fonce,
                                    fg=self.clair, font=self.police1)
                self.texte2.grid()
            elif typ[1]==1:
                self.texte2 = Label(fen, text = "The " + typ[0] + " were the first to win!", bg= self.fonce,
                                    fg=self.clair, font=self.police1)
                self.texte2.grid()
            else:
                self.texte2 = Label(fen, text = typ[0], bg= self.fonce, fg=self.clair, font=self.police1)
                self.texte2.grid(padx=110)

                
    def win(self, qui, p, d): # Game won
        
            #Marking the winning pieces
        
        self.create_line(self.coordscentres[p][0], self.coordscentres[p][1],
                         self.coordscentres[d][0], self.coordscentres[d][1],
                         fill="blue")

        if qui=="red" : self.rouges += 1 #Accounting for consequences
        if qui=="yellow" : self.jaunes += 1

        if self.running == 3:
            self.pRouges.config(text = "Reds : " + str(self.rouges))
            self.pJaunes.config(text = "Yellows : " + str(self.jaunes))
            return

            #Score display
        
        self.qui = qui
        self.texte = Label(fen, text="%s won !" % (qui), bg= self.fonce, fg=self.clair, font=self.police1)
        self.texte.grid()
        self.running = 0
        
            #Proposal to continue
        
        self.BtnContinuer = Button(fen, text=" Continue this game", bd= 0, bg=self.fonce, fg=self.clair,
                                   font=self.police3, command=self.continuer)
        self.BtnContinuer.grid(padx=120)

        
    def continuer(self): # If we choose to continue the same game (already won by a player)
        
        self.running = 3
        
            # Score display
            
        self.pRouges = Label(fen, text = "Red : %s" %(str(self.rouges)),
                             font=self.police3, bg=self.fonce, fg=self.clair)
        self.pJaunes = Label(fen, text = "Yellow : %s" %( str(self.jaunes)),
                             font=self.police3, bg=self.fonce, fg=self.clair)

        self.BtnContinuer.destroy()
        self.texte.destroy()
        self.pRouges.grid(padx=160)
        self.pJaunes.grid(padx=160)

        
    def gagnantes(self, liste=[]): # We check that the pieces are not yet winners, and we add them to the list if they become so.

        for i in liste:
            if i in self.dgagnantes: return 0
        
        for n in liste:
            self.dgagnantes.append(n)
            
        return 1

    
    def plus(self): # Give the final result
        
        if self.rouges > self.jaunes    : return "Red",0
        if self.jaunes > self.rouges    : return "Yellow",0
        if self.rouges != 0             : return self.qui, 1 # In case of a tie, the first to line up their pieces wins

        return "Nobody won", 2 #Otherwise, both lost

    def new(self):# New Game
        
            # Uncertain operations
        
        try:
            self.BtnContinuer.destroy()
        except:
            pass
        try:
            self.texte.destroy()
        except:
            pass
        try:
            self.texte2.destroy()
        except:
            pass
        try:
            self.pRouges.destroy()
        except:	
            pass
        try:
            self.pJaunes.destroy()
        except:
            pass
            
            # Operations that are
            
        self.destroy()
        self.__init__()

	
if __name__ ==	"__main__" :
    fen = Tk()
    fen.title("Power 4")
    fen.config(bg="navy blue")
    lecan = Can()
    fen.mainloop()