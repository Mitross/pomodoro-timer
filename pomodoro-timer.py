import time
import winsound  

def pomodoro_timer():
    work_minutes = 25
    short_break = 5
    long_break = 15
    sessions = 0
    
    while True:
        # Work session
        print(f"\nWork for {work_minutes} minutes (Session {sessions + 1})")
        countdown(work_minutes * 60)
        winsound.Beep(440, 1000)  # beep
        sessions += 1
        
        # Break session
        if sessions % 4 == 0:
            print(f"\nLong break  {long_break} minutes")
            countdown(long_break * 60)
        else:
            print(f"\nShort break  {short_break} minutes")
            countdown(short_break * 60)
        winsound.Beep(880, 1000)

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1

if __name__ == "__main__":
    print("=== Pomodoro Timer ===")
    print("(Ctrl+C to exit)")
    try:
        pomodoro_timer()
    except KeyboardInterrupt:
        print("\nnice job... lets get you as rubdown")
   
    
