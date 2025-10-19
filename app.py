import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("00:00\nTimer completed!")

while True:
    user_input = input("Enter time (seconds or mm:ss): ")

    try:
        if ':' in user_input:
            mins, secs = map(int, user_input.split(':'))
            total_seconds = mins * 60 + secs
        else:
            total_seconds = int(user_input)

        if total_seconds < 0:
            print("Time must be a positive number. Please try again.")
            continue

        break
    except ValueError:
        print("Invalid format. Please enter seconds or mm:ss format.")

countdown(total_seconds)
