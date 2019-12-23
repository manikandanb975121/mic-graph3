from django.shortcuts import render
from django.http import HttpResponse
from . import script
from . import file_log

# Create your views here.

def home(request):
    #a = script.main()
    b = file_log
    list2 = file_log.list2
    #data2 = file_log.misp_list
    #print(data2)
    #for i in range(0,len(data2)):
        #print(data2[i])
        #print("\n")

    #data1 = file_log.graph_list
    #for i in range(0,len(data1)):
        #print(data1[i])
        #print("\n")

    #a = range(0,len(data1))
    #print(a)

    #print(len(list2))
    
    value = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    #value = len(data1[0])

    
    return render(request, 'events_2.html', {'data':list2})
    
