###########################################################
    #  Computer Project #5
    #
    #  Algorithm
    # open_file funciton:
    #     This function is going to ask the user for both files to open
    # read_file function:
    #     This function takes the security’s file pointer that has the names of the companies and
    #     their codes. It creates a set of all the company’s names. And it also creates a master 
    #     dictionary where the key is the company code. 
    # add_prices function:
    #     This function does not return anything, but it changes the master dictionary while reading
    #     the prices file
    # get_max_price_of_company function:
    #     This function takes the master dictionary and a company symbol, and it gets the max high
    #     price and the date of the max price. It returns the tuple
    # find_max_price_company_price cuntion:
    #     This function takes the master dictionary and finds the company with the highest high
    #     price
    # get_avg_price_of_company function:
    #     This function uses the master dictionary and company symbol to find the average high
    #     price for the company
    # display_list function:
    #     This function does not return anything, but it takes a list of strings and displays that list in three
    #     columns, each column is 35 characters wide.
    # main function:
    #     print statements
    #     open file
    #     read file
    #     edit master dictionary
    #     while option is not 6:
    #         if option is 1:
    #             print statements
    #         elif option is 2:
    #             print statements
    #         elif option is 3:
    #             prompt for an input
    #             while its False:
    #                 re prompt
    #             if True:
    #                 print statements
    #         elif option is 4:
    #             print statements
    #         elif option is 5:
    #             prompt for an input
    #             while its False:
    #                 re prompt
    #             if True:
    #                 print statements
    #         elif option is 6:
    #             quit program
    #         else:
    #             print statement 
    #             ask for option     
    # call main function
    ###########################################################

import csv

MENU = '''\nSelect an option from below:
            (1) Display all companies in the New York Stock Exchange
            (2) Display companies' symbols
            (3) Find max price of a company
            (4) Find the company with the maximum stock price
            (5) Find the average price of a company's stock
            (6) quit
    '''
WELCOME = "Welcome to the New York Stock Exchange.\n"
    
def open_file():
    '''This function is going to ask the user for both files to open'''
    fp1 = input("\nEnter the price's filename: ")
    while True:
        try:
            fp1 = open(fp1, "r")
            try:
                fp2 = input("\nEnter the security's filename: ")
                fp2 = open(fp2, "r")
                return fp1, fp2
            except FileNotFoundError:
                print("\nFile not found. Please try again.")
        except FileNotFoundError:
            print("\nFile not found. Please try again.")
            fp1 = input("\nEnter the price's filename: ")
    return fp1, fp2

def read_file(securities_fp):
    '''This function takes the security’s file pointer that has the names of the companies and
        their codes. It creates a set of all the company’s names. And it also creates a master 
        dictionary where the key is the company code. '''
    company_name_set = set() # set of all company names
    master_dict = {} # key is company code
    securities = csv.reader(securities_fp)
    next(securities, None)
    for line in securities:
        # give the indexes a new name for me to better understand
        code = line[0]
        company_name = line[1]
        company_name_set.add(company_name)
        sector = line[3]
        subsector = line[4]
        address = line[5]
        date_add = line[6]
        value_list = [company_name, sector, subsector, address, date_add, []]
        master_dict[code] = value_list
    return company_name_set, master_dict


        
def add_prices (master_dictionary, prices_file_pointer):
    '''This function does not return anything, but it changes the master dictionary while reading
        the prices file'''
    
    csv.reader(prices_file_pointer)
    next(prices_file_pointer)
    for line01 in prices_file_pointer:
        line = line01.split(',')
        # give the indexes a new name for me to better understand
        date = line[0]
        company_symbol = line[1]
        open_info = float(line[2])
        close_info = float(line[3])
        low_info = float(line[4])
        high_info = float(line[5])
        price_list = [date, open_info, close_info, low_info, high_info]
        if company_symbol in master_dictionary.keys():
            value = master_dictionary.get(company_symbol)
            master_dictionary[company_symbol][5].append(price_list)

        

def get_max_price_of_company (master_dictionary, company_symbol):
    '''This function takes the master dictionary and a company symbol, and it gets the max high
        price and the date of the max price. It returns the tuple'''
    master_list = []
    # checking conditions first
    if company_symbol not in master_dictionary:
        final_tuple = (None, None)
        return final_tuple
    prices = master_dictionary[company_symbol][5]
    if prices == []:
        final_tuple = (None, None)
        return final_tuple

    for lists in prices:
        date = lists[0]
        high_info = lists[4]
        tuples = (high_info, date)
        master_list.append(tuples)
    max_tuple = max(master_list)
    return max_tuple

            

