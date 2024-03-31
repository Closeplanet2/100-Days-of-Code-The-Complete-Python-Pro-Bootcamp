def get_user_input(prompt_text, correct_values=None, default_value=None):
    while True:
        user_input = input(prompt_text)
        if correct_values is None: return user_input
        if user_input in correct_values: return user_input
        if default_value is not None: return default_value
        print("Invalid Input!")


def get_user_int_input(prompt_text, correct_values=None, default_value=None):
    while True:
        try:
            user_input = int(input(prompt_text))
            if correct_values is None: return user_input
            if user_input in correct_values: return user_input
            if default_value is not None: return default_value
            print("Invalid Input!")
        except ValueError:
            if default_value is not None: return default_value
            print("Invalid number!")