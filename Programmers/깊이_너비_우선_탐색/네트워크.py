def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    l = len(computers)
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            print(stack)
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            for i in range(0, l):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer