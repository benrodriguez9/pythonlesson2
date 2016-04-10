# Lesson 3.2: Use Functions
# Mini-Project: Take a Break

# Write a program that prompts the user to take a break
# once every two hours, a maximum of three times.

# Use this space to describe your approach to the problem.
#
#
#
#

# Your code here.
import webbrowser
import time

num = 1
print('this loop started at ' +time.ctime())  
while num <= 3:
    time.sleep (7200)
    webbrowser.open("https://www.youtube.com/watch?v=cmC1srTBPWc")
    num = num+1
