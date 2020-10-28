from django.shortcuts import render
from .methods import *
# Create your views here.
def billinfoview(request):
    return render(request,'EB/front.html',{})

def processingview(request):
    if(request.method == 'POST'):
        DataReceived = [
            Data("Fan",int(request.POST['fanT']),int(request.POST['fanQ']),request.POST['restrictionFan']),
            Data("TubeLight",int(request.POST['tubelightT']),int(request.POST['tubelightQ']),request.POST['restrictionTube']),
            Data("Bulb",int(request.POST['bulbT']),int(request.POST['bulbQ']),request.POST['restrictionBulb']),
            Data("TV",int(request.POST['TVT']),int(request.POST['TVQ']),request.POST['restrictionTV']),
            Data("Laptop",int(request.POST['laptopT']),int(request.POST['laptopQ']),request.POST['restrictionLaptop']),
            Data("Mobile",int(request.POST['mobileT']),int(request.POST['mobileQ']),request.POST['restrictionMobile']),
            Data("Fridge",int(request.POST['fridgeT']),int(request.POST['fridgeQ']),request.POST['restrictionFridge']),
        ]
        cost = calculatePrice(DataReceived)
        target = float(request.POST['target'])
        if(cost >= target):
            print(cost)
            return render(request,'EB/limit.html',{'cost':cost,'target':target})
        solution = getSolution(DataReceived,cost,target)
        data = {
            'DataList' : solution,
            'length' : len(solution),
            'count' : 1,
        }
        #print(len(DataReceived))
        #printData(solution)
        return render(request,'EB/present.html',data)
        
    return render(request,'EB/limit.html',{})