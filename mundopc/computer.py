from monitor import Monitor
from input_devices import Keyboard, Mouse

class Computer:
    computer_counter: int = 0
    
    def __init__(self, description, monitor: Monitor, keyboard: Keyboard, mouse: Mouse):
        self._description = description
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse
        self._computer_id = Computer.computer_counter +1
        Computer.computer_counter += 1
        
    
    def __str__(self):
        return f"""
            Computer id: {self._computer_id}
            Description: {self._description}
            Monitor: {self._monitor}
            Keyboard: {self._keyboard}
            Mouse: {self._mouse}
    """