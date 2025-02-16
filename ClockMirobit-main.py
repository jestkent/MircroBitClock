from microbit import display, button_a, button_b, running_time  # Import required modules

# Set the initial time here (24-hour format)
hour = 9  # Hour (1-12)
minute = 37  # Minute (0-59)
is_pm = True  # AM or PM (False = AM, True = PM)

# Store the time when the program starts
last_update_time = running_time()  # Milliseconds since the microbit started

# Loop to continuously update the time
while True:
    # Get the current time (in milliseconds)
    current_time = running_time()

    # Check if 60 seconds (60000 milliseconds) have passed since last update
    if current_time - last_update_time >= 60000:  # 1 minute passed
        # Update time by 1 minute
        minute += 1

        # If minute reaches 60, reset to 0 and increase the hour
        if minute == 60:
            minute = 0
            hour += 1

            # If hour reaches 12, switch between AM and PM
            if hour == 12:
                is_pm = not is_pm
            # If hour exceeds 12, reset to 1
            elif hour > 12:
                hour = 1

        # Update the last update time
        last_update_time = current_time

    # Always scroll the current time
    am_pm = "PM" if is_pm else "AM"
    display.scroll("{:02d}:{:02d} {}".format(hour, minute, am_pm))
