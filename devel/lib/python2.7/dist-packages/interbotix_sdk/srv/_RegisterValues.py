# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from interbotix_sdk/RegisterValuesRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class RegisterValuesRequest(genpy.Message):
  _md5sum = "725e8187efb86073bd6c7e5fa5bb725f"
  _type = "interbotix_sdk/RegisterValuesRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Set or get the register(s) value(s) from motor(s)
#
# To get familiar with the register values, go to...
# http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/
# ...click on a motor model, and scroll down to the 'Control Table of RAM Area' section.
#
# There are four options to set or get a register value:
#   1) ARM_JOINTS_AND_GRIPPER - affects the register values for all arm joints, including the gripper.
#   2) ARM_JOINTS - affects the register values for all arm joints, excluding the gripper.
#   3) GRIPPER - affects the register value only for the gripper
#   4) SINGLE_MOTOR - affects the register for the motor specified by 'motor_name'.
#                     Note that the 'motor_name' parameter only needs to be used for this
#                     option. For any other option, it can be left blank.
#
# Set the option to the 'cmd' parameter and the 'motor_name' to the specified motor (if doing the
# SINGLE_MOTOR option)..
#
# Next, set the 'addr_name' parameter to the name of the register to be written to or read from.
#
# If setting the register(s) value, set the 'value' parameter to the desired value. This value will be
# written to either one or many motors depending on the 'cmd' option selected. Note that if a joint is
# controlled by two motors and the register is in the RAM area, both motors' registers will be updated
# with the desired value. If the register is in the EEPROM area, it must be modified with another service call.
# As an FYI, if modifying an EEPROM register, the servo must first be torqued off.
#
# If reading the register(s) values, do not set the 'value' parameter. Instead, call the service at this
# stage. The 'values' vector will be automatically updated with the register(s) value(s). If reading from
# multiple joints at a time, the indexes of the values correspond with the joint names at those indexes in the
# joint_states.name vector.

int8 ARM_JOINTS_AND_GRIPPER = 1
int8 ARM_JOINTS = 2
int8 GRIPPER = 3
int8 SINGLE_MOTOR = 4

int8 cmd
string motor_name
string addr_name
int32 value
"""
  # Pseudo-constants
  ARM_JOINTS_AND_GRIPPER = 1
  ARM_JOINTS = 2
  GRIPPER = 3
  SINGLE_MOTOR = 4

  __slots__ = ['cmd','motor_name','addr_name','value']
  _slot_types = ['int8','string','string','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       cmd,motor_name,addr_name,value

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RegisterValuesRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.cmd is None:
        self.cmd = 0
      if self.motor_name is None:
        self.motor_name = ''
      if self.addr_name is None:
        self.addr_name = ''
      if self.value is None:
        self.value = 0
    else:
      self.cmd = 0
      self.motor_name = ''
      self.addr_name = ''
      self.value = 0

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
      _x = self.cmd
      buff.write(_get_struct_b().pack(_x))
      _x = self.motor_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.addr_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.value
      buff.write(_get_struct_i().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.cmd,) = _get_struct_b().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.motor_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.motor_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.addr_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.addr_name = str[start:end]
      start = end
      end += 4
      (self.value,) = _get_struct_i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.cmd
      buff.write(_get_struct_b().pack(_x))
      _x = self.motor_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.addr_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.value
      buff.write(_get_struct_i().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.cmd,) = _get_struct_b().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.motor_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.motor_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.addr_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.addr_name = str[start:end]
      start = end
      end += 4
      (self.value,) = _get_struct_i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_b = None
def _get_struct_b():
    global _struct_b
    if _struct_b is None:
        _struct_b = struct.Struct("<b")
    return _struct_b
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from interbotix_sdk/RegisterValuesResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class RegisterValuesResponse(genpy.Message):
  _md5sum = "5dd1053b3769329bd3895728a55810d3"
  _type = "interbotix_sdk/RegisterValuesResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32[] values

"""
  __slots__ = ['values']
  _slot_types = ['int32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       values

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RegisterValuesResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.values is None:
        self.values = []
    else:
      self.values = []

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
      length = len(self.values)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.values))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.values = s.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.values)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.values.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.values = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
class RegisterValues(object):
  _type          = 'interbotix_sdk/RegisterValues'
  _md5sum = 'c4b094ee6f4751519e444f39591c55e1'
  _request_class  = RegisterValuesRequest
  _response_class = RegisterValuesResponse
