import tkinter as tk

running = False
hours, minutes, seconds = 0, 0, 0
laps = []
currentTime = ""

def start():
    global running
    if not running:
        update()
        running = True

def pause():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False
    
def reset():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        lap_label.after_cancel(update_time)
        running = False
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    laps.clear()
    stopwatch_label.config(text = '00:00:00')
    lap_label.config(text = '')

def lap():
    laps.append(currentTime)
    lap_label.config(text="\n".join(map(str, laps)))

def update():
    global hours, minutes, seconds
    seconds += 1
    
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'

    global currentTime 
    currentTime = hours_string + ':' + minutes_string + ':' + seconds_string
    
    stopwatch_label.config(text = currentTime)
    
    global update_time
    update_time = stopwatch_label.after(1000, update)


root = tk.Tk()
root.title('Stopwatch')

stopwatch_label = tk.Label(text = '00:00:00', font = ('Arial', 50))
stopwatch_label.pack()


lap_label = tk.Label(text="", justify="left", font = ('Arial', 20), pady=4)
lap_label.pack(side=tk.BOTTOM)

button_style = {"background": "#bfbfbf", "foreground": "#000000", "activebackground": "#bfbfbf", "activeforeground": "#000000"}

start_button = tk.Button(root, text="Start", command=start, **button_style, height=1, width=7, font=('Arial', 20),)
start_button.pack(side = tk.LEFT)
pause_button = tk.Button(root, text="Pause", command=pause, **button_style, height=1, width=7, font=('Arial', 20),)
pause_button.pack(side = tk.LEFT)
reset_button =  tk.Button(root, text="Lap", command=lap, **button_style, height=1, width=7, font=('Arial', 20),)
reset_button.pack(side = tk.LEFT)
reset_button =  tk.Button(root, text="Reset", command=reset, **button_style, height=1, width=7, font=('Arial', 20),)
reset_button.pack(side = tk.LEFT)
quit_button =  tk.Button(root, text="Quit", command=root.quit, **button_style, height=1, width=7, font=('Arial', 20),)
quit_button.pack(side = tk.LEFT)


root.mainloop()