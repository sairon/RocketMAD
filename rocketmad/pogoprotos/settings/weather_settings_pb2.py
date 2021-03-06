# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/weather_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.settings import weather_alert_settings_pb2 as pogoprotos_dot_settings_dot_weather__alert__settings__pb2
from pogoprotos.map.weather import display_weather_pb2 as pogoprotos_dot_map_dot_weather_dot_display__weather__pb2
from pogoprotos.map.weather import gameplay_weather_pb2 as pogoprotos_dot_map_dot_weather_dot_gameplay__weather__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/weather_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_pb=_b('\n*pogoprotos/settings/weather_settings.proto\x12\x13pogoprotos.settings\x1a\x30pogoprotos/settings/weather_alert_settings.proto\x1a,pogoprotos/map/weather/display_weather.proto\x1a-pogoprotos/map/weather/gameplay_weather.proto\"\xa9\x11\n\x0fWeatherSettings\x12W\n\x11gameplay_settings\x18\x01 \x01(\x0b\x32<.pogoprotos.settings.WeatherSettings.GameplayWeatherSettings\x12U\n\x10\x64isplay_settings\x18\x02 \x01(\x0b\x32;.pogoprotos.settings.WeatherSettings.DisplayWeatherSettings\x12\x41\n\x0e\x61lert_settings\x18\x03 \x01(\x0b\x32).pogoprotos.settings.WeatherAlertSettings\x12Q\n\x0estale_settings\x18\x04 \x01(\x0b\x32\x39.pogoprotos.settings.WeatherSettings.StaleWeatherSettings\x1a\x84\x01\n\x14\x43onditionMapSettings\x12T\n\x12gameplay_condition\x18\x01 \x01(\x0e\x32\x38.pogoprotos.map.weather.GameplayWeather.WeatherCondition\x12\x16\n\x0eprovider_enums\x18\x02 \x03(\t\x1a\xa6\x03\n\x14\x44isplayLevelSettings\x12\x17\n\x0f\x63ondition_enums\x18\x01 \x03(\t\x12H\n\x0b\x63loud_level\x18\x02 \x01(\x0e\x32\x33.pogoprotos.map.weather.DisplayWeather.DisplayLevel\x12G\n\nrain_level\x18\x03 \x01(\x0e\x32\x33.pogoprotos.map.weather.DisplayWeather.DisplayLevel\x12G\n\nsnow_level\x18\x04 \x01(\x0e\x32\x33.pogoprotos.map.weather.DisplayWeather.DisplayLevel\x12\x46\n\tfog_level\x18\x05 \x01(\x0e\x32\x33.pogoprotos.map.weather.DisplayWeather.DisplayLevel\x12Q\n\x14special_effect_level\x18\x06 \x01(\x0e\x32\x33.pogoprotos.map.weather.DisplayWeather.DisplayLevel\x1a\x85\x06\n\x16\x44isplayWeatherSettings\x12p\n\x16\x64isplay_level_settings\x18\x01 \x03(\x0b\x32P.pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.DisplayLevelSettings\x12j\n\x13wind_level_settings\x18\x02 \x01(\x0b\x32M.pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.WindLevelSettings\x1a\xa6\x03\n\x14\x44isplayLevelSettings\x12\x17\n\x0f\x63ondition_enums\x18\x01 \x03(\t\x12H\n\x0b\x63loud_level\x18\x02 \x01(\x0e\x32\x33.pogoprotos.map.weather.DisplayWeather.DisplayLevel\x12G\n\nrain_level\x18\x03 \x01(\x0e\x32\x33.pogoprotos.map.weather.DisplayWeather.DisplayLevel\x12G\n\nsnow_level\x18\x04 \x01(\x0e\x32\x33.pogoprotos.map.weather.DisplayWeather.DisplayLevel\x12\x46\n\tfog_level\x18\x05 \x01(\x0e\x32\x33.pogoprotos.map.weather.DisplayWeather.DisplayLevel\x12Q\n\x14special_effect_level\x18\x06 \x01(\x0e\x32\x33.pogoprotos.map.weather.DisplayWeather.DisplayLevel\x1a\x64\n\x11WindLevelSettings\x12\x19\n\x11wind_level1_speed\x18\x01 \x01(\x05\x12\x19\n\x11wind_level2_speed\x18\x02 \x01(\x05\x12\x19\n\x11wind_level3_speed\x18\x03 \x01(\x05\x1a\xc5\x02\n\x17GameplayWeatherSettings\x12h\n\rcondition_map\x18\x01 \x03(\x0b\x32Q.pogoprotos.settings.WeatherSettings.GameplayWeatherSettings.ConditionMapSettings\x12\x1b\n\x13min_speed_for_windy\x18\x02 \x01(\x05\x12\x1c\n\x14\x63onditions_for_windy\x18\x03 \x03(\t\x1a\x84\x01\n\x14\x43onditionMapSettings\x12T\n\x12gameplay_condition\x18\x01 \x01(\x0e\x32\x38.pogoprotos.map.weather.GameplayWeather.WeatherCondition\x12\x16\n\x0eprovider_enums\x18\x02 \x03(\t\x1aj\n\x14StaleWeatherSettings\x12*\n\"max_stale_weather_threshold_in_hrs\x18\x01 \x01(\x05\x12&\n\x1e\x64\x65\x66\x61ult_weather_condition_code\x18\x02 \x01(\x05\x1a\x64\n\x11WindLevelSettings\x12\x19\n\x11wind_level1_speed\x18\x01 \x01(\x05\x12\x19\n\x11wind_level2_speed\x18\x02 \x01(\x05\x12\x19\n\x11wind_level3_speed\x18\x03 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_settings_dot_weather__alert__settings__pb2.DESCRIPTOR,pogoprotos_dot_map_dot_weather_dot_display__weather__pb2.DESCRIPTOR,pogoprotos_dot_map_dot_weather_dot_gameplay__weather__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_WEATHERSETTINGS_CONDITIONMAPSETTINGS = _descriptor.Descriptor(
  name='ConditionMapSettings',
  full_name='pogoprotos.settings.WeatherSettings.ConditionMapSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameplay_condition', full_name='pogoprotos.settings.WeatherSettings.ConditionMapSettings.gameplay_condition', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provider_enums', full_name='pogoprotos.settings.WeatherSettings.ConditionMapSettings.provider_enums', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=557,
  serialized_end=689,
)

