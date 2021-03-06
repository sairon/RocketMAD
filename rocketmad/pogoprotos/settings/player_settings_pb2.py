# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/player_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.settings import social_settings_pb2 as pogoprotos_dot_settings_dot_social__settings__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/player_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_pb=_b('\n)pogoprotos/settings/player_settings.proto\x12\x13pogoprotos.settings\x1a)pogoprotos/settings/social_settings.proto\"~\n\x0ePlayerSettings\x12\x1d\n\x15opt_out_online_status\x18\x01 \x01(\x08\x12M\n\x13\x63ompleted_tutorials\x18\x02 \x03(\x0e\x32\x30.pogoprotos.settings.SocialSettings.TutorialTypeb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_settings_dot_social__settings__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PLAYERSETTINGS = _descriptor.Descriptor(
  name='PlayerSettings',
  full_name='pogoprotos.settings.PlayerSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opt_out_online_status', full_name='pogoprotos.settings.PlayerSettings.opt_out_online_status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='completed_tutorials', full_name='pogoprotos.settings.PlayerSettings.completed_tutorials', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=235,
)

_PLAYERSETTINGS.fields_by_name['completed_tutorials'].enum_type = pogoprotos_dot_settings_dot_social__settings__pb2._SOCIALSETTINGS_TUTORIALTYPE
DESCRIPTOR.message_types_by_name['PlayerSettings'] = _PLAYERSETTINGS

PlayerSettings = _reflection.GeneratedProtocolMessageType('PlayerSettings', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERSETTINGS,
  __module__ = 'pogoprotos.settings.player_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.PlayerSettings)
  ))
_sym_db.RegisterMessage(PlayerSettings)


# @@protoc_insertion_point(module_scope)
