import time
import webbrowser

break_count = 0
total_break = 3
second_to_wait_before_next_break = 10
print("This program started at ", time.ctime())
while (break_count < total_break):
    time.sleep(second_to_wait_before_next_break)
    webbrowser.open("https://www.youtube.com/watch?v=DgwzRB2ijHY")
    break_count = break_count + 1
