# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/encounter_settings.proto

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
  name='pogoprotos/settings/master/encounter_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_pb=_b('\n3pogoprotos/settings/master/encounter_settings.proto\x12\x1apogoprotos.settings.master\"\xd3\x05\n\x11\x45ncounterSettings\x12\x1c\n\x14spin_bonus_threshold\x18\x01 \x01(\x02\x12!\n\x19\x65xcellent_throw_threshold\x18\x02 \x01(\x02\x12\x1d\n\x15great_throw_threshold\x18\x03 \x01(\x02\x12\x1c\n\x14nice_throw_threshold\x18\x04 \x01(\x02\x12\x1b\n\x13milestone_threshold\x18\x05 \x01(\x05\x12\x1c\n\x14\x61r_plus_mode_enabled\x18\x06 \x01(\x08\x12$\n\x1c\x61r_close_proximity_threshold\x18\x07 \x01(\x02\x12\"\n\x1a\x61r_low_awareness_threshold\x18\x08 \x01(\x02\x12%\n\x1d\x61r_close_proximity_multiplier\x18\t \x01(\x02\x12&\n\x1e\x61r_awareness_penalty_threshold\x18\n \x01(\x02\x12\'\n\x1f\x61r_low_awareness_max_multiplier\x18\x0b \x01(\x02\x12\x30\n(ar_high_awareness_min_penalty_multiplier\x18\x0c \x01(\x02\x12\'\n\x1f\x61r_plus_attempts_until_flee_max\x18\r \x01(\x05\x12,\n$ar_plus_attempts_until_flee_infinite\x18\x0e \x01(\x05\x12$\n\x1c\x65scaped_bonus_multiplier_max\x18\x0f \x01(\x02\x12\x33\n+escaped_bonus_multiplier_by_excellent_throw\x18\x10 \x01(\x02\x12/\n\'escaped_bonus_multiplier_by_great_throw\x18\x11 \x01(\x02\x12.\n&escaped_bonus_multiplier_by_nice_throw\x18\x12 \x01(\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ENCOUNTERSETTINGS = _descriptor.Descriptor(
  name='EncounterSettings',
  full_name='pogoprotos.settings.master.EncounterSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spin_bonus_threshold', full_name='pogoprotos.settings.master.EncounterSettings.spin_bonus_threshold', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='excellent_throw_threshold', full_name='pogoprotos.settings.master.EncounterSettings.excellent_throw_threshold', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='great_throw_threshold', full_name='pogoprotos.settings.master.EncounterSettings.great_throw_threshold', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nice_throw_threshold', full_name='pogoprotos.settings.master.EncounterSettings.nice_throw_threshold', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='milestone_threshold', full_name='pogoprotos.settings.master.EncounterSettings.milestone_threshold', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ar_plus_mode_enabled', full_name='pogoprotos.settings.master.EncounterSettings.ar_plus_mode_enabled', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ar_close_proximity_threshold', full_name='pogoprotos.settings.master.EncounterSettings.ar_close_proximity_threshold', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ar_low_awareness_threshold', full_name='pogoprotos.settings.master.EncounterSettings.ar_low_awareness_threshold', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ar_close_proximity_multiplier', full_name='pogoprotos.settings.master.EncounterSettings.ar_close_proximity_multiplier', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ar_awareness_penalty_threshold', full_name='pogoprotos.settings.master.EncounterSettings.ar_awareness_penalty_threshold', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ar_low_awareness_max_multiplier', full_name='pogoprotos.settings.master.EncounterSettings.ar_low_awareness_max_multiplier', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ar_high_awareness_min_penalty_multiplier', full_name='pogoprotos.settings.master.EncounterSettings.ar_high_awareness_min_penalty_multiplier', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ar_plus_attempts_until_flee_max', full_name='pogoprotos.settings.master.EncounterSettings.ar_plus_attempts_until_flee_max', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ar_plus_attempts_until_flee_infinite', full_name='pogoprotos.settings.master.EncounterSettings.ar_plus_attempts_until_flee_infinite', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='escaped_bonus_multiplier_max', full_name='pogoprotos.settings.master.EncounterSettings.escaped_bonus_multiplier_max', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='escaped_bonus_multiplier_by_excellent_throw', full_name='pogoprotos.settings.master.EncounterSettings.escaped_bonus_multiplier_by_excellent_throw', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='escaped_bonus_multiplier_by_great_throw', full_name='pogoprotos.settings.master.EncounterSettings.escaped_bonus_multiplier_by_great_throw', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='escaped_bonus_multiplier_by_nice_throw', full_name='pogoprotos.settings.master.EncounterSettings.escaped_bonus_multiplier_by_nice_throw', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=84,
  serialized_end=807,
)

DESCRIPTOR.message_types_by_name['EncounterSettings'] = _ENCOUNTERSETTINGS

EncounterSettings = _reflection.GeneratedProtocolMessageType('EncounterSettings', (_message.Message,), dict(
  DESCRIPTOR = _ENCOUNTERSETTINGS,
  __module__ = 'pogoprotos.settings.master.encounter_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.EncounterSettings)
  ))
_sym_db.RegisterMessage(EncounterSettings)


# @@protoc_insertion_point(module_scope)
