import os
try:
    list = []
    while True:
        list.append(int(input()))
except:
    pass
dp = dict()

def fun(posi):
    if list[posi] + (posi+1) >= len(list):
        result = []
        result.append(list[posi])
        return result
    else:
        next_element = posi+1
        last_element = posi+list[posi]      
        avl_steps = list[next_element : last_element+1]
        index_max_in_avl_list = list.index(max(avl_steps))        
        res = fun(index_max_in_avl_list)
        res.append(list[posi])
        return res
    
print(fun(0)[::-1])