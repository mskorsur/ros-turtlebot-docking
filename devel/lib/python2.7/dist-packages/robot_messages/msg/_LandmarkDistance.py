# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from robot_messages/LandmarkDistance.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class LandmarkDistance(genpy.Message):
  _md5sum = "a001cb7348c79b1e965248b3cb75752a"
  _type = "robot_messages/LandmarkDistance"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string name 	# Name of the simulated docking station landmark
float64 distance 	# Distance to the landmark, in meters
float64 quat_orientation_x	# Orientation of the robot, in radians
float64 quat_orientation_y
float64 quat_orientation_z
float64 quat_orientation_w"""
  __slots__ = ['name','distance','quat_orientation_x','quat_orientation_y','quat_orientation_z','quat_orientation_w']
  _slot_types = ['string','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       name,distance,quat_orientation_x,quat_orientation_y,quat_orientation_z,quat_orientation_w

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LandmarkDistance, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.name is None:
        self.name = ''
      if self.distance is None:
        self.distance = 0.
      if self.quat_orientation_x is None:
        self.quat_orientation_x = 0.
      if self.quat_orientation_y is None:
        self.quat_orientation_y = 0.
      if self.quat_orientation_z is None:
        self.quat_orientation_z = 0.
      if self.quat_orientation_w is None:
        self.quat_orientation_w = 0.
    else:
      self.name = ''
      self.distance = 0.
      self.quat_orientation_x = 0.
      self.quat_orientation_y = 0.
      self.quat_orientation_z = 0.
      self.quat_orientation_w = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_5d.pack(_x.distance, _x.quat_orientation_x, _x.quat_orientation_y, _x.quat_orientation_z, _x.quat_orientation_w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8')
      else:
        self.name = str[start:end]
      _x = self
      start = end
      end += 40
      (_x.distance, _x.quat_orientation_x, _x.quat_orientation_y, _x.quat_orientation_z, _x.quat_orientation_w,) = _struct_5d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_5d.pack(_x.distance, _x.quat_orientation_x, _x.quat_orientation_y, _x.quat_orientation_z, _x.quat_orientation_w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8')
      else:
        self.name = str[start:end]
      _x = self
      start = end
      end += 40
      (_x.distance, _x.quat_orientation_x, _x.quat_orientation_y, _x.quat_orientation_z, _x.quat_orientation_w,) = _struct_5d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_5d = struct.Struct("<5d")
