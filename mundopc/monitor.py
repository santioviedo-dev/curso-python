class Monitor:
    monitor_counter: int = 0
    
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size
        self._monitor_id = Monitor.monitor_counter +1
        Monitor.monitor_counter += 1
    
    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, brand):
        self._brand = brand
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size
        
    @property
    def monitor_id(self):
        return self._monitor_id
    
    def __str__(self):
        return f"""
            Monitor id: {self._monitor_id}
            Brand: {self._brand}
            Size: {self._size}
    """