import sys

#inf = open('input.txt');
inf = sys.stdin 

T = inf.readline();


for t in range(0, int(T)):
    count = dict()
    N = inf.readline()
    #print(str(N))
    #print('----------------------')
    
    split_num = inf.readline().split()
    #print(split_num)
    
    for i in range(0,int(N)):
        count[split_num[i]] = count.get(split_num[i],0) + 1
    temp_xor = [num for num, num_count in count.items() if num_count%2 == 1]
    #print(temp_xor)
    N = None
    
    for i in temp_xor:
        if N == None:
            N = int(i)
        else:
            N = N^int(i)

    Answer = N
    print('Case #%d' %(int(t)+1))    
    print(Answer)

inf.close()