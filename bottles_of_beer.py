#=====================================================
#        ALGORITHMS - Friday, July 13, 2018
#=====================================================


#----------------------------------------------------------
# ALGORITHM 3: Bottles of Beer
#----------------------------------------------------------

# def get_drink_type(number):
#     if number % 7 == 0 and number % 5 == 0 and number > 0:
#         drink = 'Miller Lite'
#     elif number % 7 == 0 and number > 0:
#         drink = 'Miller'
#     elif number % 5 == 0 and number > 0:
#         drink = 'Lite beer'
#     else:
#         drink = 'beer'
#     return drink

# def bottles_of_beer(number):
#     while number > 0:
#         current_drink = get_drink_type(number)
#         next_drink = get_drink_type(number - 1)
#         template = '%d bottles of %s on the wall, take one down pass it around, %d bottles of %s on the wall'
#         print template % (number, current_drink, number - 1, next_drink)
#         number -= 1

# bottles_of_beer(99)

#----------------------------------------------------------
# ALGORITHM 3 (Bonus): Bottles of Beer
#----------------------------------------------------------

drinks = {
    (True, True): 'Miller Lite',
    (True, False): 'Miller',
    (False, True): 'Lite beer',
    (False, False): 'beer'
}

def bottles(num):
    for x in range(num, 0, -1):
        template = '%d bottles of %s on the wall, take one down pass it around, %d bottles of %s on the wall'
        print template % (x, drinks[(x % 7 == 0, x % 5 == 0)], x - 1, drinks[(x - 1 % 7 == 0, x - 1 % 5 == 0)])

bottles(99)
``