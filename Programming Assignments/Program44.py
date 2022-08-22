# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: November 16, 2021
# Programming Assignment #44

""" printUTAs(utaList) prints out every UTA on the list of UTAs alphabetically, one per line """
def printUTAs(utaList):
    print("UTA List: ")
    utaList.sort() 
    for uta in utaList:
        print(uta)
  
""" isUTA(utaList, person) checks if the person in question is a UTA on the list and prints out a message accordingly """     
def isUTA(utaList, person):    
    isUTA == False
    for uta in utaList:
        if uta == person:
            isUTA == True
            
    if not isUTA:
        print(person + " is a UTA for CSci 127 Fall 2021.")
    else:
        print(person, "is not a UTA for CSci 127 Fall 2021.")
        
""" numUTAs(utas) return a string with how many UTAs are working this semester """                
def numUTAs(utas):
    num = len(utas)
    return "There are " + str(num) + " UTAs who love helping students in CSci 127 Fall 2021."


def main():
    # A list of UTAs working this semester
    utas = ["Mandy", "Leonardo", "Nancy", "Ifte", "Aida", "Arterio", "Destiny", "Ghazanfar", "Ilya", "Sadab", "Stephanie","Tyler"]
    printUTAs(utas)
    
    isUTA(utas, "Lola")
    isUTA(utas, "Mandy")          
    isUTA(utas, "Leonardo")
    isUTA(utas, "Yash")
    
    print(numUTAs(utas))

    
if __name__ == '__main__':
    main()