#=====================================================
#        ALGORITHMS - Friday, July 13, 2018
#=====================================================

#-----------------------------------------------------
# ALGORITHM 1: Smallest Divisable
#-----------------------------------------------------

def increase_counter(current_max, range_max):
    for i in range(range_max, 2, -1):
        if current_max % i != 0:
            return True
    return False
    
def get_result(number):
    max_number = number
    done = False
    while not done:
        if increase_counter(max_number, number):
            max_number += number
        else:
            done = True
    return max_number
    
result = get_result(20)
print 'Result is %d.' % result