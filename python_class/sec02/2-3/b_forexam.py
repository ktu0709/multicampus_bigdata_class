n_list= [[1,2,3 ],
         [4,5,6],
         [7,8,9]]

 #sublist  [1,2,3 ][4,5,6][7,8,9]
for sublist in n_list:
        print(f"sublist: {sublist}")
        for num in sublist:
            print(f"num: {num}")

'''
sublist: [1, 2, 3]
num: 1
num: 2
num: 3
sublist: [4, 5, 6]
num: 4
num: 5
num: 6
sublist: [7, 8, 9]
num: 7
num: 8
num: 9
'''