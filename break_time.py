import time
import webbrowser

count = 0
print("This program started at ", time.ctime())
while (count < 3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=DgwzRB2ijHY")
    count = count + 1
