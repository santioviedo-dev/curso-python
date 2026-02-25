from computer import Computer
class Order:
    order_counter: int = 0
    
    def __init__(self):
        self._computers = []
        self._order_id = Order.order_counter + 1
        Order.order_counter += 1
    
    @property
    def order_id(self):
        return self._order_id
    
    @property
    def computers(self):
        return self._computers
    
    def add_computer(self, computer):
        self._computers.append(computer)
    
    def __str__(self):   
        computers_str = "\n".join(str(computer) for computer in self._computers)
        return f"""
            Order id: {self._order_id}
            Computers: {computers_str}
    """
    