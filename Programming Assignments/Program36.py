# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: November 4, 2021
# Programming Assignment #36

def worldRecord(gender, event):
     """
     Write a function worldRecord(), that takes two parameters: gender (string) and the event type (int). 
     The function should return a float for the Olympic world record for the event. 
     
     Men's Standard, event type 100 meters: record is 9.36 seconds.
     Men's Standard, event type 200 meters: record is 19.30 seconds.
     Men's Standard, event type 400 meters: record is 43.03 seconds.
     Women's Standard, event type 100 meters: record is 10.62 seconds.
     Women's Standard, event type 200 meters: record is 21.34 seconds.
     Women's Standard, event type 400 meters: record is 48.25 seconds.
     Return -1 for any other value
     """
     
     time = 0.0
     if gender == "men" and event == 100:
        return 9.63
     if gender == "men" and event == 200:
        return 19.30
     if gender == "men" and event == 400:
        return 43.03
     if gender == "women" and event == 100:
        return 10.62
     if gender == "women" and event == 200:
        return 21.34
     if gender == "women" and event == 400:
        return 48.25
     else:
         return -1
    
     
     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### this is the only section    ###
     ### you change in this program. ###
     ###################################

     return(time)

def main():
     z = input('Enter the gender: ').lower()
     t = int(input('Enter the event distance: '))
     record = worldRecord(z,t)
     print("The record for "+z+" 's "+ str(t) + " meters is", record)

#Allow script to be run directly:
if __name__ == "__main__":
     main()