def wrap_array(array, current_letter, shift_amount):
    current_index = array.index(current_letter)
    current_index += shift_amount

    while current_index >= len(array):
        current_index -= len(array)

    while current_index < 0:
        current_index += len(array)

    return array[current_index]