import os
path=input('Please enter a path. ')
'''def diskUsage(path):
    total = os.path.getsize(path)
    for child in os.listdir(path):
        childPath = os.path.join(path, child)
        if os.path.isfile(childPath):
            total += os.path.getsize(childPath)
        elif os.path.isdir(childPath):
            total += diskUsage(childPath)
        print(str(os.path.getsize(childPath))+ '\t' +  childPath)
    return total

print (str(diskUsage(path)) + '\t'+ path)
'''



def diskUsage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for child in os.listdir(path):
            childPath = os.path.join(path, child)
            total+=diskUsage(childPath)
            print(str(os.path.getsize(childPath))+ '\t' +  childPath)
    return total
print(str(diskUsage(path)) + '\t'+ path)
