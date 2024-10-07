from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 
marks=""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
   global reps, marks
   window.after_cancel(timer)
   timer_title.config(text="Timer", fg = GREEN)
   marks=""
   reps=0
   check_marks.config(text= marks)
   canvas.itemconfig(timer_text, text ="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_buttonfn():
   
   
   global reps, marks
   check_marks.config(text= marks)
   work_sec = round(WORK_MIN*60)
   short_break_sec =round(SHORT_BREAK_MIN*60)
   long_break_sec = round(LONG_BREAK_MIN*60)

   if reps in (0,2,4,6):
      count_down(work_sec)
      timer_title.config(text="Work", fg = GREEN)
      reps = reps+1
      marks +="✔️"
   elif reps == 7:
      count_down(long_break_sec)
      timer_title.config(text="Break", fg = RED)
      reps=0
      marks=""
      return
   else:
      count_down(short_break_sec)
      reps= reps+1 
      timer_title.config(text="Break", fg = PINK)

   

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
   global timer
   min = math.floor(count/60)
   sec= count%60
  #  if int(sec)<=9 and sec>0:
  #     sec=f"{0}{sec}"
   if sec < 10:
      sec=f"0{sec}"   
    
   canvas.itemconfig(timer_text, text =f"{min}:{sec}")
   if count>0:
      timer = window.after(1000, count_down, count-1)
   else:
      start_buttonfn()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112,image= img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 37, 'bold'), bg=YELLOW)
timer_title.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_buttonfn)
start_button.grid(column=0, row=2)

reset_button = Button(text = "Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_marks= Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
check_marks.grid(column=1, row=3)

window.mainloop()