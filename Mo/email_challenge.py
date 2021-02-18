# You run a startup media company called Ripple Media
# It's typical when you hire a new employee in your company, to setup an email id for them

print('Question 1')
print('--------------------------------------------------------------')
employee_name = 'Ash Rahman'

# You have decided the format of the email should be: Ash Rahman -> ash.rahman@ripplemedia.com

# Let's write some code that converts a name into an email id that matches this format

# 1.1 TODO: Let's save the lowercase version of the employee_name in a new variable 'lower_name'

############ to print a variable in all lower case laters i need to use the .lower function  ###############
lower_name = employee_name.lower()
print(lower_name)

# 1.2 TODO: We want to separate the first name and last name and save it in a variable 'names_list'

############ to separate item from a list i need to use the .split() function ###############
names_list = lower_name.split(' ')
print(names_list)

# 1.3 TODO: We want to join the first name and last name with a '.' and save it in a variable called 'joined_names'

############ to join items in a list i need to use the ('').join(variable) function ###############
joined_names= ('.').join(names_list)
print(joined_names)

# 1.4 TODO: We want to add '@ripplemedia.com' to the end of the string inside joined_names and save it in a variable 'email'
email = joined_names + '@ripplemedia.com'
print(email)
print('--------------------------------------------------------------')
print()

print('Question 2')
print('--------------------------------------------------------------')
# Congratulations! Your team is expanding. Below is a list of their names:
names = ['Max Bartlett', 'Angelita Norris', 'Stewart Mueller', 'Dominique Henry', 'Carmela Gross', 'Bettie Mcmillan', 'Sara Ellison', 'Ira Anthony', 'Pauline Riley', 'Ben Weber',
         'Joanne Mcknight', 'Loren Gould', 'Jamar Singh', 'Amanda Vance', 'Tyrell Andrade', 'Jana Clements', 'Eddy Mcbride', 'Marsha Meyer', 'Elbert Shannon', 'Alyce Hull']

emails = []

# We want to convert all their names into the same format from Question 1

# 2.1 TODO: Use a "for" loop to go over each name in the names list
# 2.2 TODO: Inside the "for" loop, create the email id by re-using the logic from Question 1 and...
# 2.3 TODO: ..add the email to the emails list

# Notes:
############ to 'iterate' or do something for items in a list all at once we can use loops. ###############
############ Creating a loop we can tell the loop to execute specified commands for the list instead of individually modifying each item which can be cumbersome. ###############
############ i need to use the "for (userdefinedvariable) in (list)" command to create a loop for my list  ###############
############ for questions 2 i will need to apply the same procedure in a question in 1 for multiples items   ###############


for employee_email in names:
    lower_name = employee_email.lower()
    names_list = lower_name.split(' ')
    joined_names = ('.').join(names_list)
    email = joined_names + '@ripplemedia.com'
    emails.append(email)
print(emails)
print('--------------------------------------------------------------')
print()