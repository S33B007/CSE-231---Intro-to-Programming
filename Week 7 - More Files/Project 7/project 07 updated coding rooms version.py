###########################################################

    #  Computer Project #5
    #
    # Algorithm
   #  a Python program that uses the MovieLens dataset to answer questions like the
   #  highest average rated movies in a year, specific genre, by a specific gender (male or female), or a
   #  specific profession (occupational group).
   #  open file function
   #      This function prompts the user to input a file name to open and keeps prompting until a
   #      correct name is entered
   #  read_review function
   #      This function reads the reviews.txt file using the file pointer fp
   #  read_ users function
   #      This function reads the user.txt file using file pointer fp and returns a list of tuples
   #  read movies function
   #      This function reads the movies.txt file using the parameter fp
   #  year movies function
   #      This function filters the main movie list to find movies for a specific year and 
   #      returns their ids movieID as a sorted list in ascending order
   #  genre movies function
   #      This function filters the main movie list to find movies for a specific genre and returns
   #      their ids as a list.
   #  gen users function
   #      This function filters the main reviews list to find reviews for a specific gender of users and
   #      returns them as a list of lists
   #  occ users function
   #      This function filters the main reviews list to find reviews for a specific occupation of users and
   #      returns them as a list of lists
   # main
   #     Depending on the option selected it would prompt the user for an appropriate option and
   #     display the result based on the selection. The function would keep prompting the user for
   #     option until the user quits
    ###########################################################








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
    filename = input('\nInput {} filename: '.format(s))
    while True:
        try:
            fp = open(filename,"r",encoding ="windows-1252")
            return fp
        except FileNotFoundError:
            print('\nError: No such file; please try again.')
            filename = input('\nInput {} filename: '.format(s))  
    return fp

def read_reviews(N,fp):
    ''' This function reads the reviews.txt file using the file pointer fp'''
    # Helped by TA
    L_reviews = [[]for i in range(N + 1)]
    for line in fp:
        new_line = line.split()
        new_line = [int(i) for i in new_line[:3]]
        # setting the indexes to a variable for readability
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
        # defining the indexes with variables for readability
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
    master_list = [[]]
    genres = []
    for line in fp:
        result = line.strip().split("|")
        movie_id = int(result[0])
        title = result[1]
        date = result[2]
        empty_space = [3]
        url = result[4]
        genre = result[5:]
        genre = [int(i) for i in genre]
        genres = [(GENRES[i]) for i, variable in enumerate(genre) if variable ==1]
        # for i,variable in enumerate(genre):
            # if variable == 1:
                # genres.append(GENRES[i])
        list_of_tuples = (title, date, genres)
        master_list.append(list_of_tuples)
    return master_list
       
        


        
def year_movies(year,L_movies):
    ''' This function filters the main movie list to find movies for a specific year and 
    returns their ids movieID as a sorted list in ascending order'''
    list_of_years = []
    for i in range(len(L_movies)):
        try:
            # using i to index into a list, 1 to index into the tuple
            # and 7: to get the year in that tuple
            year_from_nl = int(L_movies[i][1][7:])
            if year == year_from_nl:
                list_of_years.append(i)
        except:
            continue
    return list_of_years

def genre_movies(genre,L_movies):
    ''' This function filters the main movie list to find movies for a specific genre and returns
        their ids as a list.'''
    list_of_genre = []
    for i in range(len(L_movies)):
        try:
            # using i to index the list and 2 to find the movie name
            genre_from_nl = L_movies[i][2]
            if genre in genre_from_nl:
                list_of_genre.append(i)
        except:
            continue
    return list_of_genre

def gen_users (gender, L_users, L_reviews):
    ''' This function filters the main reviews list to find reviews for a specific gender of users and
        returns them as a list of lists'''
    list_of_users = []
    for i in range(len(L_users)):
        try:
            # using i to index into the list and 1 to find the gender
            genders = L_users[i][1]
            if genders == gender:
                reviews = L_reviews[i]
                list_of_users.append(reviews)
        except:
            continue
    return list_of_users
            
          
def occ_users (occupation, L_users, L_reviews):
    ''' This function filters the main reviews list to find reviews for a specific occupation of users and
        returns them as a list of lists'''
    list_of_users = []
    for i in range(len(L_users)):
        try:
            # using i to index into the list and 1 to find the gender
            occupations = L_users[i][2]
            if occupations == occupation:
                reviews = L_reviews[i]
                list_of_users.append(reviews)
        except:
            continue
    return list_of_users

