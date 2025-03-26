# -*- coding: utf-8 -*-
import time
from time_password_checker import check_password

import statistics
class solution():
    def __init__(self) -> None:
        # DO NOT MODIFY THE EXISTED PROPERTY
        # You can add as many properties as you need
        self.password = ""                                              # This is where your guessed password is store
    
    def example(self):
        # The following shows how to get the time spent
        # You can modify it to test your ideas
        
        # If password is correct, check_password will return Correct
        # If password is wrong, check_password will return Wrong
        
        T1 = time.perf_counter()
        result = check_password(self.password)
        T2 = time.perf_counter()
        
        # You can print the output for debug or test.
        print(result)
        print("time spend: ", T2-T1)
        
        
              
    def median(self, password_guess):
        times = []
        for i in range(500):
            start = time.perf_counter()
            result = check_password(password_guess)
            if result == "Correct":
                return None, result
            end = time.perf_counter()
            times.append(end - start)
        
        return statistics.median(times), result

    def find_next_char(self, current_prefix):
        max_time = 0
        next_char = None
        
        for char in range(33, 127):
            guess = current_prefix + chr(char)
            time_taken, result = self.median(guess)
            
            if result == "Correct":
                return chr(char), True
            
            if time_taken > max_time:
                max_time = time_taken
                next_char = chr(char)
                
        return next_char, False

    def getPassword(self):
        current_password = ""
        
        while len(current_password) < 11:
            next_char, found_password = self.find_next_char(current_password)
            current_password += next_char
            
            if found_password:
                break
                
        self.password = current_password
        return self.password
        
       # How this code works is that I loop finding the next char and if the password is correct for
       # the first 11 characters, if it is correct or the password is 11 characters long, I return
       # the current password.
       # find next char iterates through every single valid character, returning if the password is correct,
       # or returning the character that resulted in the longest compute time
       # median just returns the median compute time for every character, and whether or not that password returned 
       # the correct guess.
       
                
                
            
        # Please complete this method
        # It should be the return the correct password in a string
        # GradeScope will import your class, and call this method to get the password you calculated.

# Write Up
# Please explain your solution