class Data:
    def __init__(self,Name,MinTime,quantity,restrict):
        self.name = Name
        self.quantity = quantity
        self.time = MinTime
        self.powerRating = PowerRatingData[self.name][0]
        self.restrict = restrict
        self.onTime = PowerRatingData[self.name][1]


PowerRatingData = {
    "Fan" : (75,1),
    "Bulb" : (20,1),
    "LED TubeLight" : (20,1),
    "LED Bulb" : (20,1),
    "TubeLight" : (40,1),
    "Laptop" : (65,2),
    "TV" : (50,1),
    "LED TV" : (60,1),
    "Mobile" : (35,2),
    "Fridge" : (200,2)
 }

CostPerUnit = 8    
DifferentCombinations = []

def printData(data):
    for item in data:
        for appliance in item[0]:
            print(appliance.name,appliance.time)
        print(round(item[1],2))
        print("________________________________________")

def calculatePrice(data):
    cost = 0
    for item in data:
        cost += (item.powerRating  * item.time *  CostPerUnit * 30 * item.quantity)/1000
    return cost

def getCost(PowerRating,Time,quantity):
    return round(((PowerRating * Time * CostPerUnit * 30 * quantity) /1000),2)

def check(cost,target):
    pass

def timeRequired(RemainingPrice,PowerRating):
    return round(RemainingPrice / ((PowerRating/1000) * CostPerUnit *30),2)

def createList():
    pass

def backtrack(data,cost,target,index=0):
    #cost = calculatePrice(data)
    if( cost >= target ):
        DifferentCombinations.append((list(data),cost))
        return

    if(index >= len(data)):
        if(cost>=target-100 and cost<=target+100):
            DifferentCombinations.append((list(data),cost))
        return
    #We try every combination of time allotment to every appliance to suggest best possible
    #combinations and let choose user the best one suits to him/her
    appliance = data[index]

    #Every Remaining appliance has fixed length of time for which it is going to be used
    #So just return the solution
    if(appliance.restrict == "high"):
    #    return
        #print("High",appliance.name)
        newData = []
        for i in range(len(data)): 
           newData.append(Data(data[i].name,data[i].time ,data[i].quantity,data[i].restrict)) 
        backtrack(newData,cost,target,index+1)

    elif(appliance.restrict == "medium"):
        #print("Medium",appliance.name)
        #Try making combinations with every hour to get possible combination within range
        #iterateLength = -1 * appliance.onTime
        #for  hour in range(19-appliance.time,appliance.onTime,iterateLength):
        for  hour in range(appliance.onTime,19-appliance.time,appliance.onTime):
            newCost = cost + getCost(appliance.powerRating,hour,appliance.quantity)
            #print(newCost,appliance.name)
            #print(hour,appliance.name)
            if(hour == 18-appliance.time):
                DifferentCombinations.append((list(data),cost))
                return
            if(newCost < target):
                #newData = data.copy() 
                newData = []
                for i in range(len(data)):
                    if(i == index):
                        newData.append(Data(data[i].name,data[i].time + hour,data[i].quantity,data[i].restrict)) 
                    else:
                        newData.append(Data(data[i].name,data[i].time ,data[i].quantity,data[i].restrict))
                
                #data[index].time = tempTime
                #print(newData[index].time,data[index].time)
                backtrack(newData,newCost,target,index+1)

            else:
                #if(cost <= target+5 and cost >= target-5):
                if(cost > target-100 and cost < target+100):
                    DifferentCombinations.append((list(data),cost))
                return 
    else:
        
        #Try making combinations with every hour to get possible combination within range
        #iterateLength = -1 * appliance.onTime
        #for  hour in range(25-appliance.time,appliance.onTime,iterateLength):
        for  hour in range(appliance.onTime,25-appliance.time,appliance.onTime):
            #print("Low",appliance.name)
            newCost = cost + getCost(appliance.powerRating,hour,appliance.quantity)
            #print(newCost,appliance.name)
            #print(hour,appliance.name)
            if(hour == 24-appliance.time):
                if(cost <= target+100 and cost >= target-100):
                    DifferentCombinations.append((list(data),cost))
                return
            if(newCost < target):
                #newData = data.copy() 
                newData = []
                for i in range(len(data)):
                    if(i == index):
                        newData.append(Data(data[i].name,data[i].time + hour,data[i].quantity,data[i].restrict)) 
                    else:
                        newData.append(Data(data[i].name,data[i].time ,data[i].quantity,data[i].restrict))
                
                #data[index].time = tempTime
                #print(newData[index].time,data[index].time)
                backtrack(newData,newCost,target,index+1)
            else:
                #if(cost <= target+5 and cost >= target-5):
                if(cost<=target+100 and cost>=target-100):
                    DifferentCombinations.append((list(data),cost))
                return 
    #print(appliance.time,appliance.name)

def printRestrict(data):
    for item in data:
        print(item.restrict,item.name)
    
def printInput(data):
    for item in data:
        print(item.name,item.restrict)
    

def filter(data):
    lowData = []
    mediumData = []
    highData = []
    for item in data:
        if(item.quantity == 0):
            continue
        if(item.restrict == "high"):
            highData.append(item)
        elif(item.restrict == "medium"):
            mediumData.append(item)
        else:
            lowData.append(item)
    lowData.reverse()
    data = highData + mediumData + lowData
    #printRestrict(data)
    return data

def selectBest(data):
    listLength = 10
    if(len(data) < 10):
        listLength = len(data)
    return data[:10]

def convertBestDict(data):
    data = selectBest(data)
    solution = []
    count = 1
    for item in data:
        lis = []
        for appliance in item[0]:
            context = {
                "name" : appliance.name,
                "time" : appliance.time,
            }
            lis.append(context)
        solution.append({ "items" : lis,"cost" : round(item[1],2),"count" : count})
        count += 1
    return solution

def getSolution(data,cost,target):
    data = filter(data)
    
    DifferentCombinations.clear()
    #printInput(data)
    backtrack(list(data),cost,target,0)
    if(len(DifferentCombinations) == 0):
        DifferentCombinations.append((list(data),cost))
    solution = convertBestDict(DifferentCombinations)
    return solution