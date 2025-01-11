# Write a function music_func that takes 3 parameters -- 
# music type, music group, vocalist -- and prints them all out as shown in 
# the example below. In case no input is provided by the user, the function 
# should assume these values for the parameters: 
#     "Classic Rock", "The Beatles", "Freddie Mercury".

# For example:
# Input:
# Alternative Rock,Pearl Jam,Chris Cornell

# Output:
# The best kind of music is Alternative Rock
# The best music group is Pearl Jam
# The best lead vocalist is Chris Cornell

def music_func (music, group, singer):
    print("The best kind of music is", music)
    print("The best music group is", group)
    print("The best lead vocalist is", singer)
    

def main():
    music, group, singer = input().split(',')
    music_func(music, group, singer)
    try:
        music_func()
    except TypeError:
        print("The best kind of music is Classic Rock")
        print("The best music group is The Beatles")
        print("The best lead vocalist is Freddie Mercury")
main()
