
file = open('input.txt', "rt")
nums = ['1','2','3','4','5','6','7','8','9','one','two','three','four','five','six','seven','eight','nine']
bwnums = ['1','2','3','4','5','6','7','8','9','eno','owt','eerht','ruof','evif','xis','neves','thgie','enin']
keys = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9',
        'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9',
        'eno':'1','owt':'2','eerht':'3','ruof':'4','evif':'5','xis':'6','neves':'7','thgie':'8','enin':'9'}
total = 0
for line in file:
    print(line)
    x=line
    y=line[::-1]
    x_positions = {}
    y_positions = {}

    #find first digit
    for num in nums:    
        loc = x.find(num)
        if loc != -1:
            x_positions.update({loc:num})

    #find last digit
    for num in bwnums:    
        loc = y.find(num)
        if loc != -1:
            y_positions.update({loc:num})   
    
    first_loc = 1000
    last_loc = 1000
    for key in x_positions:
        if key < first_loc:
            first_loc = key
    
    for key in y_positions:
        if key < last_loc:
            last_loc = key

    first_digit = x_positions.get(first_loc)
    second_digit = y_positions.get(last_loc)

    first_digit = keys.get(first_digit)
    second_digit = keys.get(second_digit)

    res = int(first_digit+second_digit)
    print(res)
    total += res
    print(total)

print(total)
file.close() 