def highest_rated_by_movie(L_in,L_reviews,N_movies):
    ''' This function calculates the average rating for the reviews in L_reviews list of the
        movies in L_in list and returns a list of the highest average rated movies and the highest
        average. '''
    # helped by TA
    total = [0] * len(L_in) # total for each review
    times = [0] * len(L_in)
    avg = [0] * len(L_in)
    for i in range(len(L_in)):
        for j in L_reviews:
            if j != []:
                for k in j:
                    if L_in[i] == k[0]:
                        total[i] += k[1]
                        times[i] += 1
    for i in range(len(L_in)):
        avg[i] = round(total[i] / times[i],2)
        max_list = []
        max_ = -1
    for i in range(len(avg)):
        if avg[i] > max_:
            max_ = avg[i]
            max_list = []
        if avg[i] == max_:
            max_list.append(L_in[i])
    return max_list, max_
        
             
def highest_rated_by_reviewer(L_in,N_movies):
    ''' This function calculates the average rating for movies by a specific group of users (L_in)
        and returns a list of the highest average rated movies and the highest average'''
    # helped by TA Mr. Zane 
    rating_sums = [0] * N_movies
    rating_count = [0] * N_movies
    for review_list in L_in:
        for movie_id,rating in review_list:
            if rating == 0 or movie_id == 0:
                continue
            rating_sums[movie_id - 1] += rating
            rating_count[movie_id - 1] += 1
    max_avg = 0
    movie_avgs = []
    for i in range(N_movies):
        try:
            average = round(rating_sums[i]/rating_count[i], 2)
            if average > max_avg:
                max_avg = average
            movie_avgs.append(average)
        except:
            movie_avgs.append(0)
    movies_with_highest_ratings = []
    for index, avg in enumerate(movie_avgs):
        if max_avg == avg:
            movies_with_highest_ratings.append(index + 1)
    return movies_with_highest_ratings, max_avg

 
def main():
    user_file = open_file("users")
    review_file = open_file("reviews")
    movie_file = open_file("movies")
    user_list = read_users(user_file)
    N = len(user_list)
    review_list = read_reviews(N, review_file)
    movie_list = read_movies(movie_file)
    print(MENU)
    option = int(input('\nSelect an option (1-5): '))
    while option != 5:
        if option == 1:
            year = int(input('\nInput a year: '))
            while True:
                if 1930 <= year <= 1998:
                    # new vaiable for year_movies
                    ym = year_movies(year,movie_list)
                    # new variable for highest rated by movies
                    hrbm_year = highest_rated_by_movie(ym, review_list, N)
                    hrbm = hrbm_year[1]
                    print('\nAvg max rating for the year is:',hrbm)
                    for movie_id in hrbm_year[0]:
                        print(movie_list[movie_id][0])
                    break
                else:
                    print("\nError in year.")
                    year = int(input('\nInput a year: '))
        elif option == 2:
            print('\nValid Genres are: ', GENRES)
            genre = input('Input a genre: ')
                # concacinating them to make one word
                # capitalizing the first letter
            genre = genre.capitalize()
            while True:
                if genre in GENRES:
                    # new variable gm is genre movies
                    gm = genre_movies(genre, movie_list)
                    # new variable for highest rated by movies
                    N = len(movie_list)
                    hrbm_genre = highest_rated_by_movie(gm, review_list, N)
                    hrbm = hrbm_genre[1]
                    print('\nAvg max rating for the Genre is:',hrbm)
                    for movie_id in hrbm_genre[0]:
                        print(movie_list[movie_id][0])
                    break
                else:
                    print("\nError in genre.")
                    genre = input('Input a genre: ')
                    genre = genre.capitalize()
        elif option == 3:
            gender = input('\nInput a gender (M,F): ')
            genderU = gender.upper()
            while True:
                if genderU == 'F' or genderU == 'M':
                    gen = gen_users(genderU, user_list, review_list)
                    N = len(movie_list)
                    hrbr_gender = highest_rated_by_reviewer(gen, N)
                    hrbr1 = hrbr_gender[1]
                    print('\nAvg max rating for the Gender is:',hrbr1)
                    for movie_id in hrbr_gender[0]:
                        print(movie_list[movie_id][0])
                    break
                else:
                    print("\nError in gender.")
                    gender = input('\nInput a gender (M,F): ')
                    genderU = gender.upper()
        elif option == 4:
            print('\nValid Occupatipns are: ', OCCUPATIONS)
            occupations = input('Input an occupation: ')
            occupationsL = occupations.lower()
            while True:
                if occupationsL in OCCUPATIONS:
                    occ = occ_users(occupationsL, user_list, review_list)
                    N = len(movie_list)
                    hrbr_occ = highest_rated_by_reviewer(occ, N)
                    hrbr = hrbr_occ[1]
                    print('\nAvg max rating for the occupation is:',hrbr )
                    for movie_id in hrbr_occ[0]:
                        print(movie_list[movie_id][0])
                    break
                else:
                    print("\nError in occupation.")
                    occupations = input('Input an occupation: ')
                    occupationsL = occupations.lower()
        elif option == 5:
            break
        

        else:
            print("\nError: not a valid option.")
        option = int(input('\nSelect an option (1-5): '))


    

if __name__ == "__main__":
    main()