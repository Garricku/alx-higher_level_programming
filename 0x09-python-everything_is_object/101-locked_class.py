def init(self, first_name):
    self.first_name = first_name

LockedClass = type("LockedClass", (), {"__slots__": ["first_name"],
    "__init__": init})
