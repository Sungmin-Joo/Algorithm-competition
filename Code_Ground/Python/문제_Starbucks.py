import sys

#inf = open('sample_input.txt');
inf = sys.stdin 

T = inf.readline();

for t in range(0, int(T)):
    
    Answer=0;
    
	#############################################################################################
	#
	#  Implement your algorithm here.
	#  The answer to the case will be stored in variable Answer.
	#
	#############################################################################################
	
	# Print the answer to standard output(screen).
    [N, M, K] = inf.readline().split() #개행문자 제거
    table = dict()
    Money = 0
    flag = 0
    for i in range(int(N)):
        temp_N = inf.readline().rstrip('\n')
        table[temp_N] =  table.get(temp_N,0) + 1
    for i in range(0,int(M)):
        try:
            Money += table[str(i+1)] * int(inf.readline())
        except:
            buffer = inf.readline()
        if Money > int(K):
            if flag == 1:
                pass
            else:
                Answer = 'N'
                flag = 1
        else:
            if flag == 1:
                pass
            else:
                Answer = 'Y'
    print('Case #%d' %(int(t)+1))    
    print(Answer)
inf.close()