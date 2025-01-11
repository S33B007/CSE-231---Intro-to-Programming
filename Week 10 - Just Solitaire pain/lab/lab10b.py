
 
import cards
 
def fix_ace_rank(n):
    if n == 1:
        n = 13
    return n
 
# Create the deck of cards
 
the_deck = cards.Deck()
 
p1_list=[]
p2_list=[]
for i in range( 5 ):
    p1_list.append( the_deck.deal() )
    p2_list.append( the_deck.deal() )
 
print("Starting Hands")
print("Hand1:",p1_list)
print("Hand2:",p2_list)
p1_card = p1_list.pop( 0 )
p2_card = p2_list.pop( 0 )
 
if fix_ace_rank(p1_card.rank()) == fix_ace_rank(p2_card.rank()):
    print("Battle was 1: {}, 2: {}. Battle was a draw.".format(p1_card,p2_card))
    p1_list.append( p1_card )
    p2_list.append( p2_card )
elif fix_ace_rank(p1_card.rank()) > fix_ace_rank(p2_card.rank()):
    print("Battle was 1: {}, 2: {}. Player 1 wins battle.".format(p1_card,p2_card))
    p1_list.append( p1_card )
    p1_list.append( p2_card )
else:
    print("Battle was 1: {}, 2: {}. Player 2 wins battle.".format(p1_card,p2_card))
    p2_list.append( p2_card )
    p2_list.append( p1_card )
 
while True:
    
    print("hand1:",p1_list)
    print("hand2:",p2_list)
 
    if ( len(p1_list) != 0 ) and ( len(p2_list) != 0 ):
        p1_card = p1_list.pop( 0 )
        p2_card = p2_list.pop( 0 )
        if input("Keep Going: (Nn) to stop:").lower() != 'n':
            if fix_ace_rank(p1_card.rank()) == fix_ace_rank(p2_card.rank()):
                print("Battle was 1: {}, 2: {}. Battle was a draw.".format(p1_card,p2_card))
                p1_list.append( p1_card )
                p2_list.append( p2_card )
            elif fix_ace_rank(p1_card.rank()) > fix_ace_rank(p2_card.rank()):
                print("Battle was 1: {}, 2: {}. Player 1 wins battle.".format(p1_card,p2_card))
                p1_list.append( p1_card )
                p1_list.append( p2_card )
            else:
                print("Battle was 1: {}, 2: {}. Player 2 wins battle.".format(p1_card,p2_card))
                p2_list.append( p2_card )
                p2_list.append( p1_card )
        else:
            if len(p1_list) > len(p2_list):
                print("Player 1 wins!!!")
            elif len(p2_list) > len(p1_list):
                print("Player 2 wins!!!")
            break
    else:
        if len(p1_list) > len(p2_list):
            print("Player 1 wins!!!")
        elif len(p2_list) > len(p1_list):
            print("Player 2 wins!!!")
        break

