#read file
inputFile = open("DATA.txt","r")

#splits the file lines into an array
data = inputFile.readlines()

#counts how many times it loops through the list
loops = 0

#sets the num to find to the user input
numToFind = int(input("what number would you like to find \n"))

indexFound = 0

def split(listToSplit):
    line = []
    if len(listToSplit) > 1:
        if len(listToSplit) % 2 != 0:
            split1 = listToSplit[0:int((len(listToSplit)//2)+1)]
            split2 = listToSplit[int(len(listToSplit)//2+1):int(len(listToSplit))]
        else:
            split1 = listToSplit[0:int(len(listToSplit)/2)]
            split2 = listToSplit[int(len(listToSplit)/2):int(len(listToSplit))]
        line = [split1,split2]
        findNum(line)
    else:
        print("no match found")    

def findNum(splits):

    global indexFound
       
    split1 = splits[0]
    split2 = splits[1]

    if int(split1[len(split1)-1]) == numToFind:
        print(indexFound)
    elif int(split1[len(split1)-1]) > numToFind:
        #indexFound += len(split1)
        split(split1)
    if int(split2[0]) == numToFind:
        print(indexFound)
    elif int(split2[0]) < numToFind:
        indexFound += len(split1)
        split(split2)
                   
#loops through the lines
for line in data:

    indexFound = 0
    
    #splits the line into a list
    nums = line.split()

    #variable that checks if the list is sorted
    ordered = True

    #counter for while loop
    i = 0

    #loops through the list of numbers
    while i < len(nums):

        #try catch to find the end of the num list
        try:
            #checks if the first of the 2 is greater than the first 
            if int(nums[i]) > int(nums[i+1]):
                
                #sets temp variables for the first and second num
                firstNum = nums[i]
                secondNum = nums[i+1]

                #swaps the positions
                nums[i] = secondNum
                nums[i+1] = firstNum

                #sets ordered to false so the computer knows to loop again
                ordered = False                
        #checks if the list has ended        
        except:
            #adds one to loop 
            loops += 1
            #if its ordered print the result and break the loop
            if ordered == True:
                print(nums)
                break
            #if not restart the loop
            else:
                i = -1
                ordered = True
        #iterate the loop
        i += 1

    found = False
    
    split(nums)
    
    
            
            
        





        
