# MircroBitClock
I want to make use of my extra MicroBit and I don't have a clock so I created a Digital Clock on Microbit

Digital Clock on Microbit
This repository contains the code for a digital clock running on a BBC Microbit. The clock is designed to display the current time in a 12-hour format with an AM/PM indicator, and it continuously scrolls the current time on the LED matrix. The time updates every minute, ensuring accurate timekeeping. The clock's functionality is implemented using Python and the microbit module.

Key Features:
Displays time in 12-hour format (hh:mm AM/PM).
Updates every minute (once the minute reaches 60, the hour increments).
Continuous scrolling of time on the Microbit's LED display.
No sleep or pauses in the display – it keeps running while updating once a minute.
How It Works:
The clock uses the running_time() function to track the passage of time and updates the minute count every 60 seconds.
The display scrolls the current time, but the minute only increments after a full minute has passed.
Buttons can be added to change or modify the time if needed.
Installation:
Download the code onto your BBC Microbit.
The code will automatically run, showing the current time and updating it every minute.
Customization:
You can manually set the initial time in the code by changing the values of hour and minute in the script.
The clock uses AM and PM for time representation, but this can be adjusted if needed.
