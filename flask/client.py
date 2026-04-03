class Client:
    def __init__(self, id=None, first_name=None, last_name=None, membership=None):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._membership = membership
    
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, value):
        self._first_name = value
    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    @property
    def membership(self):
        return self._membership
    @membership.setter
    def membership(self, value):
        self._membership = value
    

    def __str__(self):
        return f"Client(id={self._id}, first_name={self._first_name}, last_name={self._last_name}, membership={self._membership})"