_WEATHERSETTINGS_DISPLAYLEVELSETTINGS = _descriptor.Descriptor(
  name='DisplayLevelSettings',
  full_name='pogoprotos.settings.WeatherSettings.DisplayLevelSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='condition_enums', full_name='pogoprotos.settings.WeatherSettings.DisplayLevelSettings.condition_enums', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cloud_level', full_name='pogoprotos.settings.WeatherSettings.DisplayLevelSettings.cloud_level', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rain_level', full_name='pogoprotos.settings.WeatherSettings.DisplayLevelSettings.rain_level', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='snow_level', full_name='pogoprotos.settings.WeatherSettings.DisplayLevelSettings.snow_level', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fog_level', full_name='pogoprotos.settings.WeatherSettings.DisplayLevelSettings.fog_level', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='special_effect_level', full_name='pogoprotos.settings.WeatherSettings.DisplayLevelSettings.special_effect_level', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=692,
  serialized_end=1114,
)

_WEATHERSETTINGS_DISPLAYWEATHERSETTINGS_DISPLAYLEVELSETTINGS = _descriptor.Descriptor(
  name='DisplayLevelSettings',
  full_name='pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.DisplayLevelSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='condition_enums', full_name='pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.DisplayLevelSettings.condition_enums', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cloud_level', full_name='pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.DisplayLevelSettings.cloud_level', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rain_level', full_name='pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.DisplayLevelSettings.rain_level', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='snow_level', full_name='pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.DisplayLevelSettings.snow_level', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fog_level', full_name='pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.DisplayLevelSettings.fog_level', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='special_effect_level', full_name='pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.DisplayLevelSettings.special_effect_level', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=692,
  serialized_end=1114,
)

