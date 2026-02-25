class InputDevice:
    def __init__(self, brand, input_type):
        self._brand = brand
        self._input_type = input_type
    
    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, brand):
        self._brand = brand
    @property
    def input_type(self):
        return self._input_type
    @input_type.setter
    def input_type(self, input_type):
        self._input_type = input_type


class Mouse(InputDevice):
    mouse_counter: int = 0
    
    def __init__(self, brand, input_type):
        super().__init__(brand, input_type)
        self._mouse_id = Mouse.mouse_counter +1
        Mouse.mouse_counter += 1
    
    @property
    def mouse_id(self):
        return self._mouse_id

    def __str__(self):
        return f"""
            Mouse id: {self._mouse_id}
            Brand: {self._brand}
    """
    

class Keyboard(InputDevice):
    keyboard_counter: int = 0
    
    def __init__(self, brand, input_type):
        super().__init__(brand, input_type)
        self._keyboard_id = Keyboard.keyboard_counter +1
        Keyboard.keyboard_counter += 1
    
    @property
    def keyboard_id(self):
        return self._keyboard_id

    def __str__(self):
        return f"""
            Keyboard id: {self._keyboard_id}
            Brand: {self._brand}
    """
    



