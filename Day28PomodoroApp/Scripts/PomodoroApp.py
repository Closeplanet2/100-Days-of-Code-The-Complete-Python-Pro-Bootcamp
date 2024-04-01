from Scripts.TkinterController import TkinterController
import time
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

class PomodoroApp:
    def __init__(self):
        self.current_time = WORK_MIN * 60
        self.run_timer = False
        self.reps = 0
        self.controller = TkinterController()
        self.controller.create_window(self.function_thread_callback, wt="PomodoroApp", wh=500, ww=500, bg=YELLOW)
        self.controller.current_window.config(padx=50, pady=50)
        self.timer_title = self.controller.add_label("Timer", fg=GREEN, g_pos_x=1, g_pos_y=0, bg=YELLOW, ff=FONT_NAME, fs=35)
        self.tomato_image = self.controller.add_image(image_path="Images/tomato.png", w=200, h=224, bg=YELLOW, g_pos_x=1, g_pos_y=1)
        self.timer_text = self.controller.add_label(text="{:02d}:{:02d}".format(0, 0), bg=None, fg="#000000", ff=FONT_NAME, fs=35, g_pos_x=1, g_pos_y=1)
        self.controller.add_button(text="Start", g_pos_x=0, g_pos_y=2, function_callback=self.button_callback_start, bg=YELLOW, fg="#000000")
        self.controller.add_button(text="Reset", g_pos_x=2, g_pos_y=2, function_callback=self.button_callback_reset, bg=YELLOW, fg="#000000")
        self.tick_label = self.controller.add_label(text="", g_pos_x=1, g_pos_y=3, fg=GREEN, bg=YELLOW)
        self.controller.start_window()

    def function_thread_callback(self):
        if not self.run_timer: return
        self.current_time -= 1
        seconds = self.current_time
        minutes = self.current_time // 60
        seconds %= 60
        self.timer_text.config(text="{:02d}:{:02d}".format(minutes, seconds))
        if self.current_time <= 0:
            self.button_callback_start(None, None)
            marks = ""
            work_sessions = math.floor(self.reps / 2)
            for x in range(work_sessions):
                marks += "✅"
            self.tick_label.config(text=marks)

    def button_callback_start(self, thread_id, args):
        self.reps += 1
        if self.reps % 8 == 0:
            self.timer_title.config(text="BREAK", fg=RED)
            self.current_time = LONG_BREAK_MIN * 60
        elif self.reps % 2 == 0:
            self.timer_title.config(text="BREAK", fg=PINK)
            self.current_time = SHORT_BREAK_MIN * 60
        else:
            self.timer_title.config(text="WORK", fg=GREEN)
            self.current_time = WORK_MIN * 60
        self.run_timer = True

    def button_callback_reset(self, thread_id, args):
        self.run_timer = False
        self.current_time = 0
        self.reps = 0
        self.tick_label.config(text="")
        self.timer_title.config(text="TIMER", fg=GREEN)
        self.timer_text.config(text="{:02d}:{:02d}".format(0, 0))