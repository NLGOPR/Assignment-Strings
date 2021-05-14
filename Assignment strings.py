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

goal_1= 32 #Time Goal 1
goal_2= 54 #Time Goal 2

# assignment 3
# combine str and int
scorers = scorer_name1 + ', ' + str(goal_1) + ', ' + scorer_name2 + ', ' + str(goal_2) + '.' 
print (scorers)

# Part 2
# assignment 4

# use f-strings for str
report = f"{scorer_name1} scored in the {goal_1}nd minute. \n{scorer_name2} scored in the {goal_2}th minute."
print (report)


# assignment 1, 2, 3

player = 'Wim Kieft'
first_name = player [:3]
#print (first_name)
last_name = player[4:]
print (last_name)
print (last_name, len(last_name))

# assignment 4

name_short = player[0]  + '. ' + last_name
print (name_short)

# assignment 5 

#chant = (first_name +'!\t')  * len(first_name) # chant after goal
#print (chant)

# assignment 6
# I do not understand the question!

chant2 = (first_name +'! ')  * len(first_name) # chant after goal
print (chant2)

#stripping white space last character
good_chant = (first_name +'! ')  * len(first_name) # chant after goal
print (good_chant.rstrip()) # without space last character

result = chant2 != good_chant
print (result)

# The result seems to be the same but the last output did not has an extra space character
# I do not understand why it's False


