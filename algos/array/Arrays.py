from utils import gcd
#TODO : ARRAYS 
def array_rotation(array=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
rotate_till_element=3):    
    # So take the gcd of Len. of array and elem. 
    # to rotate and make pairs, shift pairwise elements
    pairs= gcd(len(array),rotate_till_element)
    temp = array[0]  
    starting_posi = 0
    while(rotate_till_element>0):   
        temp = array[starting_posi]
        num = starting_posi
        try:
            while num < len(array):
                array[num]=array[num+pairs]
                num+=pairs
                print(num)
        except Exception as e:
            array[num]=temp
        starting_posi+=1
        rotate_till_element-=1
    return array


def reverse_array(array=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13]):
    for num in range(0, int(len(array)/2)):
        t = array[num]
        array[num] = array[(len(array)-1)-num]
        array[(len(array)-1)-num] = t    
    return array

def max_sum_of_k_consecutive_elements(array=[100, 200, 300, 400]):
    
    pass

if __name__=='__main__':
    function_name  = {
        'array_rotation':array_rotation,
        'reverse_array':reverse_array
    }
    inp = input()
    if inp not in function_name:
        raise Exception('Enter a valid functino')
    else:
        print('Result :',function_name[inp]())