# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# the UEFA Euro 1988 Final

# assignment 1
# variable for every scoring player

scorer_name1= 'Ruud Gullit'
scorer_name2= 'Marco van Basten'

# assignment 2

goal_0= 32 #Time Goal 0
goal_1= 54 #Time Goal 1

# assignment 3
scorers = scorer_name1 + ' ' + str(goal_0) + ', ' + scorer_name2 + ' ' + str(goal_1)
print(scorers)

# Part 2
# assignment 4

# use f-strings for str
report = f'{scorer_name1} scored in the {goal_0}nd minute \n{scorer_name2} scored in the {goal_1}th minute'
print(report)

# assignment 1, 2, 3

player = 'Wim Kieft'
find_first_name= player.find(" ") 
first_name = player[:find_first_name]
print(first_name)

find_last_name= player.find(" ") #find space between first and surname
last_name= player[find_last_name+1:] # slice 
last_name_len= len(last_name)
print(last_name)
print(last_name_len)

# assignment 4

name_short = player[0]  + '. ' + last_name
print(name_short)

# assignment 5

chant_1= (first_name + "! ") * len(first_name) # first name times number characters name
chant= chant_1.rstrip()
print(chant) 

# assignment 6

good_chant= chant[-1] != " "
print(good_chant)






