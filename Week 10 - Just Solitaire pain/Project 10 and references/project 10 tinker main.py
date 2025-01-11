
from cards import Card, Deck

MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''
def initialize():
    '''The function has no parameters and returns the starting state of the game with the four data
        structures, tableau, stock, foundation, waste '''
    stock = Deck()
    tableau = [[], [], [], [], [], [], []]
    foundation = [[], [], [], []]
    waste = []
    stock.shuffle()
    for i in range(8):
        # use i to index through list to get correct format of tableau
         for lists in tableau[i:]:
             new_card = stock.deal()
             new_card.flip_card()
             lists.append(new_card)
    # flip the last card of each list
    for lists in tableau:
        lists[-1].flip_card()
    waste_card = stock.deal()
    waste.append(waste_card)

    
    
    
        
    return tableau, stock, foundation, waste  
def display(tableau, stock, foundation, waste):
    """ display the game setup """
    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" #stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
    

def stock_to_waste( stock, waste ):
    '''this function moves a card from the stock to the waste'''
    # if the amount of cards in the stock is greater than 0, deal the card
    if len(stock) > 0:
        waste.append(stock.deal())
        return True
    else:
        return False
    return True

    
       
def waste_to_tableau( waste, tableau, t_num ):
    '''The program will use the following function to move a card from the waste to tableau'''
    # if there is nothing in the waste deck return false
    if len(waste) == 0:
        return False
        
    waste_card = waste[-1]
    # conditon if designated tableau column is empty and current card to move is king, allow the move
    if (tableau[t_num] == [] and waste_card.rank() == 13):
        card = waste.pop()
        tableau[t_num].append(card)
        return True

    if len(tableau[t_num]) == 0:
        return False

    tab_card = tableau[t_num][-1]
    # if the waste card is 1 rank lower than that of the tablaeu card and they are opposite colors
    if (waste_card.rank() + 1 == tab_card.rank()):
        # if the waste card suit is black
        if waste_card.suit() == 1 or waste_card.suit() == 4:
            # and the desitantion tableau card suit is not black, so red
            if tab_card.suit() != 4 and tab_card.suit() != 1:
                card = waste.pop()
                tableau[t_num].append(card)
                return True
        # if the waste card is red
        if waste_card.suit() == 2 or waste_card.suit() == 3:
            # and the desitantion tableau card suit is not red, so black
            if tab_card.suit() != 2 and tab_card.suit() != 3:
                card = waste.pop()
                tableau[t_num].append(card)
                return True
    return False

    

# waste is a list and foundation is a list of list
def waste_to_foundation( waste, foundation, f_num ):
    '''The program will use the following function to move a card from the waste to a foundation'''
    # f_num is used as an index to pinpoint which stack in the foundation
    try:
        # try to index into the 
        waste_card = waste[-1]
        try:
            top_foundation = foundation[f_num][-1]
        except:
            x = 0 # useless code to continue
        # if the top waste card is ace and the designated foundatin is empty pop from the wast and add it to foundation
        if (waste_card.rank() == 1) and (foundation[f_num] == []):
            card = waste.pop()
            foundation[f_num].append(card)
            return True
        # if rank is not ace then deny the move
        elif (foundation[f_num] == [] and waste_card.rank() != 1):
            return False
        # if the waste card suit matches with that of the designated foundaiton and
        # 1 minus the rank of the waste card is equal to the deisgnated foundation card, then add card
        if (waste_card.suit() == top_foundation.suit()) and ((waste_card.rank() - 1) == top_foundation.rank()):
            foundation[f_num].append(waste.pop())
            return True
        else:
            return False
    # if waste is empty then make it invalid
    except IndexError:
        return False
    

def tableau_to_foundation( tableau, foundation, t_num, f_num ):
    '''The program will use the following function to move a card from the tableau to a foundation'''
    try:
        # check if tableau is empty
        tab_card = tableau[t_num][-1]
        try:
            found_card = foundation[f_num][-1]
        except:
            if tab_card.rank() == 1 and foundation[f_num] == []:
                # tableau[t_num].pop()
                foundation[f_num].append(tab_card)
                # if tableau card is not face up flip the card 
                if not tableau[t_num][-1].is_face_up():
                    tableau[t_num][-1].flip_card()
                    return True
                if tableau[t_num][-1].is_face_up():
                    tableau[t_num].pop()
                    if len(tableau[t_num]) > 0:
                        tableau[t_num][-1].flip_card()
                    return True        
                found_card = foundation[f_num][-1]
            else:
                return False
        if tab_card.rank() == 1 and foundation[f_num] == []:
            card = tableau[t_num].pop()
            foundation[f_num].append(card)
            if not tableau[t_num][-1].is_face_up():
                tableau[t_num][-1].flip_card()
                return True
            if tableau[t_num][-1].is_face_up():
                return True

        if tab_card.suit() == found_card.suit() and tab_card.rank() -1 == found_card.rank():
            card = tableau[t_num].pop()
            foundation[f_num].append(card)
            if not tableau[t_num][-1].is_face_up():
                tableau[t_num][-1].flip_card()
                return True
            if tableau[t_num][-1].is_face_up():
                return True
        return False
    # if tableau is empty then void move
    except IndexError:
        x = 0


