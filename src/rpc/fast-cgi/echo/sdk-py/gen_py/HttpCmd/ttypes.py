#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class STATUS:
  SUCCESS = 0
  FAILED = -1
  EXCEPTION = -2
  NO_COMMAND = -3
  PARSE_FAIL = -4
  CHECK_FAIL = -5

  _VALUES_TO_NAMES = {
    0: "SUCCESS",
    -1: "FAILED",
    -2: "EXCEPTION",
    -3: "NO_COMMAND",
    -4: "PARSE_FAIL",
    -5: "CHECK_FAIL",
  }

  _NAMES_TO_VALUES = {
    "SUCCESS": 0,
    "FAILED": -1,
    "EXCEPTION": -2,
    "NO_COMMAND": -3,
    "PARSE_FAIL": -4,
    "CHECK_FAIL": -5,
  }


class Header:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Header')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class HttpRequest:
  """
  Attributes:
   - command
   - header
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'command', None, None, ), # 1
    (2, TType.STRUCT, 'header', (Header, Header.thrift_spec), None, ), # 2
  )

  def __init__(self, command=None, header=None,):
    self.command = command
    self.header = header

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.command = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.header = Header()
          self.header.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('HttpRequest')
    if self.command is not None:
      oprot.writeFieldBegin('command', TType.STRING, 1)
      oprot.writeString(self.command)
      oprot.writeFieldEnd()
    if self.header is not None:
      oprot.writeFieldBegin('header', TType.STRUCT, 2)
      self.header.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.command is None:
      raise TProtocol.TProtocolException(message='Required field command is unset!')
    if self.header is None:
      raise TProtocol.TProtocolException(message='Required field header is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.command)
    value = (value * 31) ^ hash(self.header)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class HttpResponse:
  """
  Attributes:
   - error
   - errmsg
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'error', None, None, ), # 1
    (2, TType.STRING, 'errmsg', None, None, ), # 2
  )

  def __init__(self, error=None, errmsg=None,):
    self.error = error
    self.errmsg = errmsg

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.error = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.errmsg = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('HttpResponse')
    if self.error is not None:
      oprot.writeFieldBegin('error', TType.I32, 1)
      oprot.writeI32(self.error)
      oprot.writeFieldEnd()
    if self.errmsg is not None:
      oprot.writeFieldBegin('errmsg', TType.STRING, 2)
      oprot.writeString(self.errmsg)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.error is None:
      raise TProtocol.TProtocolException(message='Required field error is unset!')
    if self.errmsg is None:
      raise TProtocol.TProtocolException(message='Required field errmsg is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.error)
    value = (value * 31) ^ hash(self.errmsg)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
