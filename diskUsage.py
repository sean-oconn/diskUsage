import os                   #importing os function
path=input('Please enter a path. ') # getting path input from user
def diskUsage(path):
    '''
    This function takes the input the user gave and
    returns the diskUsage used in each file of the provided path
    '''

    total = os.path.getsize(path)
    if os.path.isdir(path):
        for child in os.listdir(path):  #for loop that runs through the directories
            childPath = os.path.join(path, child)
            total+=diskUsage(childPath)
            print(str(os.path.getsize(childPath))+ '\t' +  childPath)  #formats and prints totals and name of the child path
    return total
print(str(diskUsage(path)) + '\t'+ path)  #prints total of all disk spaced used by path




