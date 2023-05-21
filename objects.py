class Object:
    def __init__(self, name, center, mask):
        self.name = name
        self.center = center
        self.mask = mask

# breadboard inherits from object
class Breadboard(Object):
    # i might need to initialize the grid w.r.t with the breadboard coordinates, not image coordinates
    # because in the future, i might combine multiple images
    # connection should have a name

    # high level:
    # breadboard has a list of objects, and each object has:
    # - name
    # - center coordinate
    # - associated mask

    """
    format for the grid:
    
    """
    
    def __init__(self, img=None, has_power_rails=True, grid=None):
        self.img = img
        self.has_power_rails = has_power_rails
        self.num_rows = 10 # not including power rails
        self.num_cols = None # not including power rails
        self.grid = grid # middle of the breadboard (no power rails)