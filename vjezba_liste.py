N = int(input("input"))
    
the_list = []
commands = []
for i in range(0, N):
    commands.append(input().split())



for i in range(0, N):
    if commands[i][0] == 'insert':
        the_list.insert(int(commands[i][1]), int(commands[i][2]))
    elif commands[i][0] == 'print':
        print(the_list)
    elif commands[i][0] == 'remove':
        the_list.remove(int(commands[i][1]))
    elif commands[i][0] == 'append':
        the_list.append(int(commands[i][1]))
    elif commands[i][0] == 'sort':
        the_list.sort()
    elif commands[i][0] == 'pop':
        the_list.pop()
    elif commands[i][0] == 'reverse':
        the_list.reverse()
