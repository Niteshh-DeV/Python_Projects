import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"  # Format as MM:SS
        print(f"\rTime left: {timer}", end="")  # Print on the same line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    print("\nTime's up!")

def main():
    print("Welcome to the Countdown Timer!")
    while True:
        try:
            duration = int(input("Enter the countdown time in seconds: "))
            if duration <= 0:
                print("Please enter a positive number.")
                continue

            print(f"Starting a {duration}-second timer...")
            countdown_timer(duration)
            
            if input("Do you want to set another timer? (yes/no): ").lower() != "yes":
                print("Thank you for using the Countdown Timer. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()