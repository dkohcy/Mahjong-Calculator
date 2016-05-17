from Tkinter import *

class mahjong():
    
    global Action1, Action2
    
    def __init__(self, top):
        
        
        ####### input on first canvas ##########
        '''
        self.c1 = Canvas(top, width = 400, height = 500, bg = 'white')
        self.c1.grid(column = 0, row = 0)
        '''
        
        self.p1 = Label(top, text = "Player 1")
        self.p1.grid(column = 0, row = 0)
        
        self.p2 = Label(top, text = 'Player 2')
        self.p2.grid(column = 0, row = 1)
        
        self.p3 = Label(top, text = 'Player 3')
        self.p3.grid(column = 0, row = 2)
        
        self.p4 = Label(top, text = 'Player 4')
        self.p4.grid(column = 0, row = 3)
        
        self.double = Label(top, text = 'Point:', width = 12)
        self.double.grid(column = 2, row = 0)
    
        self.s1 = StringVar()
        self.s2 = StringVar()
        self.s3 = StringVar()
        self.s4 = StringVar()
        self.sdouble = int(10)
        
        self.p1e = Entry(top, textvariable = self.s1, justify = LEFT)
        self.p1e.grid(column = 1, row = 0)
        
        self.p2e = Entry(top, textvariable = self.s2, justify = LEFT)
        self.p2e.grid(column = 1, row = 1)
        
        self.p3e = Entry(top, textvariable = self.s3, justify = LEFT)
        self.p3e.grid(column = 1, row = 2)
        
        self.p4e = Entry(top, textvariable = self.s4, justify = LEFT)
        self.p4e.grid(column = 1, row = 3)
        
        self.Double = Entry(top, textvariable = '', justify = RIGHT, width = 5)
        self.Double.grid(column = 3, row = 0)
        
        self.b1 = Button(top, text = 'Enter', command = self.canvas2)
        self.b1.grid(column = 0, row = 4)
        
        
        
        ### line in between the canvas ###
        #self.c = Canvas(top, width = 60, height = 100, bg = 'red')
        #self.c.grid(column = 2, row = 0, rowspan = 50)
           
    def canvas2(self):
        
        global Action1, Action2
        
        self.dList = []
        
        
        self.spacing = Label(top, text = '', width = 5)
        self.spacing.grid(column = 4, row = 0)
        
        self.p12 = Label(top, text = self.s1.get(), width = 10)
        self.p12.grid(column = 5, row = 0)
        
        self.p22 = Label(top, text = self.s2.get(), width = 10)
        self.p22.grid(column = 6, row = 0)
        
        self.p32 = Label(top, text = self.s3.get(), width = 10)
        self.p32.grid(column = 7, row = 0)
        
        self.p42 = Label(top, text = self.s4.get(), width = 10)
        self.p42.grid(column = 8, row = 0)
        
        for i in range(10):
            self.dList.append(self.sdouble)
            self.sdouble = self.sdouble * 2 
            
        self.sdouble = int(10)
        print self.dList
        
        
        #### Winner List ######
        self.winner = Label(top, text = 'Winner:')
        self.winner.grid(column = 0, row = 5)
        
        Action1 = IntVar()
        
        self.p1 = Radiobutton(top, text = self.s1.get(), variable = Action1, value = 1, justify = LEFT, width = 15)
        self.p1.grid(column = 0, row = 6, columnspan = 2)
        
        self.p2 = Radiobutton(top, text = self.s2.get(), variable = Action1, value = 2, justify = LEFT, width = 15)
        self.p2.grid(column = 0, row = 7, columnspan = 2)
        
        self.p3 = Radiobutton(top, text = self.s3.get(), variable = Action1, value = 3, justify = LEFT, width = 15)
        self.p3.grid(column = 0, row = 8, columnspan = 2)
        
        self.p4 = Radiobutton(top, text = self.s4.get(), variable = Action1, value = 4, justify = LEFT, width = 15)
        self.p4.grid(column = 0, row = 9, columnspan = 2)
        
        
        ###### Loser List #####
        self.giver = Label(top, text = 'Who gave?')
        self.giver.grid(column = 0, row = 10)
        
        Action2 = IntVar()
        
        self.p1 = Radiobutton(top, text = self.s1.get(), variable = Action2, value = 1, justify = LEFT, width = 15)
        self.p1.grid(column = 0, row = 11, columnspan = 2)
        
        self.p2 = Radiobutton(top, text = self.s2.get(), variable = Action2, value = 2, justify = LEFT, width = 15)
        self.p2.grid(column = 0, row = 12, columnspan = 2)
        
        self.p3 = Radiobutton(top, text = self.s3.get(), variable = Action2, value = 3, justify = LEFT, width = 15)
        self.p3.grid(column = 0, row = 13, columnspan = 2)
        
        self.p4 = Radiobutton(top, text = self.s4.get(), variable = Action2, value = 4, justify = LEFT, width = 15)
        self.p4.grid(column = 0, row = 14, columnspan = 2)
        
        ####### How many doubles ######
        self.doubles = Label(top, text = '# of Doubles')
        self.doubles.grid(column = 2, row = 5)
        
        self.intdoubles = IntVar()
        
        self.Edoubles = Entry(top, textvariable = self.intdoubles, justify = LEFT, width = 5)
        self.Edoubles.grid(column = 3, row = 5)
        
        ### submit score ###
        self.b2 = Button(top, text = 'Submit', command = self.score)
        self.b2.grid(column = 3, row = 6)
        
        
        
        
    def score(self):
        global Action1, Action2
                
        if self.intdoubles.get() == 1:
            if Action1.get() == 1:
                if Action2.get() == 2:
                    self.loser = Label(top, text = int( 0-self.dList[ self.intdoubles.get() ]))
                    self.loser.grid(column = Action2.get() + 4, row = 1)
                    
                    self.winner = Label(top, text = int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) ))
                    self.winner.grid(column = Action1.get() + 4, row = 1)
                    
                    self.rest1 = Label(top, text = int(0 - self.dList[self.intdoubles.get() - 1]))
                    self.rest1.grid(column = Action2.get() + 5, row = 1)
                    
                    self.rest2 = Label(top, text = int(0 - self.dList[self.intdoubles.get() - 1]))
                    self.rest2.grid(column = Action2.get() + 6, row = 1)
            
                elif Action2.get() == 3:
                    self.loser = Label(top, text = int( 0-self.dList[ self.intdoubles.get() ]))
                    self.loser.grid(column = Action2.get() + 4, row = 1)
                    
                    self.winner = Label(top, text = int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) ))
                    self.winner.grid(column = Action1.get() + 4, row = 1)
                    
                    self.rest1 = Label(top, text = int(0 - self.dList[self.intdoubles.get() - 1]))
                    self.rest1.grid(column = Action2.get() + 5, row = 1)
                    
                    self.rest2 = Label(top, text = int(0 - self.dList[self.intdoubles.get() - 1]))
                    self.rest2.grid(column = Action2.get() + 3, row = 1)
                
                elif Action2.get() == 4:
                    self.loser = Label(top, text = int( 0-self.dList[ self.intdoubles.get() ]))
                    self.loser.grid(column = Action2.get() + 4, row = 1)
                    
                    self.winner = Label(top, text = int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) ))
                    self.winner.grid(column = Action1.get() + 4, row = 1)
                    
                    self.rest1 = Label(top, text = int(0 - self.dList[self.intdoubles.get() - 1]))
                    self.rest1.grid(column = Action2.get() + 2, row = 1)
                    
                    self.rest2 = Label(top, text = int(0 - self.dList[self.intdoubles.get() - 1]))
                    self.rest2.grid(column = Action2.get() + 3, row = 1)
                    
            elif Action1.get() == 2:
                if Action2.get() == 1
            
        pass
        
    

        
        
        
        
        
top = Tk()
top.title('Mahjong')

myGui = mahjong(top)

top.mainloop()
            