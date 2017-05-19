from deck import Deck
war=Deck()
war.Shuffle()
player1,player2=war.Cut()
play1=player1.findLength()
play2=player2.findLength()
while(play1!=0 and play2!=0):
	play1D=player1.TakeFromBottom()
	play2D=player2.TakeFromBottom()
	value1=play1D.checkRank()
	value2=play2D.checkRank()
	raw_input("Player1 Press Enter to draw")
	play1D.displayCard()
	raw_input("Player2 Press Enter to draw")
	play2D.displayCard()
	play1=player1.findLength()
	play2=player2.findLength()
if(play1>play2):
	print("Congrats Player 1 wins!")
else:
	print("Congrats Player 2 wins!")