_WEATHERSETTINGS_DISPLAYWEATHERSETTINGS_WINDLEVELSETTINGS = _descriptor.Descriptor(
  name='WindLevelSettings',
  full_name='pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.WindLevelSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wind_level1_speed', full_name='pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.WindLevelSettings.wind_level1_speed', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wind_level2_speed', full_name='pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.WindLevelSettings.wind_level2_speed', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wind_level3_speed', full_name='pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.WindLevelSettings.wind_level3_speed', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1790,
  serialized_end=1890,
)

_WEATHERSETTINGS_DISPLAYWEATHERSETTINGS = _descriptor.Descriptor(
  name='DisplayWeatherSettings',
  full_name='pogoprotos.settings.WeatherSettings.DisplayWeatherSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='display_level_settings', full_name='pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.display_level_settings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wind_level_settings', full_name='pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.wind_level_settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_WEATHERSETTINGS_DISPLAYWEATHERSETTINGS_DISPLAYLEVELSETTINGS, _WEATHERSETTINGS_DISPLAYWEATHERSETTINGS_WINDLEVELSETTINGS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1117,
  serialized_end=1890,
)

_WEATHERSETTINGS_GAMEPLAYWEATHERSETTINGS_CONDITIONMAPSETTINGS = _descriptor.Descriptor(
  name='ConditionMapSettings',
  full_name='pogoprotos.settings.WeatherSettings.GameplayWeatherSettings.ConditionMapSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameplay_condition', full_name='pogoprotos.settings.WeatherSettings.GameplayWeatherSettings.ConditionMapSettings.gameplay_condition', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provider_enums', full_name='pogoprotos.settings.WeatherSettings.GameplayWeatherSettings.ConditionMapSettings.provider_enums', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=557,
  serialized_end=689,
)

_WEATHERSETTINGS_GAMEPLAYWEATHERSETTINGS = _descriptor.Descriptor(
  name='GameplayWeatherSettings',
  full_name='pogoprotos.settings.WeatherSettings.GameplayWeatherSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='condition_map', full_name='pogoprotos.settings.WeatherSettings.GameplayWeatherSettings.condition_map', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_speed_for_windy', full_name='pogoprotos.settings.WeatherSettings.GameplayWeatherSettings.min_speed_for_windy', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conditions_for_windy', full_name='pogoprotos.settings.WeatherSettings.GameplayWeatherSettings.conditions_for_windy', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_WEATHERSETTINGS_GAMEPLAYWEATHERSETTINGS_CONDITIONMAPSETTINGS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1893,
  serialized_end=2218,
)

_WEATHERSETTINGS_STALEWEATHERSETTINGS = _descriptor.Descriptor(
  name='StaleWeatherSettings',
  full_name='pogoprotos.settings.WeatherSettings.StaleWeatherSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_stale_weather_threshold_in_hrs', full_name='pogoprotos.settings.WeatherSettings.StaleWeatherSettings.max_stale_weather_threshold_in_hrs', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='default_weather_condition_code', full_name='pogoprotos.settings.WeatherSettings.StaleWeatherSettings.default_weather_condition_code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=2220,
  serialized_end=2326,
)

_WEATHERSETTINGS_WINDLEVELSETTINGS = _descriptor.Descriptor(
  name='WindLevelSettings',
  full_name='pogoprotos.settings.WeatherSettings.WindLevelSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wind_level1_speed', full_name='pogoprotos.settings.WeatherSettings.WindLevelSettings.wind_level1_speed', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wind_level2_speed', full_name='pogoprotos.settings.WeatherSettings.WindLevelSettings.wind_level2_speed', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wind_level3_speed', full_name='pogoprotos.settings.WeatherSettings.WindLevelSettings.wind_level3_speed', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1790,
  serialized_end=1890,
)

