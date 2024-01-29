# # retrieve getpass function from getpass module
# from getpass import getpass
#
# my_password = getpass("Enter Password: ")
# # display how many characters
# print(len(my_password))

# importing the getpass module
import getpass

# using the getpass() function
my_pass = getpass.getpass(prompt='Input the Password:')
# using the if-else conditional statements
if my_pass == 'Admin':
    print('The key is Unlocked!')
else:
    print("You've entered an invalid password!")