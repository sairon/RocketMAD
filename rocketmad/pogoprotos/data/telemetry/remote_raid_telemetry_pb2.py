# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/remote_raid_telemetry.proto

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
  name='pogoprotos/data/telemetry/remote_raid_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_pb=_b('\n5pogoprotos/data/telemetry/remote_raid_telemetry.proto\x12\x19pogoprotos.data.telemetry\"\xd7\x06\n\x13RemoteRaidTelemetry\x12g\n\x18remote_raid_telemetry_id\x18\x01 \x01(\x0e\x32\x45.pogoprotos.data.telemetry.RemoteRaidTelemetry.RemoteRaidTelemetryIds\x12\x64\n\x17remote_raid_join_source\x18\x02 \x01(\x0e\x32\x43.pogoprotos.data.telemetry.RemoteRaidTelemetry.RemoteRaidJoinSource\x12u\n remote_raid_invite_accept_source\x18\x03 \x01(\x0e\x32K.pogoprotos.data.telemetry.RemoteRaidTelemetry.RemoteRaidInviteAcceptSource\"\xb5\x01\n\x16RemoteRaidTelemetryIds\x12\x1f\n\x1bUNDEFINED_REMOTE_RAID_EVENT\x10\x00\x12\x1b\n\x17REMOTE_RAID_LOBBY_ENTER\x10\x01\x12\x1b\n\x17REMOTE_RAID_INVITE_SENT\x10\x02\x12\x1f\n\x1bREMOTE_RAID_INVITE_ACCEPTED\x10\x03\x12\x1f\n\x1bREMOTE_RAID_INVITE_REJECTED\x10\x04\"\x96\x01\n\x14RemoteRaidJoinSource\x12%\n!UNDEFINED_REMOTE_RAID_JOIN_SOURCE\x10\x00\x12\x18\n\x14REMOTE_RAID_USED_MAP\x10\x01\x12\x1a\n\x16REMOTE_RAID_NEARBY_GUI\x10\x02\x12!\n\x1dREMOTE_RAID_INVITED_BY_FRIEND\x10\x03\"\xa8\x01\n\x1cRemoteRaidInviteAcceptSource\x12.\n*UNDEFINED_REMOTE_RAID_INVITE_ACCEPT_SOURCE\x10\x00\x12\x16\n\x12REMOTE_RAID_IN_APP\x10\x01\x12!\n\x1dREMOTE_RAID_PUSH_NOTIFICATION\x10\x02\x12\x1d\n\x19REMOTE_RAID_NEARBY_WINDOW\x10\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_REMOTERAIDTELEMETRY_REMOTERAIDTELEMETRYIDS = _descriptor.EnumDescriptor(
  name='RemoteRaidTelemetryIds',
  full_name='pogoprotos.data.telemetry.RemoteRaidTelemetry.RemoteRaidTelemetryIds',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_REMOTE_RAID_EVENT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_RAID_LOBBY_ENTER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_RAID_INVITE_SENT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_RAID_INVITE_ACCEPTED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_RAID_INVITE_REJECTED', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=435,
  serialized_end=616,
)
_sym_db.RegisterEnumDescriptor(_REMOTERAIDTELEMETRY_REMOTERAIDTELEMETRYIDS)

_REMOTERAIDTELEMETRY_REMOTERAIDJOINSOURCE = _descriptor.EnumDescriptor(
  name='RemoteRaidJoinSource',
  full_name='pogoprotos.data.telemetry.RemoteRaidTelemetry.RemoteRaidJoinSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_REMOTE_RAID_JOIN_SOURCE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_RAID_USED_MAP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_RAID_NEARBY_GUI', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_RAID_INVITED_BY_FRIEND', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=619,
  serialized_end=769,
)
_sym_db.RegisterEnumDescriptor(_REMOTERAIDTELEMETRY_REMOTERAIDJOINSOURCE)

_REMOTERAIDTELEMETRY_REMOTERAIDINVITEACCEPTSOURCE = _descriptor.EnumDescriptor(
  name='RemoteRaidInviteAcceptSource',
  full_name='pogoprotos.data.telemetry.RemoteRaidTelemetry.RemoteRaidInviteAcceptSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_REMOTE_RAID_INVITE_ACCEPT_SOURCE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_RAID_IN_APP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_RAID_PUSH_NOTIFICATION', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_RAID_NEARBY_WINDOW', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=772,
  serialized_end=940,
)
_sym_db.RegisterEnumDescriptor(_REMOTERAIDTELEMETRY_REMOTERAIDINVITEACCEPTSOURCE)


_REMOTERAIDTELEMETRY = _descriptor.Descriptor(
  name='RemoteRaidTelemetry',
  full_name='pogoprotos.data.telemetry.RemoteRaidTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='remote_raid_telemetry_id', full_name='pogoprotos.data.telemetry.RemoteRaidTelemetry.remote_raid_telemetry_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remote_raid_join_source', full_name='pogoprotos.data.telemetry.RemoteRaidTelemetry.remote_raid_join_source', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remote_raid_invite_accept_source', full_name='pogoprotos.data.telemetry.RemoteRaidTelemetry.remote_raid_invite_accept_source', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REMOTERAIDTELEMETRY_REMOTERAIDTELEMETRYIDS,
    _REMOTERAIDTELEMETRY_REMOTERAIDJOINSOURCE,
    _REMOTERAIDTELEMETRY_REMOTERAIDINVITEACCEPTSOURCE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=940,
)

_REMOTERAIDTELEMETRY.fields_by_name['remote_raid_telemetry_id'].enum_type = _REMOTERAIDTELEMETRY_REMOTERAIDTELEMETRYIDS
_REMOTERAIDTELEMETRY.fields_by_name['remote_raid_join_source'].enum_type = _REMOTERAIDTELEMETRY_REMOTERAIDJOINSOURCE
_REMOTERAIDTELEMETRY.fields_by_name['remote_raid_invite_accept_source'].enum_type = _REMOTERAIDTELEMETRY_REMOTERAIDINVITEACCEPTSOURCE
_REMOTERAIDTELEMETRY_REMOTERAIDTELEMETRYIDS.containing_type = _REMOTERAIDTELEMETRY
_REMOTERAIDTELEMETRY_REMOTERAIDJOINSOURCE.containing_type = _REMOTERAIDTELEMETRY
_REMOTERAIDTELEMETRY_REMOTERAIDINVITEACCEPTSOURCE.containing_type = _REMOTERAIDTELEMETRY
DESCRIPTOR.message_types_by_name['RemoteRaidTelemetry'] = _REMOTERAIDTELEMETRY

RemoteRaidTelemetry = _reflection.GeneratedProtocolMessageType('RemoteRaidTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _REMOTERAIDTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.remote_raid_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.RemoteRaidTelemetry)
  ))
_sym_db.RegisterMessage(RemoteRaidTelemetry)


# @@protoc_insertion_point(module_scope)
