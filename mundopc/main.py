from computer import Computer
from monitor import Monitor
from input_devices import Keyboard, Mouse
from order import Order

if __name__ == "__main__":
    monitor1 = Monitor("LG", "27 inches")
    keyboard1 = Keyboard("Logitech", "Mechanical")
    mouse1 = Mouse("Razer", "Optical")
    
    computer1 = Computer("Gaming PC", monitor1, keyboard1, mouse1)
    
    order1 = Order()
    order1.add_computer(computer1)
    
    print(order1)