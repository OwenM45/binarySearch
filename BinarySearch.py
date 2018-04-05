#loops the program infinetly
while True:
    #read file
    inputFile = open("DATA.txt","r")

    #splits the file lines into an array
    data = inputFile.readlines()

    #counts how many times it loops through the list
    loops = 0

    #sets the num to find to the user input
    print("---------------------------")
    numToFind = int(input("what number would you like to find \n"))

    #counts the number of splits
    numSplits = 1

    #function that splits the list in half 
    def split(listToSplit, indexF):
        #tells the function that numsplits
        global numSplits
        line = []
        #checks to make sure that the remaining list is more than one
        if len(listToSplit) > 1:
            #checks if the list is uneven then splits the list accordingly
            if len(listToSplit) % 2 != 0:
                split1 = listToSplit[0:int((len(listToSplit)//2)+1)]
                split2 = listToSplit[int(len(listToSplit)//2+1):int(len(listToSplit))]
                #print(str(split1) + "----" + str(split2))
            else:
                #splits the list in half because it is even
                split1 = listToSplit[0:int(len(listToSplit)/2)]
                split2 = listToSplit[int(len(listToSplit)/2):int(len(listToSplit))]
                #print(str(split1) + "----" + str(split2))
            #sets up the variable that will be passed into the find num function
            line = [split1,split2]
            #calls findnum
            findNum(line, indexF)
            #counts the number of splits to complete the search
            numSplits += 1
        else:
            #tells the user if no match is found
            print("no match found")

    def findNum(splits, indexF):

        #sets the variable that keeps track of the index
        indexFo = indexF

        #sets the two arrays
        split1 = splits[0]
        split2 = splits[1]

        #checks if the first value of the second array is the same as the num to find
        if int(split2[0]) == numToFind:
            indexFo += len(split1)
            print("num index:" + str(indexFo) + "\n" + "it took " + str(numSplits) + " splits to find")
        #checks if the first value of the second array is less than the num to find
        elif int(split2[0]) < numToFind:
            indexFo += len(split1)
            split(split2, indexFo)
        #checks if the last value of the first array is the same as the num to find
        elif int(split1[len(split1)-1]) == numToFind:
            print("num index:" + str(indexFo + len(split1)-1) + "\n" + "it took " + str(numSplits) + " splits to find \n")
        #checks if the last value of the first array is more than the num to find
        elif int(split1[len(split1)-1]) > numToFind:
            split(split1, indexFo)
        else:
            #prints if the num to find does not exist within the array
            print("no match found")
        
        
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
                    #print(nums)
                    break
                #if not restart the loop
                else:
                    i = -1
                    ordered = True
            #iterate the loop
            i += 1
        
        found = False
        
        split(nums, 0)
        
        
                
                
            





            

