file = open('happy.txt', 'w')
file.write("""hello there, whats going on.\n okay,then do something .""")
file.close()

file1 = open(r"/home/ayush/Documents/scripts/happy.txt",'r')

print(file1.read())
file.close()