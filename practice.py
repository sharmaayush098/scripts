import  datetime
from function_test  import start
fp = open("file.txt","w+")

time_now = datetime.datetime.now()

a = input("")
str(a)
fp.write("\n %s %s" %(a, str(time_now)))

fp.close()