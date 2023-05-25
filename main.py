from pynput.mouse import Listener, Button
from pynput.keyboard import Key, Listener as KeyListener
from PIL import Image, ImageGrab
import tkinter as tk
import sys

root = tk.Tk()

ix = None
iy = None
stop = False

# Get the current screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


# Get and print coordinates
def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))


# Start and End mouse position
def on_click(x, y, button, pressed):
    global ix, iy
    if button == Button.left:
        # Left button pressed then continue
        if pressed:
            ix = x
            iy = y
            print('left button pressed at {0}'.format((x, y)))
        else:
            print('left button released at {0}'.format((x, y)))
            canvas.create_rectangle(ix, iy, x, y)  # Draw a rectangle
            canvas.pack()
            img = ImageGrab.grab(bbox=(ix, iy, x, y))  # Take the screenshot
            img.save('screenshot.png')  # Save screenshot
            root.quit()  # Remove tkinter window

    elif button == Button.right:
        # Right button pressed then stop
        print('right button pressed at {0}'.format((x, y)))
        stop_program()

    if not pressed:
        # Stop listener
        return False


def on_key_press(key):
    global stop
    if key == Key.esc:
        stop_program()


def stop_program():
    global stop
    stop = True
    listener.stop()
    key_listener.stop()
    root.quit()
    sys.exit()


# Print the screen width and height
print(screen_width, screen_height)

root_geometry = str(screen_width) + 'x' + str(screen_height)  # Creates a geometric string argument
root.geometry(root_geometry)  # Sets the geometry string value

root.overrideredirect(True)
root.wait_visibility(root)
root.wm_attributes("-alpha", 0.01)  # Set windows transparent

canvas = tk.Canvas(root, width=screen_width, height=screen_height)  # Create canvas
canvas.config(cursor="cross")  # Change mouse pointer to cross
canvas.pack()

# Collect events until released or stopped
with Listener(on_move=on_move, on_click=on_click) as listener, KeyListener(on_press=on_key_press) as key_listener:
    root.mainloop()  # Start tkinter window
    if stop:
        sys.exit()  # Close the program