def find_max_company_price (master_dictionary):
    '''This function takes the master dictionary and finds the company with the highest high
        price'''
    master_list = []
    for key, value in master_dictionary.items():
        if value[5] == []:
            continue
        max_high_price_max_date = get_max_price_of_company(master_dictionary, key)
        if max_high_price_max_date == (None, None):
            continue
        else:
            max_high_price = max_high_price_max_date[0]
            max_comp_price = (max_high_price, key)
            master_list.append(max_comp_price)
    max_ = max(master_list)
    max_company = max_[1]
    max_price = max_[0]
    final_tuple = (max_company, max_price)
    return final_tuple
    


def get_avg_price_of_company (master_dictionary, company_symbol):
    '''This function uses the master dictionary and company symbol to find the average high
        price for the company'''
    master_list = []
    high_price_list = []
    if company_symbol in master_dictionary:
        # cheching condition if list is empty
        if master_dictionary[company_symbol][5] == []:
            final = 0.0
            return final
        total = len(master_dictionary[company_symbol][5])
        # itterating through each list and grabbing the high price info to use in my sum(master_list)
        for lst in master_dictionary[company_symbol][5]:
            high_price = lst[-1]
            high_price_list.append(high_price)
        average = float((sum(high_price_list)/total))
        final = round(average, 2)
        return final
    else:
        final = 0.0
        return final

        
        
            
def display_list (lst):  # "{:^35s}"
    '''This function does not return anything, but it takes a list of strings and displays that list in three
        columns, each column is 35 characters wide.'''
    for index, name in enumerate(lst):
        print("{:^35s}".format(name), end = '')
        # using this condition so at each index where this is tru rint new line
        # at 2, 5, 8, and so on i print indexes 0,1,2 then 3,4,5 then 6,7,8 at new rows each
        if index % 3 == 2:
            print()
    print("\n")
    
def main():
    print(WELCOME)
    prices_fp, securities_fp = open_file()
    company_name, master_dict = read_file(securities_fp)
    add_prices(master_dict, prices_fp)
    print(MENU)
    option = input("\nOption: ")
    while option != "6":
        if option == "1":
            print()
            title = "Companies in the New York Stock Market from 2010 to 2016"
            print("{:^105s}".format(title))
            # since company_name is currently a tuple i need to convert it to a sorted list to index correctly in display func
            lst = sorted(list(company_name))
            display_list(lst)
            print(MENU)
        elif option == "2":
            print("\ncompanies' symbols:")
            # since company_name is currently a tuple i need to convert it to a sorted list to index correctly in display func
            lst_code = sorted(list(master_dict.keys()))
            display_list(lst_code)
            print(MENU)
        elif option == "3":
            prompt_symbol = input("\nEnter company symbol for max price: ")
            while prompt_symbol not in master_dict:
                print("\nError: not a company symbol. Please try again.")
                prompt_symbol = input("\nEnter company symbol for max price: ")
            if prompt_symbol in master_dict:
                tuples = get_max_price_of_company(master_dict, prompt_symbol)
                # since tuples is a tuple if None is in either 0 or 1 index, do as follows
                if None in tuples:
                    print("\nThere were no prices.")
                else:
                    print("\nThe maximum stock price was ${:.2f} on the date {:s}/\n". format(tuples[0], tuples[1]))
                print(MENU)
        elif option == "4":
            tuples = find_max_company_price(master_dict)
            print("\nThe company with the highest stock price is {:s} with a value of ${:.2f}\n".format(tuples[0], tuples[1]))
            print(MENU)
        elif option == "5":
            prompt_symbol = input("\nEnter company symbol for average price: ")
            while prompt_symbol not in master_dict:
                print("\nError: not a company symbol. Please try again.")
                prompt_symbol = input("\nEnter company symbol for average price: ")
            if prompt_symbol in master_dict:
                average = get_avg_price_of_company(master_dict, prompt_symbol)
                if average == 0.0:
                    print("\nThere were no prices.")
                else:
                    print("\nThe average stock price was ${:.2f}.\n". format(average))
                print(MENU)
        elif option == "6":
            break
        else:
            print("\nInvalid option. Please try again.")
        option = input("\nOption: ")

    
       
if __name__ == "__main__": 
    main() 