_WEATHERSETTINGS = _descriptor.Descriptor(
  name='WeatherSettings',
  full_name='pogoprotos.settings.WeatherSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameplay_settings', full_name='pogoprotos.settings.WeatherSettings.gameplay_settings', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='display_settings', full_name='pogoprotos.settings.WeatherSettings.display_settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alert_settings', full_name='pogoprotos.settings.WeatherSettings.alert_settings', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stale_settings', full_name='pogoprotos.settings.WeatherSettings.stale_settings', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_WEATHERSETTINGS_CONDITIONMAPSETTINGS, _WEATHERSETTINGS_DISPLAYLEVELSETTINGS, _WEATHERSETTINGS_DISPLAYWEATHERSETTINGS, _WEATHERSETTINGS_GAMEPLAYWEATHERSETTINGS, _WEATHERSETTINGS_STALEWEATHERSETTINGS, _WEATHERSETTINGS_WINDLEVELSETTINGS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=2428,
)

_WEATHERSETTINGS_CONDITIONMAPSETTINGS.fields_by_name['gameplay_condition'].enum_type = pogoprotos_dot_map_dot_weather_dot_gameplay__weather__pb2._GAMEPLAYWEATHER_WEATHERCONDITION
_WEATHERSETTINGS_CONDITIONMAPSETTINGS.containing_type = _WEATHERSETTINGS
_WEATHERSETTINGS_DISPLAYLEVELSETTINGS.fields_by_name['cloud_level'].enum_type = pogoprotos_dot_map_dot_weather_dot_display__weather__pb2._DISPLAYWEATHER_DISPLAYLEVEL
_WEATHERSETTINGS_DISPLAYLEVELSETTINGS.fields_by_name['rain_level'].enum_type = pogoprotos_dot_map_dot_weather_dot_display__weather__pb2._DISPLAYWEATHER_DISPLAYLEVEL
_WEATHERSETTINGS_DISPLAYLEVELSETTINGS.fields_by_name['snow_level'].enum_type = pogoprotos_dot_map_dot_weather_dot_display__weather__pb2._DISPLAYWEATHER_DISPLAYLEVEL
_WEATHERSETTINGS_DISPLAYLEVELSETTINGS.fields_by_name['fog_level'].enum_type = pogoprotos_dot_map_dot_weather_dot_display__weather__pb2._DISPLAYWEATHER_DISPLAYLEVEL
_WEATHERSETTINGS_DISPLAYLEVELSETTINGS.fields_by_name['special_effect_level'].enum_type = pogoprotos_dot_map_dot_weather_dot_display__weather__pb2._DISPLAYWEATHER_DISPLAYLEVEL
_WEATHERSETTINGS_DISPLAYLEVELSETTINGS.containing_type = _WEATHERSETTINGS
_WEATHERSETTINGS_DISPLAYWEATHERSETTINGS_DISPLAYLEVELSETTINGS.fields_by_name['cloud_level'].enum_type = pogoprotos_dot_map_dot_weather_dot_display__weather__pb2._DISPLAYWEATHER_DISPLAYLEVEL
_WEATHERSETTINGS_DISPLAYWEATHERSETTINGS_DISPLAYLEVELSETTINGS.fields_by_name['rain_level'].enum_type = pogoprotos_dot_map_dot_weather_dot_display__weather__pb2._DISPLAYWEATHER_DISPLAYLEVEL
_WEATHERSETTINGS_DISPLAYWEATHERSETTINGS_DISPLAYLEVELSETTINGS.fields_by_name['snow_level'].enum_type = pogoprotos_dot_map_dot_weather_dot_display__weather__pb2._DISPLAYWEATHER_DISPLAYLEVEL
_WEATHERSETTINGS_DISPLAYWEATHERSETTINGS_DISPLAYLEVELSETTINGS.fields_by_name['fog_level'].enum_type = pogoprotos_dot_map_dot_weather_dot_display__weather__pb2._DISPLAYWEATHER_DISPLAYLEVEL
_WEATHERSETTINGS_DISPLAYWEATHERSETTINGS_DISPLAYLEVELSETTINGS.fields_by_name['special_effect_level'].enum_type = pogoprotos_dot_map_dot_weather_dot_display__weather__pb2._DISPLAYWEATHER_DISPLAYLEVEL
_WEATHERSETTINGS_DISPLAYWEATHERSETTINGS_DISPLAYLEVELSETTINGS.containing_type = _WEATHERSETTINGS_DISPLAYWEATHERSETTINGS
_WEATHERSETTINGS_DISPLAYWEATHERSETTINGS_WINDLEVELSETTINGS.containing_type = _WEATHERSETTINGS_DISPLAYWEATHERSETTINGS
_WEATHERSETTINGS_DISPLAYWEATHERSETTINGS.fields_by_name['display_level_settings'].message_type = _WEATHERSETTINGS_DISPLAYWEATHERSETTINGS_DISPLAYLEVELSETTINGS
_WEATHERSETTINGS_DISPLAYWEATHERSETTINGS.fields_by_name['wind_level_settings'].message_type = _WEATHERSETTINGS_DISPLAYWEATHERSETTINGS_WINDLEVELSETTINGS
_WEATHERSETTINGS_DISPLAYWEATHERSETTINGS.containing_type = _WEATHERSETTINGS
_WEATHERSETTINGS_GAMEPLAYWEATHERSETTINGS_CONDITIONMAPSETTINGS.fields_by_name['gameplay_condition'].enum_type = pogoprotos_dot_map_dot_weather_dot_gameplay__weather__pb2._GAMEPLAYWEATHER_WEATHERCONDITION
_WEATHERSETTINGS_GAMEPLAYWEATHERSETTINGS_CONDITIONMAPSETTINGS.containing_type = _WEATHERSETTINGS_GAMEPLAYWEATHERSETTINGS
_WEATHERSETTINGS_GAMEPLAYWEATHERSETTINGS.fields_by_name['condition_map'].message_type = _WEATHERSETTINGS_GAMEPLAYWEATHERSETTINGS_CONDITIONMAPSETTINGS
_WEATHERSETTINGS_GAMEPLAYWEATHERSETTINGS.containing_type = _WEATHERSETTINGS
_WEATHERSETTINGS_STALEWEATHERSETTINGS.containing_type = _WEATHERSETTINGS
_WEATHERSETTINGS_WINDLEVELSETTINGS.containing_type = _WEATHERSETTINGS
_WEATHERSETTINGS.fields_by_name['gameplay_settings'].message_type = _WEATHERSETTINGS_GAMEPLAYWEATHERSETTINGS
_WEATHERSETTINGS.fields_by_name['display_settings'].message_type = _WEATHERSETTINGS_DISPLAYWEATHERSETTINGS
_WEATHERSETTINGS.fields_by_name['alert_settings'].message_type = pogoprotos_dot_settings_dot_weather__alert__settings__pb2._WEATHERALERTSETTINGS
_WEATHERSETTINGS.fields_by_name['stale_settings'].message_type = _WEATHERSETTINGS_STALEWEATHERSETTINGS
DESCRIPTOR.message_types_by_name['WeatherSettings'] = _WEATHERSETTINGS

