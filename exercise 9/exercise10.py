import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

# TODO: Use the glob.glob() function to obtain the list of filenames
# what does glob.glob do?
file_name = glob.glob(pattern)
print(file_name)

# # TODO: use os.path.getsize to find each file's size
# File  variable created:
for file_name in file_name:
    size = os.path.getsize(file_name)
    print(f"Size of '{file_name}' in bytes:", size)

# TODO: Add a test to only display files that are not zero length
# min_size = 0
# for file_name in file_name:
#     size = os.path.getsize(file_name)
# if size == min_size:
#     print("empty")
# elif
#     print(f"Size of '{file_name}' in bytes:", size)


# file_name = file_name
# for file_name in file_name:
#     size = os.path.getsize(file_name)
# and
#     size > 0
#     print(f"Size of '{file_name}' in bytes:", size)

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()

# ----------
# Question 2: Python programme emulating the high-street bank mechanism for checking a pin

# variables defined and values assigned
# correct username and password defined
correct_user = "paulene"
correct_pass = "1234"

# max login attempts defined
max_attempts = 3

# number of login attempts
attempts = 0

# user_input facing: request for username and password
# while loop. user_input/pass will be requested whilst the while statement is true (attempts is less than max attempts
# while attempts < max_attempts:
#     user_input = input("Enter your username: ")
#     pass_input = input("Enter your password: ")

# # check if the entered username and password are correct
# # conditions to define response to correct and incorrect information inputted
#     if user_input == correct_user and pass_input == correct_pass:
#         print("Access Granted")
# # if user_input and pass combination is correct, break the while loop
#         break
#     else:
#         attempts += 1
#         remaining_attempts = max_attempts - attempts
#         print(f"{remaining_attempts} attempts left")
# # if number max attempts have been reached, print 'blocked' message
# if attempts == max_attempts:
#     print("Your account has been blocked")

# Q3) Instead of input, use getpass.getpass in the same place in the program, the same parameters
import getpass

while attempts < max_attempts:
    user_input = input("Enter username: ")
    pass_input = getpass.getpass(prompt="Password", stream=None)

    # check if the entered username and password are correct
    # conditions to define response to correct and incorrect information inputted
    if user_input == correct_user and pass_input == correct_pass:
        print("Access Granted")
        # if user_input and pass combination is correct, break the while loop.
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"{remaining_attempts} attempts left")
# if number max attempts have been reached, print 'blocked' message
if attempts == max_attempts:
    print("Your account has been blocked")
