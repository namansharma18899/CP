def gcd(num1,num2):
    i = 2
    while (i <= max(num1,num2)):
        if num1%i == 0 and num2%i==0:
            return i
        i+=1
    return 1

def sort_objects(list_of_objects: list, sorting_for):
    
    pass