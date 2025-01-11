GENRES = ['Unknown','Action', 'Adventure', 'Animation',"Children's",
          'Comedy','Crime','Documentary', 'Drama', 'Fantasy', 'Film-noir',
          'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
          'War', 'Western']
OCCUPATIONS = ['administrator', 'artist', 'doctor', 'educator', 'engineer',
               'entertainment', 'executive', 'healthcare', 'homemaker', 'lawyer',
               'librarian', 'marketing', 'none', 'other', 'programmer', 'retired',
               'salesman', 'scientist', 'student', 'technician', 'writer']
'''
Three main data structures (lists)
L_users, indexed by userID, list of tuples (age,gender,occupation)
L_reviews, indexed by userID, list of tuples (movieID, rating)
L_movies, indexed by movieID, list of tuples (movieName, releaseDate, list of genres)
'''
MENU = '''
        Options:
        1. Highest rated movie for a specific year
        2. Highest rated movie for a specific Genre
        3. Highest rated movies by a specific Gender (M,F)
        4. Highest rated movies by a specific occupation
        5. Quit
        '''
def open_file(s):
    ''' This function prompts the user to input a file name to open and keeps prompting until a
        correct name is entered'''
    while True:
        try:
            fp = open(s, "r", encoding ="windows-1252")
            return fp
        except FileNotFoundError:
            print('\nError: No such file; please try again.')
            s = input("Enter file name: ") 

def read_reviews(N,fp):
    ''' This function reads the reviews.txt file using the file pointer fp'''
    # Helped by TA
    L_reviews = [[]for i in range(N + 1)]
    for line in fp:
        new_line = line.split()
        new_line = [int(i) for i in new_line[:3]]
        user_Id = new_line[0]
        movie_id = new_line[1]
        rating = new_line[2]
        L_reviews[user_Id].append((movie_id,rating))
        L_reviews[user_Id].sort()
    return L_reviews

def read_users(fp):
    '''This function reads the user.txt file using file pointer fp and returns a list of tuples'''
    master_list = []
    master_list.append([])
    for line in fp:
        result = line.strip().split("|")
        result = result[0:4]
        reviewer_id = int(result[0])
        age = int(result[1])
        gender = result[2]
        occupation = result[3]
        list_of_tuples = (age, gender, occupation)
        master_list.append(list_of_tuples)
    return master_list
   


def read_movies(fp):
    ''' This function reads the movies.txt file using the parameter fp'''
    master_list = []
    genres = []
    master_list.append([])
    for line in fp:
        result = line.strip().split("|")
        movie_id = int(result[0])
        title = result[1]
        date = result[2]
        empty_space = [3]
        url = result[4]
        genre = result[5:]
        for i in genre:
            if i == 1:
                genres.append(GENRES[i])
        list_of_tuples = (title, date, genres)
        master_list[movie_id].append(list_of_tuples)
    return master_list
       
        


        
def year_movies(year,L_movies):
    ''' Docstring'''
    pass   # remove this line

def genre_movies(genre,L_movies):
    ''' Docstring'''
    pass   # remove this line

def gen_users (gender, L_users, L_reviews):
    ''' Docstring'''
    pass   # remove this line
          
def occ_users (occupation, L_users, L_reviews):
    ''' Docstring'''
    pass   # remove this line

def highest_rated_by_movie(L_in,L_reviews,N_movies):
    ''' Docstring'''
    pass   # remove this line
             
def highest_rated_by_reviewer(L_in,N_movies):
    ''' Docstring'''
    pass   # remove this line
 
def main():
    s = input("Enter file name: ")
    if s == "users.txt":
        fp = open_file(s) 
        print(read_users(fp))  
    if s == "movies.txt":
        fp = open_file(s) 
        print(read_movies(fp))
    

if __name__ == "__main__":
    main()
                                           
