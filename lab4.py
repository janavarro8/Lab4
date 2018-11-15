"""
Course: CS2302 Data Structures
Author: Javier Navarro
Assignment: Option B
Instructor: Diego Aguirre
TA: Manoj Saha
Last modified: 11/14/18
Purpose: Improve running time of lab 3
"""
import ChainingHashTable

def main():
    fileName = ""       #holds user input of file name
    userInput = ""      #holds user input for anagrams
    validInput = False  #used for confirming user input is valid
    
    while(validInput == False):
        try:
            fileName = input("Enter the name of the file you would like to use:")
            numLines = number_of_lines(fileName)
            print()
            print("There are ", numLines, " elements in ", fileName)
            validInput = True       #will allow the loop to be exited
        except FileNotFoundError:   #forces loop if exception is caught
            print("File not found. Try again.")
    
    tableSize = numLines // 2       #allows for search to have avg of 1 comparison
    table = ChainingHashTable.ChainingHashTable((tableSize))    #creates hash table
    
    create_hash_table(table, fileName)
    
    userInput = input("Enter a word to find anagrams for:")
    
    print()
    print("Anagrams for '", userInput, "':")
    userInput = userInput.lower()
    print_anagrams(userInput, table)
    
    print()
    avg_comparisons(table, fileName, numLines // 2)
    
    print()
    load_factor(numLines, tableSize)

#counts and returns number of lines in the given file
def number_of_lines(fileName):
    count = 0   #keeps count of lines
    with open(fileName, "r") as file:
        for i in file:
            count += 1
    return count

#populates the table with the elements in the given file
def create_hash_table(table, fileName):
    with open(fileName, "r") as file:       #opens file with given fileName
        for i in file:                      #i holds each line in the file
            line = i.split()                
            line[0] = line[0].lower()       #set to lower to compare with words in caps
            table.insert(line[0])           #inserts the line into hash table

#prints the anagrams for a given word from a given table
def print_anagrams(word, table, prefix = ""):
    if len(word) <= 1:
        str = prefix + word
        
        if(table.search(str) != None):   #looks for str in the tree
            print(str)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur
            
            if cur not in before: # Check if permutations of cur have not been generated.
                print_anagrams(before + after, table, prefix + cur)

#prints the average number of comparisons it takes to find a word
def avg_comparisons(table, fileName, numElements):
    numComparisons = [0]        #will add up the total comparisons
    numComparisons[0] = 0
    count = 0                   #keeps track of how many elements seen
    
    print("Using the first ", numElements, " elements from ", fileName, " to calculate average...")
    
    with open(fileName, "r") as file:
        for i in file:
            if(count > numElements):        #exits for loop at given size
                break;
            numComparisons[0] += table.search_comparisons(i.split()[0].lower()) #adds the number of comparisons for a given word
            count += 1
    
    print()
    print("The average number of comparisons needed for the retrieve operation:")
    print(numComparisons[0] // count)       #prints the average number of comparisons
    
#prints the load factor of the hash table
def load_factor(elemCount, tableSize):
    loadFactor = elemCount / tableSize      #equation for load factor
    print("The load factor for the hash table is", loadFactor)

main()