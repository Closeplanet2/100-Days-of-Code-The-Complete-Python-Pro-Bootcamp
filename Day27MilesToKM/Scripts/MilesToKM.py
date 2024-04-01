from Scripts.TkinterController import TkinterController

KM_CONSTANT = 1.609344

class MilesToKM:
    def __init__(self):
        self.controller = TkinterController()
        self.controller.create_window(self.function_thread_callback, wh=300, ww=500)
        self.controller.add_entry_field("0", function_callback=self.entry_field_callback, g_pos_x=1, g_pos_y=0)
        self.controller.add_label(text="Miles", g_pos_x=2, g_pos_y=0)
        self.controller.add_label(text="is equal to", g_pos_x=0, g_pos_y=1)
        self.output_label = self.controller.add_label(text="0", g_pos_x=1, g_pos_y=1)
        self.controller.add_label(text="Km", g_pos_x=2, g_pos_y=1)
        self.controller.add_button(text="Calculate", g_pos_x=1, g_pos_y=2, function_callback=self.button_callback)
        self.current_user_input = None
        self.controller.start_window()

    def function_thread_callback(self):
        pass

    def entry_field_callback(self, thread_id, option):
        self.current_user_input = option[0][0].get()

    def button_callback(self, thread_id, args):
        if self.current_user_input is None:
            return
        try:
            miles_value = float(self.current_user_input)
            km_value = miles_value * KM_CONSTANT
            print(str(km_value))
            self.output_label.config(text=str(km_value))
        except ValueError:
            print("Error")
            return
