# return_screen_coordinate
This script is a Python program that uses the `pynput` library and `tkinter` to capture a selected region of the screen and save it as a screenshot.

Let's break down the script:

1. The necessary imports are made:
   - `Listener` from `pynput.mouse` for capturing mouse events
   - `Image`, `ImageGrab` from `PIL` for capturing screenshots
   - `tkinter` as `tk` for creating the GUI window

2. A `tkinter` window (`root`) is created.

3. Variables `ix` and `iy` are initialized to store the starting position of the mouse.

4. The screen width and height are obtained using `root.winfo_screenwidth()` and `root.winfo_screenheight()`.

5. Two event handler functions, `on_move` and `on_click`, are defined:
   - `on_move` is called when the mouse pointer is moved and prints the current coordinates.
   - `on_click` is called when a mouse button is clicked:
     - If the left mouse button is pressed, the starting position (`ix`, `iy`) is updated and the coordinates are printed.
     - If the left mouse button is released, a rectangle is drawn on the `canvas` using the starting and ending positions (`ix`, `iy`, `x`, `y`).
     - A screenshot is taken using `ImageGrab.grab(bbox=(ix, iy, x, y))` and saved as "screenshot.png".
     - The `tkinter` window (`root`) is closed using `root.quit()`.

6. The screen width and height are printed.

7. The `root_geometry` string is created to set the size of the `root` window.

8. The `root` window is configured with the given geometry and made transparent.

9. A `tkinter` canvas (`canvas`) is created with the same size as the screen and configured with a cross-shaped cursor.

10. The `Listener` object is created using the event handlers `on_move` and `on_click`.

11. The `tkinter` window (`root`) is started using `root.mainloop()`, and the listener starts capturing events.

 the "Escape" key is used to stop the program. Pressing the "Escape" key will stop the listeners, close the tkinter window, and exit the program.
12. Once the `tkinter` window is closed (`root.quit()` is called), the listener stops capturing events using `listener.join()`.
