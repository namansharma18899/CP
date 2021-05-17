#!/usr/bin/env pypy
class Events():
    def __init__(self,start_time:int,end_time:int):        
        self.start_time,self.end_time = int(start_time),int(end_time)
    def __repr__(self):
        return str((self.start_time, self.end_time))
        
def  calculate_max_events(arr):
    if len(arr)==0:
        return 0
    sorted_arr = sorted(arr,key=lambda x : int(x.end_time))
    max_events = 1
    prev_end_time = sorted_arr[0].end_time    
    for i in range(0,len(sorted_arr)):
        if sorted_arr[i].start_time>=prev_end_time:
            prev_end_time = sorted_arr[i].end_time
            max_events+=1
    return max_events
    
test_cases = int(input())
result = list()
inputs = {}
while(test_cases > 0):
    test_cases-=1
    num_of_events=(int(input()))               
    arr = list() 
    for i in range(0,num_of_events): 
        start_time ,end_time = input().split(' ')
        arr.append(Events(start_time,end_time))
    inputs[num_of_events] = arr
for k,v in inputs.items():        
    result.append(calculate_max_events(v))
for each in result:
    print(each)