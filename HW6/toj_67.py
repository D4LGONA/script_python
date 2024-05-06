
n = eval(input())
chart = input()
graph = ['.' * n]
cnt = 0

for i in range(len(chart)):
    if chart[i] == '+':
        if i == 0:
            graph[cnt] = '/' + graph[cnt][i + 1:]
        else:
            if graph[cnt][i-1] == '/':
                if cnt == 0:
                    graph.insert(0, '.' * n)
                else:
                    cnt -= 1
                graph[cnt] = graph[cnt][:i] + '/' + graph[cnt][i + 1:]

            elif graph[cnt][i-1] == '_':
                graph[cnt] = graph[cnt][:i] + '/' + graph[cnt][i + 1:]
            else:
                graph[cnt] = graph[cnt][:i] + '/' + graph[cnt][i + 1:]

    elif chart[i] == '=':
        if i == 0:
            graph[0] = '_' + graph[0][1:]
        else:
            if graph[cnt][i-1] == '/':
                if cnt == 0:
                    graph.insert(0, '.' * n)
                else:
                    cnt -= 1
                graph[cnt] = graph[cnt][:i] + '_' + graph[cnt][i + 1:]

            elif graph[cnt][i-1] == '_':
                graph[cnt] = graph[cnt][:i] + '_' + graph[cnt][i + 1:]

            else:
                graph[cnt] = graph[cnt][:i] + '_' + graph[cnt][i + 1:]

    elif chart[i] == '-':
        if i == 0:
            graph[0] = '\\' + graph[0][1:]
        else:
            if graph[cnt][i-1] == '/':
                graph[cnt] = graph[cnt][:i] + '\\' + graph[cnt][i + 1:]

            elif graph[cnt][i-1] == '_':
                if cnt == len(graph) - 1:
                    graph.append('.' * n)
                cnt += 1
                graph[cnt] = graph[cnt][:i] + '\\' + graph[cnt][i + 1:]

            else:
                if cnt == len(graph) - 1:
                    graph.append('.' * n)
                cnt += 1
                graph[cnt] = graph[cnt][:i] + '\\' + graph[cnt][i + 1:]

for i in range(len(graph)):
    for j in range(len(graph[i])):
        print(graph[i][j],end='')
    print()
