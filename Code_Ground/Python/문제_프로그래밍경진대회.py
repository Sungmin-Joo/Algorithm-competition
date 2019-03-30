import sys
#inf = open('sample_input.txt');
inf = sys.stdin 
T = inf.readline();
for t in range(0, int(T)):
    competition_N = []
    N = int(inf.readline())
    Answer = 0
    for i in range(0,N):
        competition_N.append(int(inf.readline()))
    competition_N.sort()
    max_num = 0
    for i in range(0,N):
        if competition_N[i] + (N - i) >= max_num:
            max_num = competition_N[i] + (N - i)
    for i in range(0,N):
        if competition_N[i] + N >= max_num:
            Answer += 1
    print('Case #%d' %(int(t)+1))    
    print(Answer)

inf.close()