WeatherSettings = _reflection.GeneratedProtocolMessageType('WeatherSettings', (_message.Message,), dict(

  ConditionMapSettings = _reflection.GeneratedProtocolMessageType('ConditionMapSettings', (_message.Message,), dict(
    DESCRIPTOR = _WEATHERSETTINGS_CONDITIONMAPSETTINGS,
    __module__ = 'pogoprotos.settings.weather_settings_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.settings.WeatherSettings.ConditionMapSettings)
    ))
  ,

  DisplayLevelSettings = _reflection.GeneratedProtocolMessageType('DisplayLevelSettings', (_message.Message,), dict(
    DESCRIPTOR = _WEATHERSETTINGS_DISPLAYLEVELSETTINGS,
    __module__ = 'pogoprotos.settings.weather_settings_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.settings.WeatherSettings.DisplayLevelSettings)
    ))
  ,

  DisplayWeatherSettings = _reflection.GeneratedProtocolMessageType('DisplayWeatherSettings', (_message.Message,), dict(

    DisplayLevelSettings = _reflection.GeneratedProtocolMessageType('DisplayLevelSettings', (_message.Message,), dict(
      DESCRIPTOR = _WEATHERSETTINGS_DISPLAYWEATHERSETTINGS_DISPLAYLEVELSETTINGS,
      __module__ = 'pogoprotos.settings.weather_settings_pb2'
      # @@protoc_insertion_point(class_scope:pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.DisplayLevelSettings)
      ))
    ,

    WindLevelSettings = _reflection.GeneratedProtocolMessageType('WindLevelSettings', (_message.Message,), dict(
      DESCRIPTOR = _WEATHERSETTINGS_DISPLAYWEATHERSETTINGS_WINDLEVELSETTINGS,
      __module__ = 'pogoprotos.settings.weather_settings_pb2'
      # @@protoc_insertion_point(class_scope:pogoprotos.settings.WeatherSettings.DisplayWeatherSettings.WindLevelSettings)
      ))
    ,
    DESCRIPTOR = _WEATHERSETTINGS_DISPLAYWEATHERSETTINGS,
    __module__ = 'pogoprotos.settings.weather_settings_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.settings.WeatherSettings.DisplayWeatherSettings)
    ))
  ,

  GameplayWeatherSettings = _reflection.GeneratedProtocolMessageType('GameplayWeatherSettings', (_message.Message,), dict(

    ConditionMapSettings = _reflection.GeneratedProtocolMessageType('ConditionMapSettings', (_message.Message,), dict(
      DESCRIPTOR = _WEATHERSETTINGS_GAMEPLAYWEATHERSETTINGS_CONDITIONMAPSETTINGS,
      __module__ = 'pogoprotos.settings.weather_settings_pb2'
      # @@protoc_insertion_point(class_scope:pogoprotos.settings.WeatherSettings.GameplayWeatherSettings.ConditionMapSettings)
      ))
    ,
    DESCRIPTOR = _WEATHERSETTINGS_GAMEPLAYWEATHERSETTINGS,
    __module__ = 'pogoprotos.settings.weather_settings_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.settings.WeatherSettings.GameplayWeatherSettings)
    ))
  ,

  StaleWeatherSettings = _reflection.GeneratedProtocolMessageType('StaleWeatherSettings', (_message.Message,), dict(
    DESCRIPTOR = _WEATHERSETTINGS_STALEWEATHERSETTINGS,
    __module__ = 'pogoprotos.settings.weather_settings_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.settings.WeatherSettings.StaleWeatherSettings)
    ))
  ,

  WindLevelSettings = _reflection.GeneratedProtocolMessageType('WindLevelSettings', (_message.Message,), dict(
    DESCRIPTOR = _WEATHERSETTINGS_WINDLEVELSETTINGS,
    __module__ = 'pogoprotos.settings.weather_settings_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.settings.WeatherSettings.WindLevelSettings)
    ))
  ,
  DESCRIPTOR = _WEATHERSETTINGS,
  __module__ = 'pogoprotos.settings.weather_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.WeatherSettings)
  ))
_sym_db.RegisterMessage(WeatherSettings)
_sym_db.RegisterMessage(WeatherSettings.ConditionMapSettings)
_sym_db.RegisterMessage(WeatherSettings.DisplayLevelSettings)
_sym_db.RegisterMessage(WeatherSettings.DisplayWeatherSettings)
_sym_db.RegisterMessage(WeatherSettings.DisplayWeatherSettings.DisplayLevelSettings)
_sym_db.RegisterMessage(WeatherSettings.DisplayWeatherSettings.WindLevelSettings)
_sym_db.RegisterMessage(WeatherSettings.GameplayWeatherSettings)
_sym_db.RegisterMessage(WeatherSettings.GameplayWeatherSettings.ConditionMapSettings)
_sym_db.RegisterMessage(WeatherSettings.StaleWeatherSettings)
_sym_db.RegisterMessage(WeatherSettings.WindLevelSettings)


# @@protoc_insertion_point(module_scope)
