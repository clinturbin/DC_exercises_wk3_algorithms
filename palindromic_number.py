#=====================================================
#        ALGORITHMS - Friday, July 13, 2018
#=====================================================

#-----------------------------------------------------
# ALGORITHM 2: Palindromic Number
#-----------------------------------------------------

def get_largest_palindrome(number):
    for i in range(number, 0, -1):
        for j in range(number, 0, -1):
            if is_palindrome(i * j):
                return i * j

def is_palindrome(number):
    str_number = str(number)
    length = len(str_number)
    reverse_str = ''
    for i in range(length, 0, -1):
        reverse_str += str_number[i-1]
    return str_number == reverse_str


number = 999
max_palindrome = get_largest_palindrome(number)

print "highest palindrom number is: %d" % max_palindrome