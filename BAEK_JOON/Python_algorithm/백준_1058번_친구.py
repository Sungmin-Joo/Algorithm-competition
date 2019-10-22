import sys
input=sys.stdin.readline

if __name__ == "__main__":
    num = int(input())
    fnd = [[] for i in range(num)]
    no_fnd = [[] for i in range(num)]
    fnd_second = [[] for i in range(num)]
    for i in range(num):
        for idx, v in enumerate(input()):
            if v == 'Y' :
                fnd[i].append(idx)
            elif v == 'N' and i != idx:
                no_fnd[i].append(idx)
    for idx, v in enumerate(no_fnd):
        for name in v:
            if len(set(fnd[name]) - set(fnd[idx])) != len(fnd[name]):
                fnd_second[idx].append(name)
    m = 0
    for i in range(num):
        if m < len(fnd[i] + fnd_second[i]):
            m = len(fnd[i] + fnd_second[i])
    print(m)
