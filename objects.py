class Object:
    # an object is an element that's identifiable by the segmentation model
    def __init__(self, name, center, mask):
        self.name = name
        self.center = center
        self.mask = mask

class Net:
    def __init__(self, code, name):
        # at the beginning, node is these 5 vertical points on the breadboard
        self.code = code # code is just 0, 1, etc., as in n0, n1, n2, etc.
        self.name = name # name is an alternative custom name like VCC, GND, AMP_INPUT, etc.
        self.nodes = [] # nodes are specific pins on the chip, wires, resistors, etc. that are connected to this net

    def add_node(self, node):
        self.nodes.append(node)

# Helper function for the Point class
def set_name_from_coord(self, coord):
    return "a1" # TODO: implement this

class Point:
    # a point is a hole on the breadboard
    # it has an image-specific coordinate and a name on a breadboard (like a1, j10) that it represents
    def __init__(self, coord):
        self.coord = coord
        self.name = set_name_from_coord(coord)

class Wire(Object):
    def __init__(self, name, center, mask):
        super().__init__(name, center, mask)
        self.contact_pt1 = None # instance of Point class
        self.contact_pt2 = None

class Passive(Object):
    # resistor or a capacitor
    def __init__(self, name, center, mask):
        super().__init__(name, center, mask)
        self.contact_pt1 = None # instance of Point class
        self.contact_pt2 = None
        self.ref = None
        self.value = None

class Chip(Object):
    def __init__(self, name, center, mask):
        super().__init__(name, center, mask)
        # connection is a point on the grid that has been identified as the closest to the center of the chip
        self.num_pins = None
        # format: probably (<letter><number>) for readability
        self.contact_pts = []
        self.datasheet = None
        self.ref = None

# breadboard inherits from object
class Breadboard(Object):
    # there will be two breadboard objects:
    # 1. breadboard that's obtained from the image (potentially, buggy)
    # 2. breadboard that's obtained from the schematics (reference)
    # our final goal is to identify differences between them and suggest what to fix
    def __init__(self, name, center, mask, grid):
        super().__init__(name, center, mask)
        # grid is a list of Point objects, where each Point object has a name (like a1, j10) and a coordinate (just x,y)
        self.grid = grid
        # wires, resistors, capacitors, chips; everything else will probably need to be manually annotated
        self.objects = []