from ctypes import set_errno


axis = [['X',500],['Y',500],['Z',30000],['O', 400000],['L',500],['P',500]]
id = 'Y'
stepcount = 600

# print(axis[1][1])
# print(axis)

# for x in axis:
#     # if x[0] == 'Y':
#     #     print("the array contains the ID")
#     #     break
#     if x[1] <= 1000:
#         print('within bounds moving axis')
#     # print(x[1])

for x in axis:
    if x[0] == id: # find correct ID
        print('found correct id ' + id)
        if x[1] >= stepcount: # verify axis can move requested step ammount
            print(id + ' moving ' + stepcount + ' steps')
            print(True)
        else:
            print(id + ' axis unable to move, requested movement exceeds max step count of ' + str(x[1]) + ' steps for axis ' + id)
            print(False)
