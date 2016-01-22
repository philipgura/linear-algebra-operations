class Vector(object):
  def __init__(self, coordinates):
    try:
      if not coordinates:
        raise ValueError
      self.coordinates = tuple(coordinates)
      self.demension = len(coordinates)
    
    except ValueError:
      raise ValueError('The coordinates must be nonempty')
    
    except TypeError:
      raise ValueError('The coordinates must be an iterable')