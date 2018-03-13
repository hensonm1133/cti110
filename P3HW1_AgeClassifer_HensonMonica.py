# CTI-110-0902
# P3HW1 - Age Classifer
# Monica Henson
# 12 March 2018
#

# Get the age of the person.
Age = int(input('Enter your age:'))

# Determine which age group the person is in.
if Age <= 1:
    print ('User is infant.')
if 1 < Age < 13:
    print ('User is a child.')
if 13 <= Age < 20:
    print ('User is a teenager.')
if Age >= 20:
    print ('User is an adult.')