def tableau_to_tableau( tableau, t_num1, t_num2 ):
    '''this following function will move a card from one column in the tableau to
        another column'''
    # t_num1 = the index for the starting list to get your card
    # t_num2 =  the index for the list you want to move the card to
    initial_card = tableau[t_num1][-1]
    try:
        last_col_card = tableau[t_num2][-1]
    except:
        x=0 # uselesee code b/c i can't use continue
    if (tableau[t_num2] == [] and initial_card.rank() == 13):
        tableau[t_num2].append(tableau[t_num1].pop())
        tableau[t_num1][-1].flip_card()
        return True
    if len(tableau[t_num2]) == 0:
        return False
    initial_card = tableau[t_num1][-1]
    last_col_card = tableau[t_num2][-1]
    # if the waste card is 1 rank lower than that of the tablaeu card and they are opposite colors
    if (initial_card.rank() + 1 == last_col_card.rank()):

        # if initial card suit is black
        if initial_card.suit() == 1 or initial_card.suit() == 4:
            # and destination card suit is not black, so red
            if last_col_card.suit() != 4 and last_col_card.suit() != 1:
                tableau[t_num2].append(tableau[t_num1].pop())
                if len(tableau[t_num1]) > 0:
                    tableau[t_num1][-1].flip_card()
                return True

        # if initial card suit is red
        elif initial_card.suit() == 2 or initial_card.suit() == 3:
            # and destination card suit is not black, so red
            if last_col_card.suit() != 2 and last_col_card.suit() != 3:
                tableau[t_num2].append(tableau[t_num1].pop())
                if len(tableau[t_num1]) > 0:
                    tableau[t_num1][-1].flip_card()
                return True
    return False

    
def check_win (stock, waste, foundation, tableau):
    '''Docstring'''
    total = 0
    if stock.is_empty() and len(waste) == 0 :
        for i in tableau:
            if len(i) == 0:
                total += 1
        if total == 7:
            return True
        else:
            return False
    else:
        return False

def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            #elif opt_str == 'MFT' and (source < 0 or source > 3):
                #print("Error in Source.")
                #return None
            # source values are valid
            # check for valid destination values
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   # none of the above


def main():   
    tableau, stock, foundation, waste = initialize()
    print(MENU)
    # display(tableau, stock, foundation, waste)

    while True:
        display(tableau, stock, foundation, waste)
        prompt = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): ")
        option = parse_option(prompt)
        if option == None:
            continue
        opt = option[0]
        
        
        # source = option[1] - 1
        # destination = option[2] - 1
        
        if opt == "TT":
            boolean = tableau_to_tableau(tableau, option[1] - 1, option[2] - 1)
            if boolean == False:
                print("\nInvalid move!\n")
                
        elif opt == "TF":
            boolean = tableau_to_foundation(tableau, foundation, option[1] - 1, option[2] - 1)
            if boolean == False:
                print("\nInvalid move!\n")
                
            else:
                check_dub = check_win(stock, waste, foundation, tableau)
                if check_dub == True:
                    print("You won!")
                    display(tableau, stock, foundation, waste)
                    break

        # destination = option[1]-1
        elif opt == "WT":
            boolean = waste_to_tableau(waste, tableau, option[1]-1)
            if boolean == False:
                print("\nInvalid move!\n")
                

        elif opt == "WF":
            boolean = waste_to_foundation(waste, foundation, option[1]-1)
            if boolean == False:
                print("\nInvalid move!\n")
                
              
            else:
                check_dub = check_win(stock, waste, foundation, tableau)
                if check_dub == True:
                    print("You won!")
                    display(tableau, stock, foundation, waste)
                    break

        elif opt == "SW":
            boolean = stock_to_waste(stock, waste)
            if boolean == False:
                print("\nInvalid move!\n")
            
        elif opt == "R":
            tableau, stock, foundation, waste = initialize()
            print(MENU)
            
        elif opt == "H":
            print(MENU)
        elif opt == "Q": 
            break

                
            
        
        

if __name__ == '__main__':
     main()
