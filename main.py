from tkinter import *

green = "#9bdeac"
yellow = "#f7f5dd"
font = "Courier"
work_time = 25
s_break_time = 5
l_break_time = 15

time = 0
running = True
marks = ""
work = 1
reset = False



def reset_timer():
    global running, marks, time, work, reset
    running = True
    marks = ""
    time = 0
    work = 0
    reset = True



def start_timer():
    global running, marks, time, work
    if running:
        running = False
        if len(marks) == 4:
            time = l_break_time * 60
            marks = ""
            timer_label.config(text="Long Break")
        elif work % 2 == 1:
            time = work_time * 60
            marks += "✓"
            timer_label.config(text="Work")
        else:
            time = s_break_time * 60
            timer_label.config(text="Short Break")
        timer(time)



def timer(time_t):
    global running, work, reset
    minutes = 0
    t = time_t
    if reset:
        reset = False
        t = 0

    if t > 0:
        minutes = t / 60
        if t%60 < 10:
            canvas.itemconfig(timer_text, text=f"{int(minutes)}:0{t % 60}")
        else:
            canvas.itemconfig(timer_text, text=f"{int(minutes)}:{t%60}")
        window.after(1000, timer, t -1)
    else:
        check_marks.config(text=marks)
        work += 1
        running = True
        start_timer()



window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=yellow)

canvas = Canvas(width=200, height=224, bg=yellow, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)

timer_text = canvas.create_text(100, 130, text="00:00", font=(font, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(font, 35, "bold"), bg=yellow, fg=green)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", bg=green, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=green, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(text="", bg=yellow)
check_marks.grid(row=3, column=1)

window.mainloop()
