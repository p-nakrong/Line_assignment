
#python 3
n = int(input()) #No of element
inp = str(input()) #The elements of array
list_inp = inp.split(' ')
list_inp[:] = list(map(int, list_inp))
cnt_element = [0]*100
max_count = 0
ans_major = -1
for i in list_inp:
    cnt_element[i-1] = cnt_element[i-1] + 1
    if( cnt_element[i-1] >= max_count):
        max_count = cnt_element[i-1]
        ans_major = i
        
if(max_count > n//2):
    print(ans_major)
else:
    print(-1)
