# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_quest_details_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.quests import client_quest_pb2 as pogoprotos_dot_data_dot_quests_dot_client__quest__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_quest_details_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n@pogoprotos/networking/responses/get_quest_details_response.proto\x12\x1fpogoprotos.networking.responses\x1a)pogoprotos/data/quests/client_quest.proto\"\xf7\x01\n\x17GetQuestDetailsResponse\x12O\n\x06status\x18\x01 \x01(\x0e\x32?.pogoprotos.networking.responses.GetQuestDetailsResponse.Status\x12\x33\n\x06quests\x18\x02 \x03(\x0b\x32#.pogoprotos.data.quests.ClientQuest\"V\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x19\n\x15\x45RROR_QUEST_NOT_FOUND\x10\x02\x12\x19\n\x15\x45RROR_INVALID_DISPLAY\x10\x03\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_quests_dot_client__quest__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETQUESTDETAILSRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.GetQuestDetailsResponse.Status',
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
    _descriptor.EnumValueDescriptor(
      name='ERROR_QUEST_NOT_FOUND', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_DISPLAY', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=306,
  serialized_end=392,
)
_sym_db.RegisterEnumDescriptor(_GETQUESTDETAILSRESPONSE_STATUS)


_GETQUESTDETAILSRESPONSE = _descriptor.Descriptor(
  name='GetQuestDetailsResponse',
  full_name='pogoprotos.networking.responses.GetQuestDetailsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.GetQuestDetailsResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quests', full_name='pogoprotos.networking.responses.GetQuestDetailsResponse.quests', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETQUESTDETAILSRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=392,
)

_GETQUESTDETAILSRESPONSE.fields_by_name['status'].enum_type = _GETQUESTDETAILSRESPONSE_STATUS
_GETQUESTDETAILSRESPONSE.fields_by_name['quests'].message_type = pogoprotos_dot_data_dot_quests_dot_client__quest__pb2._CLIENTQUEST
_GETQUESTDETAILSRESPONSE_STATUS.containing_type = _GETQUESTDETAILSRESPONSE
DESCRIPTOR.message_types_by_name['GetQuestDetailsResponse'] = _GETQUESTDETAILSRESPONSE

GetQuestDetailsResponse = _reflection.GeneratedProtocolMessageType('GetQuestDetailsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETQUESTDETAILSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_quest_details_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetQuestDetailsResponse)
  ))
_sym_db.RegisterMessage(GetQuestDetailsResponse)


# @@protoc_insertion_point(module_scope)
