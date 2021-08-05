class Rectangle:
  def __init__(self,width, height):
    self.width = width
    self.height = height

  def __repr__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height)+")"

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self): 
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self): 
    '''
    Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
    '''
    text = ""
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    else:
      for i in range(self.height):
        text += ("*" * self.width + "\n")
      return text

  def get_amount_inside(self, shape): 
    '''
    Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
    '''
    height_fit = self.height // shape.height
    width_fit = self.width // shape.width

    if height_fit == 0 or width_fit == 0:
      return 0
    else:
      return height_fit * width_fit

class Square(Rectangle):
  def __init__(self,side_length):
    Rectangle.height = side_length
    Rectangle.width = side_length

  def __repr__(self):
      return "Square(side=" + str(Rectangle.height)+")"

  def set_width(self, side):
    Rectangle.height = side
    Rectangle.width = side

  def set_height(self, side):
    Rectangle.height = side
    Rectangle.width = side

  def set_side(self, side):
    Rectangle.width = side
    Rectangle.height = side
