from Tkinter import *


v = 1
u = 1
p1List = []
p2List = []
p3List = []
p4List = []
dic = {}
scoreList = []

class mahjong():

	def __init__(self, top):

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
		self.sdouble = IntVar()
		
		
		self.p1e = Entry(top, textvariable = self.s1, justify = LEFT)
		self.p1e.grid(column = 1, row = 0)
		
		self.p2e = Entry(top, textvariable = self.s2, justify = LEFT)
		self.p2e.grid(column = 1, row = 1)
		
		self.p3e = Entry(top, textvariable = self.s3, justify = LEFT)
		self.p3e.grid(column = 1, row = 2)
		
		self.p4e = Entry(top, textvariable = self.s4, justify = LEFT)
		self.p4e.grid(column = 1, row = 3)
		
		self.Double = Entry(top, textvariable = self.sdouble, justify = LEFT, width = 5)
		self.Double.grid(column = 3, row = 0)
		
		self.b1 = Button(top, text = 'Enter', command = self.canvas2)
		self.b1.grid(column = 0, row = 4)

		self.initials = Label(top, text = 'Please enter initials only', font = ('Helvetiva',10,'italic'), fg = 'red')
		self.initials.grid(column = 1, row = 4)

		self.pointscomment = Label(top, text = 'eg.[10,20,40,...] input 10 \n eg.[20,40,80,...] input 20', font = ('Helvetica',10,'italic'), fg = 'red')
		self.pointscomment.grid(column = 2, row = 1, columnspan = 2)

	def canvas2(self):
	    
	    global Action1, Action2, v, Action3


	    self.covercenter = Label(top, text = '', width = 15)
	    self.covercenter.grid(column = 0, row = 4)
	    
	    self.dList = []
	    sdouble = self.sdouble.get()
	    
	    #self.spacing = Label(top, text = '', width = 5)
	    #self.spacing.grid(column = 4, row = 0)
	
	    self.p12 = Label(top, text = self.s1.get(), width = 10)
	    self.p12.grid(column = 5, row = 0)
	    
	    self.p22 = Label(top, text = self.s2.get(), width = 10)
	    self.p22.grid(column = 6, row = 0)
	    
	    self.p32 = Label(top, text = self.s3.get(), width = 10)
	    self.p32.grid(column = 7, row = 0)
	    
	    self.p42 = Label(top, text = self.s4.get(), width = 10)
	    self.p42.grid(column = 8, row = 0)

	    ### second list ###
	    self.p13 = Label(top, text = self.s1.get(), width = 10)
	    self.p13.grid(column = 9, row = 0)
	    
	    self.p23 = Label(top, text = self.s2.get(), width = 10)
	    self.p23.grid(column = 10, row = 0)
	    
	    self.p33 = Label(top, text = self.s3.get(), width = 10)
	    self.p33.grid(column = 11, row = 0)
	    
	    self.p43 = Label(top, text = self.s4.get(), width = 10)
	    self.p43.grid(column = 12, row = 0)


	    ### calculation for the list of doubles ####
	    for i in range(20):
	        self.dList.append(sdouble)
	        sdouble = sdouble * 2 
	        
	    
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
	    
	    
	    ###### Loser List & Zhi Mo & pingwu #####
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

	    self.zimo = Radiobutton(top, text = 'Zi Mo', variable = Action2, value = 5, justify = LEFT, width = 15)
	    self.zimo.grid(column = 0, row = 15, columnspan = 2)

	    ####### How many doubles ######
	    self.doubles = Label(top, text = '# of Doubles')
	    self.doubles.grid(column = 2, row = 5)

	    self.maxdoubles = Label(top, text = 'max doubles = 19', font = ('Helvetica',10,'italic'), fg = 'red')
	    self.maxdoubles.grid(column = 2, row = 6, columnspan = 2)
	    
	    self.intdoubles = IntVar()

	    self.Edoubles = Entry(top, textvariable = self.intdoubles, justify = LEFT, width = 5)
	    self.Edoubles.grid(column = 3, row = 5)
	    

	    #### scores for flowers #####
	    self.flowers = Label(top, text = 'Flower scores')
	    self.flowers.grid(column = 0, row = 16)

	    self.catmouse = Radiobutton(top, text = 'Cat & Mouse', variable = Action2, value = 6, justify = LEFT, width = 15)
	    self.catmouse.grid(column = 0, row = 17, columnspan = 2)

	    self.chickencentipede = Radiobutton(top, text = 'Chicken \nCentipede', variable = Action2, value = 7, justify = LEFT, width = 15)
	    self.chickencentipede.grid(column = 0, row = 18, columnspan = 2)

	    self.fournumbers = Radiobutton(top, text = 'Complete \nFlowers', variable = Action2, value = 8, justify = LEFT, width = 15)
	    self.fournumbers.grid(column = 0, row = 19, columnspan = 2)

	    self.gongpong = Radiobutton(top, text = 'Gong (pong)', variable = Action2, value = 9 , justify = LEFT, width = 15)
	    self.gongpong.grid(column = 0, row = 20, columnspan = 2)

	    self.gongself = Radiobutton(top, text = 'Gong (self)', variable = Action2, value = 10, justify = LEFT, width = 15)
	    self.gongself.grid(column = 0, row = 21, columnspan = 2)

	    ##### Ping Hu no flowers ######
	    self.oddDoubles = Label(top, text = 'Odd Doubles')
	    self.oddDoubles.grid(column = 0 , row = 22)

	    Action3 = IntVar()
	    self.pinghu = Checkbutton(top, text = 'Ping Hu', variable = Action3, onvalue = 1, offvalue = 0, justify = LEFT, width = 15) ###### in between 3&4 doubles #####
	    self.pinghu.grid(column = 0, row = 23, columnspan = 2)

	    ### submit score button ###
	    self.b2 = Button(top, text = 'Submit', command = self.score)
	    self.b2.grid(column = 3, row = 7)

	    #### finish button#####
	    self.finish = Button(top, text = 'Finish', command = self.finish)
	    self.finish.grid(column = 3, row = 13)

	    ##### delete button #####
	    self.delete = Button(top, text = 'Delete', command = self.delete)
	    self.delete.grid(column = 3, row = 10)

	    ### extra lines/spaces ###
	    self.extra1 = Label(top, text = '')
	    self.extra1.grid(column = 0, row = 24)

	    self.extra2 = Label(top, text = '')
	    self.extra2.grid(column = 0, row = 25)

	    self.extra3 = Label(top, text = '')
	    self.extra3.grid(column = 0, row = 26)

	    self.extra4 = Label(top, text = '')
	    self.extra4.grid(column = 0, row = 27)

	    self.extra5 = Label(top, text = '')
	    self.extra5.grid(column = 0, row = 28)

	def score(self):

		#####scores for flowers#####
		if Action1.get() == 1:
			if Action2.get() == 6:
				self.p1 = int( self.dList[0]* 3 )
				self.p2 = int( 0 - self.dList[0] )
				self.p3 = int( 0 - self.dList[0] )
				self.p4 = int( 0 - self.dList[0] )

				p1List.append( int( self.dList[0]* 3 ))
				p2List.append( int( 0 - self.dList[0] ))
				p3List.append( int( 0 - self.dList[0] )) 
				p4List.append( int( 0 - self.dList[0] ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

			elif Action2.get() == 7:
				self.p1 = int( self.dList[0]* 3 )
				self.p2 = int( 0 - self.dList[0] )
				self.p3 = int( 0 - self.dList[0] )
				self.p4 = int( 0 - self.dList[0] )

				p1List.append( int( self.dList[0]* 3 ))
				p2List.append( int( 0 - self.dList[0] ))
				p3List.append( int( 0 - self.dList[0] )) 
				p4List.append( int( 0 - self.dList[0] ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

			elif Action2.get() == 8:
				self.p1 = int( self.dList[0]* 3 )
				self.p2 = int( 0 - self.dList[0] )
				self.p3 = int( 0 - self.dList[0] )
				self.p4 = int( 0 - self.dList[0] )

				p1List.append( int( self.dList[0]* 3 ))
				p2List.append( int( 0 - self.dList[0] ))
				p3List.append( int( 0 - self.dList[0] )) 
				p4List.append( int( 0 - self.dList[0] ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

			elif Action2.get() == 9:
				self.p1 = int( self.dList[0]* 3 )
				self.p2 = int( 0 - self.dList[0] )
				self.p3 = int( 0 - self.dList[0] )
				self.p4 = int( 0 - self.dList[0] )

				p1List.append( int( self.dList[0]* 3 ))
				p2List.append( int( 0 - self.dList[0] ))
				p3List.append( int( 0 - self.dList[0] )) 
				p4List.append( int( 0 - self.dList[0] ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

			elif Action2.get() == 10:
				self.p1 = int( self.dList[1]* 3 )
				self.p2 = int( 0 - self.dList[1] )
				self.p3 = int( 0 - self.dList[1] )
				self.p4 = int( 0 - self.dList[1] )

				p1List.append( int( self.dList[1]* 3 ))
				p2List.append( int( 0 - self.dList[1] ))
				p3List.append( int( 0 - self.dList[1] )) 
				p4List.append( int( 0 - self.dList[1] ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

		if Action1.get() == 2:
			if Action2.get() == 6:
				self.p1 = int( 0 - self.dList[0] )
				self.p2 = int( self.dList[0]* 3 )
				self.p3 = int( 0 - self.dList[0] )
				self.p4 = int( 0 - self.dList[0] )

				p1List.append( int( 0 - self.dList[0] ))
				p2List.append( int( self.dList[0]* 3 ))
				p3List.append( int( 0 - self.dList[0] )) 
				p4List.append( int( 0 - self.dList[0] ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

			elif Action2.get() == 7:
				self.p1 = int( 0 - self.dList[0] )
				self.p2 = int( self.dList[0]* 3 )
				self.p3 = int( 0 - self.dList[0] )
				self.p4 = int( 0 - self.dList[0] )

				p1List.append( int( 0 - self.dList[0] ))
				p2List.append( int( self.dList[0]* 3 ))
				p3List.append( int( 0 - self.dList[0] )) 
				p4List.append( int( 0 - self.dList[0] ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

			elif Action2.get() == 8:
				self.p1 = int( 0 - self.dList[0] )
				self.p2 = int( self.dList[0]* 3 )
				self.p3 = int( 0 - self.dList[0] )
				self.p4 = int( 0 - self.dList[0] )

				p1List.append( int( 0 - self.dList[0] ))
				p2List.append( int( self.dList[0]* 3 ))
				p3List.append( int( 0 - self.dList[0] )) 
				p4List.append( int( 0 - self.dList[0] ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

			elif Action2.get() == 9:
				self.p1 = int( 0 - self.dList[0] )
				self.p2 = int( self.dList[0]* 3 )
				self.p3 = int( 0 - self.dList[0] )
				self.p4 = int( 0 - self.dList[0] )

				p1List.append( int( 0 - self.dList[0] ))
				p2List.append( int( self.dList[0]* 3 ))
				p3List.append( int( 0 - self.dList[0] )) 
				p4List.append( int( 0 - self.dList[0] ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

			elif Action2.get() == 10:
				self.p1 = int( 0 - self.dList[1] )
				self.p2 = int( self.dList[1]* 3 )
				self.p3 = int( 0 - self.dList[1] )
				self.p4 = int( 0 - self.dList[1] )

				p1List.append( int( 0 - self.dList[1] ))
				p2List.append( int( self.dList[1]* 3 ))
				p3List.append( int( 0 - self.dList[1] )) 
				p4List.append( int( 0 - self.dList[1] ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

		if Action1.get() == 3:
			if Action2.get() == 6:
				self.p1 = int( 0 - self.dList[0] )
				self.p2 = int( 0 - self.dList[0] )
				self.p3 = int( self.dList[0]* 3 )
				self.p4 = int( 0 - self.dList[0] )

				p1List.append( int( 0 - self.dList[0] ))
				p2List.append( int( 0 - self.dList[0] ))
				p3List.append( int( self.dList[0]* 3 )) 
				p4List.append( int( 0 - self.dList[0] ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

			elif Action2.get() == 7:
				self.p1 = int( 0 - self.dList[0] )
				self.p2 = int( 0 - self.dList[0] )
				self.p3 = int( self.dList[0]* 3 )
				self.p4 = int( 0 - self.dList[0] )

				p1List.append( int( 0 - self.dList[0] ))
				p2List.append( int( 0 - self.dList[0] ))
				p3List.append( int( self.dList[0]* 3 )) 
				p4List.append( int( 0 - self.dList[0] ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

			elif Action2.get() == 8:
				self.p1 = int( 0 - self.dList[0] )
				self.p2 = int( 0 - self.dList[0] )
				self.p3 = int( self.dList[0]* 3 )
				self.p4 = int( 0 - self.dList[0] )

				p1List.append( int( 0 - self.dList[0] ))
				p2List.append( int( 0 - self.dList[0] ))
				p3List.append( int( self.dList[0]* 3 )) 
				p4List.append( int( 0 - self.dList[0] ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

			elif Action2.get() == 9:
				self.p1 = int( 0 - self.dList[0] )
				self.p2 = int( 0 - self.dList[0] )
				self.p3 = int( self.dList[0]* 3 )
				self.p4 = int( 0 - self.dList[0] )

				p1List.append( int( 0 - self.dList[0] ))
				p2List.append( int( 0 - self.dList[0] ))
				p3List.append( int( self.dList[0]* 3 )) 
				p4List.append( int( 0 - self.dList[0] ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

			elif Action2.get() == 10:
				self.p1 = int( 0 - self.dList[1] )
				self.p2 = int( 0 - self.dList[1] )
				self.p3 = int( self.dList[1]* 3 )
				self.p4 = int( 0 - self.dList[1] )

				p1List.append( int( 0 - self.dList[1] ))
				p2List.append( int( 0 - self.dList[1] ))
				p3List.append( int( self.dList[1]* 3 )) 
				p4List.append( int( 0 - self.dList[1] ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

		if Action1.get() == 4:
			if Action2.get() == 6:
				self.p1 = int( 0 - self.dList[0] )
				self.p2 = int( 0 - self.dList[0] )
				self.p3 = int( 0 - self.dList[0] )
				self.p4 = int( self.dList[0]* 3 )

				p1List.append( int( 0 - self.dList[0] ))
				p2List.append( int( 0 - self.dList[0] ))
				p3List.append( int( 0 - self.dList[0] )) 
				p4List.append( int( self.dList[0]* 3 ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

			elif Action2.get() == 7:
				self.p1 = int( 0 - self.dList[0] )
				self.p2 = int( 0 - self.dList[0] )
				self.p3 = int( 0 - self.dList[0] )
				self.p4 = int( self.dList[0]* 3 )

				p1List.append( int( 0 - self.dList[0] ))
				p2List.append( int( 0 - self.dList[0] ))
				p3List.append( int( 0 - self.dList[0] )) 
				p4List.append( int( self.dList[0]* 3 ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

			elif Action2.get() == 8:
				self.p1 = int( 0 - self.dList[0] )
				self.p2 = int( 0 - self.dList[0] )
				self.p3 = int( 0 - self.dList[0] )
				self.p4 = int( self.dList[0]* 3 )

				p1List.append( int( 0 - self.dList[0] ))
				p2List.append( int( 0 - self.dList[0] ))
				p3List.append( int( 0 - self.dList[0] )) 
				p4List.append( int( self.dList[0]* 3 ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

			elif Action2.get() == 9:
				self.p1 = int( 0 - self.dList[0] )
				self.p2 = int( 0 - self.dList[0] )
				self.p3 = int( 0 - self.dList[0] )
				self.p4 = int( self.dList[0]* 3 )

				p1List.append( int( 0 - self.dList[0] ))
				p2List.append( int( 0 - self.dList[0] ))
				p3List.append( int( 0 - self.dList[0] )) 
				p4List.append( int( self.dList[0]* 3 ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)

			elif Action2.get() == 10:
				self.p1 = int( 0 - self.dList[1] )
				self.p2 = int( 0 - self.dList[1] )
				self.p3 = int( 0 - self.dList[1] )
				self.p4 = int( self.dList[1]* 3 )

				p1List.append( int( 0 - self.dList[1] ))
				p2List.append( int( 0 - self.dList[1] ))
				p3List.append( int( 0 - self.dList[1] )) 
				p4List.append( int( self.dList[1]* 3 ))

				self.printscore(self.p1, self.p2, self.p3, self.p4)




		#####scores for doubles#####
		for i in range(1,20):

			if self.intdoubles.get() == i:

				if Action1.get() == 1:
					if Action2.get() == 2:
						if Action3.get() == 0:
							self.p1 = int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) )
							self.p2 = int( 0 - self.dList[self.intdoubles.get()] )
							self.p3 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p4 = int( 0 - self.dList[self.intdoubles.get() - 1] )

							p1List.append( int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) ))
							p2List.append( int( 0 - self.dList[self.intdoubles.get()] ))
							p3List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p4List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

						else:					
							self.p1 = int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) )
							self.p2 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p3 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p4 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )

							p1List.append(int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) ))
							p2List.append(int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p3List.append(int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p4List.append(int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

					elif Action2.get() == 3:
						if Action3.get() == 0:
							self.p1 = int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) )
							self.p2 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p3 = int( 0 - self.dList[self.intdoubles.get()] )
							self.p4 = int( 0 - self.dList[self.intdoubles.get() - 1] )

							p1List.append( int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) ))
							p2List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p3List.append( int( 0 - self.dList[self.intdoubles.get()] ))
							p4List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

						else:
							self.p1 = int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) )
							self.p2 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p3 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p4 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )

							p1List.append(int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) ))
							p2List.append(int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p3List.append(int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p4List.append(int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

					elif Action2.get() == 4:
						if Action3.get() == 0:
							self.p1 = int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) )
							self.p2 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p3 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p4 = int( 0 - self.dList[self.intdoubles.get()] )

							p1List.append( int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) ))
							p2List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p3List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p4List.append( int( 0 - self.dList[self.intdoubles.get()] ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)
						
						else:
							self.p1 = int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) )
							self.p2 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p3 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p4 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )

							p1List.append(int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) ))
							p2List.append(int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p3List.append(int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p4List.append(int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4) 

					elif Action2.get() == 5:
						if Action3.get() == 0:
							self.p1 = int( self.dList[self.intdoubles.get()] * 3 )
							self.p2 = int(0 - self.dList[self.intdoubles.get()] ) 
							self.p3 = int(0 - self.dList[self.intdoubles.get()] )
							self.p4 = int(0 - self.dList[self.intdoubles.get()] )

							p1List.append( int( self.dList[self.intdoubles.get()] * 3 ))
							p2List.append( int(0 - self.dList[self.intdoubles.get()] ))
							p3List.append( int(0 - self.dList[self.intdoubles.get()] ))
							p4List.append( int(0 - self.dList[self.intdoubles.get()] ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

						
						else:
							self.p1 = int( ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2)*3 )
							self.p2 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p3 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p4 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )

							p1List.append(int( ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2)*3 ))
							p2List.append(int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p3List.append(int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p4List.append(int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)


				elif Action1.get() == 2:
					if Action2.get() == 1:
						if Action3.get() == 0:
							self.p1 = int( 0 - self.dList[self.intdoubles.get()] )
							self.p2 = int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) )
							self.p3 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p4 = int( 0 - self.dList[self.intdoubles.get() - 1] )

							p1List.append( int( 0 - self.dList[self.intdoubles.get()] ))
							p2List.append( int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) ))
							p3List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p4List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

						else:
							self.p1 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p2 = int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) )
							self.p3 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p4 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )

							p1List.append(int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p2List.append(int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) ))
							p3List.append(int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p4List.append(int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

					elif Action2.get() == 3:
						if Action3.get() == 0:
							self.p1 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p2 = int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) )
							self.p3 = int( 0 - self.dList[self.intdoubles.get()] )
							self.p4 = int( 0 - self.dList[self.intdoubles.get() - 1] )

							p1List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p2List.append( int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) ))
							p3List.append( int( 0 - self.dList[self.intdoubles.get()] ))
							p4List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)
						else:
							self.p1 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p2 = int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) )
							self.p3 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p4 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )

							p1List.append(int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p2List.append(int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) ))
							p3List.append(int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p4List.append(int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

					elif Action2.get() == 4:
						if Action3.get() == 0:
							self.p1 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p2 = int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) )
							self.p3 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p4 = int( 0 - self.dList[self.intdoubles.get()] )

							p1List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p2List.append( int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) ))
							p3List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p4List.append( int( 0 - self.dList[self.intdoubles.get()] ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

						else:
							self.p1 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p2 = int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) )
							self.p3 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p4 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )

							p1List.append(int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p2List.append(int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) ))
							p3List.append(int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p4List.append(int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)	

					elif Action2.get() == 5:
						if Action3.get() == 0:
							self.p1 = int(0 - self.dList[self.intdoubles.get()] )
							self.p2 = int( self.dList[self.intdoubles.get()] * 3 )
							self.p3 = int(0 - self.dList[self.intdoubles.get()] )
							self.p4 = int(0 - self.dList[self.intdoubles.get()] )

							p1List.append( int(0 - self.dList[self.intdoubles.get()] ))
							p2List.append( int( self.dList[self.intdoubles.get()] * 3 ))
							p3List.append( int(0 - self.dList[self.intdoubles.get()] ))
							p4List.append( int(0 - self.dList[self.intdoubles.get()] ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

						else:
							self.p1 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p2 = int( ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2)*3 )
							self.p3 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p4 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )

							p1List.append(int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p2List.append(int( ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2)*3 ))
							p3List.append(int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p4List.append(int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

					

				elif Action1.get() == 3:
					if Action2.get() == 1:
						if Action3.get() == 0:
							self.p1 = int( 0 - self.dList[self.intdoubles.get()] )
							self.p2 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p3 = int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) )
							self.p4 = int( 0 - self.dList[self.intdoubles.get() - 1] )

							p1List.append( int( 0 - self.dList[self.intdoubles.get()] ))
							p2List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p3List.append( int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) ))
							p4List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

						else:
							self.p1 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p2 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p3 = int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) )
							self.p4 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )

							p1List.append( int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p2List.append( int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p3List.append( int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) ))
							p4List.append( int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

					elif Action2.get() == 2:
						if Action3.get() == 0:
							self.p1 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p2 = int( 0 - self.dList[self.intdoubles.get()] )
							self.p3 = int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) )
							self.p4 = int( 0 - self.dList[self.intdoubles.get() - 1] )

							p1List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p2List.append( int( 0 - self.dList[self.intdoubles.get()] ))
							p3List.append( int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) ))
							p4List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

						else:
							self.p1 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p2 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p3 = int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) )
							self.p4 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )

							p1List.append( int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p2List.append( int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p3List.append( int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) ))
							p4List.append( int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

					elif Action2.get() == 4:
						if Action3.get() == 0:
							self.p1 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p2 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p3 = int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) )
							self.p4 = int( 0 - self.dList[self.intdoubles.get()] )

							p1List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p2List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p3List.append( int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) ))
							p4List.append( int( 0 - self.dList[self.intdoubles.get()] ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

						else:
							self.p1 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p2 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p3 = int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) )
							self.p4 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )

							p1List.append( int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p2List.append( int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p3List.append( int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) ))
							p4List.append( int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

					elif Action2.get() == 5:
						if Action3.get() == 0:
							self.p1 = int(0 - self.dList[self.intdoubles.get()] )
							self.p2 = int(0 - self.dList[self.intdoubles.get()] )
							self.p3 = int( self.dList[self.intdoubles.get()] * 3 )
							self.p4 = int(0 - self.dList[self.intdoubles.get()] )

							p1List.append( int(0 - self.dList[self.intdoubles.get()] ))
							p2List.append( int(0 - self.dList[self.intdoubles.get()] ))
							p3List.append( int( self.dList[self.intdoubles.get()] * 3 ))
							p4List.append( int(0 - self.dList[self.intdoubles.get()] ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

						else:
							self.p1 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p2 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p3 = int( ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2)*3 )
							self.p4 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )

							p1List.append( int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p2List.append( int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p3List.append( int( ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2)*3 ))
							p4List.append( int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

						
				elif Action1.get() == 4:
					if Action2.get() == 1:
						if Action3.get() == 0:
							self.p1 = int( 0 - self.dList[self.intdoubles.get()] )
							self.p2 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p3 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p4 = int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) )

							p1List.append( int( 0 - self.dList[self.intdoubles.get()] ))
							p2List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p3List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p4List.append( int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

						else:
							self.p1 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p2 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p3 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p4 = int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) )

							p1List.append( int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p2List.append( int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p3List.append( int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p4List.append( int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

					elif Action2.get() == 2:
						if Action3.get() == 0:
							self.p1 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p2 = int( 0 - self.dList[self.intdoubles.get()] )
							self.p3 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p4 = int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) )

							p1List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p2List.append( int( 0 - self.dList[self.intdoubles.get()] ))
							p3List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p4List.append( int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

						else:
							self.p1 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p2 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p3 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p4 = int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) )

							p1List.append( int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p2List.append( int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p3List.append( int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p4List.append( int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

					elif Action2.get() == 3:
						if Action3.get() == 0:
							self.p1 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p2 = int( 0 - self.dList[self.intdoubles.get() - 1] )
							self.p3 = int( 0 - self.dList[self.intdoubles.get()] )




							self.p4 = int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) )

							p1List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p2List.append( int( 0 - self.dList[self.intdoubles.get() - 1] ))
							p3List.append( int( 0 - self.dList[self.intdoubles.get()] ))
							p4List.append( int( self.dList[self.intdoubles.get()] + (self.dList[self.intdoubles.get() - 1]*2) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

						else:
							self.p1 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p2 = int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) )
							self.p3 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p4 = int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) )

							p1List.append( int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p2List.append( int( 0 - ((self.dList[self.intdoubles.get()]+self.dList[self.intdoubles.get()-1])/2) ))
							p3List.append( int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p4List.append( int( (self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()]) ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

					elif Action2.get() == 5:
						if Action3.get() == 0:
							self.p1 = int(0 - self.dList[self.intdoubles.get()] )
							self.p2 = int(0 - self.dList[self.intdoubles.get()] )
							self.p3 = int(0 - self.dList[self.intdoubles.get()] )
							self.p4 = int( self.dList[self.intdoubles.get()] * 3 )

							p1List.append( int(0 - self.dList[self.intdoubles.get()] ))
							p2List.append( int(0 - self.dList[self.intdoubles.get()] ))
							p3List.append( int(0 - self.dList[self.intdoubles.get()] ))
							p4List.append( int( self.dList[self.intdoubles.get()] * 3 ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

						else:
							self.p1 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p2 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p3 = int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) )
							self.p4 = int( ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2)*3 )

							p1List.append( int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p2List.append( int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p3List.append( int( 0 - ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2) ))
							p4List.append( int( ((self.dList[self.intdoubles.get()+1]+self.dList[self.intdoubles.get()])/2)*3 ))

							self.printscore(self.p1, self.p2, self.p3, self.p4)

		print p1List
		print p2List
		print p3List
		print p4List

	def delete(self):
	        global v, u

	        if v > 1 and v < 25:

	            if u == 1:
	                v -= 1

	                self.rest1 = Label(top, text = '', width = 10)
	                self.rest1.grid(column = 5, row = v)

	                self.rest2 = Label(top, text = '', width = 10)
	                self.rest2.grid(column = 6, row = v)

	                self.rest3 = Label(top, text = '', width = 10)
	                self.rest3.grid(column = 7, row = v)

	                self.rest4 = Label(top, text = '', width = 10)
	                self.rest4.grid(column = 8, row = v)
	                
	                p1List.pop(-1)
	                p2List.pop(-1)
	                p3List.pop(-1)
	                p4List.pop(-1)

	        elif v == 25 and u == 1:
	            
	            self.rest1 = Label(top, text = '', width = 10)
	            self.rest1.grid(column = 5, row = v-1)

	            self.rest2 = Label(top, text = '', width = 10)
	            self.rest2.grid(column = 6, row = v-1)

	            self.rest3 = Label(top, text = '', width = 10)
	            self.rest3.grid(column = 7, row = v-1)

	            self.rest4 = Label(top, text = '', width = 10)
	            self.rest4.grid(column = 8, row = v-1)
	            
	            p1List.pop(-1)
	            p2List.pop(-1)
	            p3List.pop(-1)
	            p4List.pop(-1)
	            v -= 1

	        elif v == 25 and v < 50 and u > 1:

	            u -= 1
	            
	            self.rest1 = Label(top, text = '', width = 10)
	            self.rest1.grid(column = 9, row = u)

	            self.rest2 = Label(top, text = '', width = 10)
	            self.rest2.grid(column = 10, row = u)

	            self.rest3 = Label(top, text = '', width = 10)
	            self.rest3.grid(column = 11, row = u)

	            self.rest4 = Label(top, text = '', width = 10)
	            self.rest4.grid(column = 12, row = u)

	            p1List.pop(-1)
	            p2List.pop(-1)
	            p3List.pop(-1)
	            p4List.pop(-1) 

	def printscore(self, p1, p2, p3, p4):

		global u, v, Action1, Action2

		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		self.p4 = p4

		if v >= 1 and v < 25:

			self.rest1 = Label(top, text = self.p1)
			self.rest1.grid(column = 5, row = v)

			self.rest2 = Label(top, text = self.p2)
			self.rest2.grid(column = 6, row = v)

			self.rest3 = Label(top, text = self.p3)
			self.rest3.grid(column = 7, row = v)

			self.rest4 = Label(top, text = self.p4)
			self.rest4.grid(column = 8, row = v)

			v += 1
			
		elif v >= 25 and v < 50:

			self.rest1 = Label(top, text = self.p1)
			self.rest1.grid(column = 9, row = u)

			self.rest2 = Label(top, text = self.p2)
			self.rest2.grid(column = 10, row = u)

			self.rest3 = Label(top, text = self.p3)
			self.rest3.grid(column = 11, row = u)

			self.rest4 = Label(top, text = self.p4)
			self.rest4.grid(column = 12, row = u)
			u += 1

		
		pass

	def finish(self):
		
		self.finish1 = Label(top, text = self.s1.get() + ':')
		self.finish1.grid(column = 2 , row = 14)
		self.finish1score = Label(top, text = sum(p1List), width = 5)
		self.finish1score.grid(column = 3, row = 14)


		self.finish2 = Label(top, text = self.s2.get() + ':')
		self.finish2.grid(column = 2, row = 15)
		self.finish2score = Label(top, text = sum(p2List), width = 5)
		self.finish2score.grid(column = 3, row = 15)


		self.finish3 = Label(top, text = self.s3.get() + ':')
		self.finish3.grid(column = 2, row = 16)
		self.finish3score = Label(top, text = sum(p3List), width = 5)
		self.finish3score.grid(column = 3, row = 16)


		self.finish4 = Label(top, text = self.s4.get() + ':')
		self.finish4.grid(column = 2, row = 17)
		self.finish4score = Label(top, text = sum(p4List), width = 5)
		self.finish4score.grid(column = 3, row = 17)






print p1List
print p2List
print p3List
print p4List


top = Tk()
top.title('Mahjong')


myGui = mahjong(top)

top.mainloop()

