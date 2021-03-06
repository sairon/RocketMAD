# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/send_probe_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/send_probe_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n9pogoprotos/networking/responses/send_probe_response.proto\x12\x1fpogoprotos.networking.responses\"\xa9\x01\n\x11SendProbeResponse\x12I\n\x06result\x18\x01 \x01(\x0e\x32\x39.pogoprotos.networking.responses.SendProbeResponse.Result\x12\n\n\x02id\x18\x02 \x01(\t\x12\x1b\n\x13server_timestamp_ms\x18\x03 \x01(\x03\" \n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SENDPROBERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.SendProbeResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=232,
  serialized_end=264,
)
_sym_db.RegisterEnumDescriptor(_SENDPROBERESPONSE_RESULT)


_SENDPROBERESPONSE = _descriptor.Descriptor(
  name='SendProbeResponse',
  full_name='pogoprotos.networking.responses.SendProbeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.SendProbeResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='pogoprotos.networking.responses.SendProbeResponse.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_timestamp_ms', full_name='pogoprotos.networking.responses.SendProbeResponse.server_timestamp_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SENDPROBERESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=264,
)

_SENDPROBERESPONSE.fields_by_name['result'].enum_type = _SENDPROBERESPONSE_RESULT
_SENDPROBERESPONSE_RESULT.containing_type = _SENDPROBERESPONSE
DESCRIPTOR.message_types_by_name['SendProbeResponse'] = _SENDPROBERESPONSE

SendProbeResponse = _reflection.GeneratedProtocolMessageType('SendProbeResponse', (_message.Message,), dict(
  DESCRIPTOR = _SENDPROBERESPONSE,
  __module__ = 'pogoprotos.networking.responses.send_probe_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.SendProbeResponse)
  ))
_sym_db.RegisterMessage(SendProbeResponse)


# @@protoc_insertion_point(module_scope)
