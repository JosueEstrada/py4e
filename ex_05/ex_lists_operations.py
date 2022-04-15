# Original code from Youtube comment
# https://youtu.be/9Wtqo6vha1M
while True:
    question = input(
        "you need to type a list before typing a list please choose a tool "
        "the following tools are \nfinding smallest number among your list to "
        "do that type smallest\nfinding biggest number among your list to do "
        "that type biggest\nfinding average of your list to do that type "
        "average \ncounting the list to do that type count \nadding "
        "everything to do that type add\nsearching in list for conformation "
        "to do that type search >>> ")
    if question == 'smallest':
        break
    elif question == 'biggest':
        break
    elif question == 'average':
        break
    elif question == 'count':
        break
    elif question == 'add':
        break
    elif question == 'search':
        break
    else:
        print("please type a tool")
if question == 'biggest':
    try:
        lit = input("type a list here to find the biggest number\n>>> ")
        reallist = list(map(int, lit.split()))
        nothinghere = None
        final = "the greatest number among your list is"
    except:
        lit = 'this is not even a full number please type a number list'
        nothinghere = ' '
        value = ' '
        reallist = ' '
        final = ' '
        print(lit, reallist, nothinghere, value)

    for value in reallist:
        if nothinghere is None:
            nothinghere = value
        elif nothinghere < value:
            nothinghere = value
    print(final, nothinghere)
elif question == 'smallest':
    try:
        lit = input("type a list here to find the smallest number\n>>> ")
        reallist = list(map(int, lit.split()))
        nothinghere = None
        final = "the smallest number among your list is"
    except:
        lit = 'this is not even a full number please type a number list'
        nothinghere = ' '
        value = ' '
        reallist = ' '
        final = ' '
        print(lit, reallist, nothinghere, value)

    for value in reallist:
        if nothinghere is None:
            nothinghere = value
        elif nothinghere > value:
            nothinghere = value
    print(final, nothinghere)
elif question == 'average':
    try:
        lit = input("type a list here to find the average of your list \n>>> ")
        reallist = list(map(int, lit.split()))
        count = 0
        sum = 0
        final = "the average of your list is"
    except:
        lit = 'this is not even a full number please type a number list'
        reallist = ' '
        value = ' '
        count = ' '
        sum = ' '
        final = ' '
    try:
        for value in reallist:
            count = count + 1
            sum = sum + value
    except:
        lit = 'this is not even a full number please type a number list'
        print(lit)

    average = count + sum
    print(final, average)
elif question == 'count':
    try:
        lit = input("type a list here to find the count of your list \n>>> ")
        reallist = list(map(int, lit.split()))
        count = 0
        final = "the count of your list is"
        for value in reallist:
            count = count + 1
        print(final, count)

    except:
        lit = 'this is not even a full number please type a number list'
        nothinghere = ' '
        value = ' '
        reallist = ' '
        final = ' '
        print(lit, reallist, nothinghere, value)
elif question == 'add':
    try:
        lit = input("type a list here to find the sum of your list \n>>> ")
        reallist = list(map(int, lit.split()))
        sum = 0
        final = "the sum of your list is"
        for value in reallist:
            sum = sum + value
        print(final, sum)

    except:
        lit = 'this is not even a full number please type a number list'
        nothinghere = ' '
        value = ' '
        reallist = ' '
        final = ' '
        print(lit, reallist, nothinghere, value)
elif question == 'search':
    lit = input("type a list here to find the integer of your list \n>>> ")
    searchinteger = input("search your integer here\n>>> ")
    reallist = lit.split()
    foundithuh = searchinteger in reallist
    if foundithuh == False:
        print("sorry your integer that you searched is not found")
    elif foundithuh == True:
        print("your integer that you searched is found in the list")
