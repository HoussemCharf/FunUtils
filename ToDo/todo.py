#! /usr/bin/python -tt
import datetime
import webbrowser
import time
def main():
    print ("The Scheduler has begun !!!! :) \nThe Scheduler is now ACTIVE")
    while(1):
        tempTime = str(datetime.datetime.now().time())
        listTime = tempTime.split(':',1)
        hour = int(listTime[0]) + 1
        hour = str(hour)
#  extracting minutes out of the time
        tempMinute = str(listTime[1])
        minute = tempMinute[0:2]
#  extracting seconds out of the time
        tempSecList = tempMinute.split(':')
        tempSecString = str(tempSecList[1])
        sec = tempSecString[0:2]
        if( minute == '24' and sec == '01'):
            if hour == '11':
                with open('C:\Users\user\Desktop\todo.txt','r+') as f:
                    f.write("Please send in the 11pm - 12am CST report")
                webbrowser.open_new_tab('C:\Users\user\Desktop\todo.txt')
                time.sleep(1)
            elif hour == '12':
                with open('C:\Users\user\Desktop\todo.txt','r+') as f:
                    f.write("Task 1\n")
                webbrowser.open('C:\Users\user\Desktop\todo.txt')
                time.sleep(1)
            elif hour == '13':
                with open('C:\Users\user\Desktop\todo.txt','r+') as f:
                    f.write("Task 2\n")
                webbrowser.open_new_tab('C:\Users\user\Desktop\todo.txt')
                time.sleep(1)
            elif hour == '14':
                with open('C:\Users\user\Desktop\todo.txt','r+') as f:
                    f.write("Task 3\n")
                webbrowser.open_new_tab('C:\Users\user\Desktop\todo.txt')
                time.sleep(1)
            elif hour == '15':
                with open('C:\Users\user\Desktop\todo.txt','r+') as f:
                    f.write("Task 4\n")
                webbrowser.open_new_tab('C:\Users\user\Desktop\todo.txt')
                time.sleep(1)
            elif hour == '16':
                with open('C:\Users\user\Desktop\todo.txt','r+') as f:
                    f.write("Task 5\n")
                webbrowser.open_new_tab('C:\Users\user\Desktop\todo.txt')
                time.sleep(1)
            elif hour == '17':
                with open('C:\Users\user\Desktop\todo.txt','r+') as f:
                    f.write("Task 6\n")
                webbrowser.open_new_tab('C:\Users\user\Desktop\todo.txt')
                time.sleep(1)
    print ("The Scheduler is now INACTIVE")
if __name__ == '__main__':
    main()
