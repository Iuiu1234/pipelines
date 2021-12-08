# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: third_party/py/google_cloud_pipeline_components/google_cloud_pipeline_components/proto/gcp_resources.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='third_party/py/google_cloud_pipeline_components/google_cloud_pipeline_components/proto/gcp_resources.proto',
  package='gcp_launcher',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\njthird_party/py/google_cloud_pipeline_components/google_cloud_pipeline_components/proto/gcp_resources.proto\x12\x0cgcp_launcher\x1a\x17google/rpc/status.proto\"\xe0\x01\n\x0cGcpResources\x12\x36\n\tresources\x18\x01 \x03(\x0b\x32#.gcp_launcher.GcpResources.Resource\x1a\x97\x01\n\x08Resource\x12\x1a\n\rresource_type\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0cresource_uri\x18\x02 \x01(\tH\x01\x88\x01\x01\x12!\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12\x0e\n\x06labels\x18\x04 \x03(\tB\x10\n\x0e_resource_typeB\x0f\n\r_resource_urib\x06proto3'
  ,
  dependencies=[google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GCPRESOURCES_RESOURCE = _descriptor.Descriptor(
  name='Resource',
  full_name='gcp_launcher.GcpResources.Resource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='gcp_launcher.GcpResources.Resource.resource_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_uri', full_name='gcp_launcher.GcpResources.Resource.resource_uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='gcp_launcher.GcpResources.Resource.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='gcp_launcher.GcpResources.Resource.labels', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_resource_type', full_name='gcp_launcher.GcpResources.Resource._resource_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_resource_uri', full_name='gcp_launcher.GcpResources.Resource._resource_uri',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=223,
  serialized_end=374,
)

_GCPRESOURCES = _descriptor.Descriptor(
  name='GcpResources',
  full_name='gcp_launcher.GcpResources',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='gcp_launcher.GcpResources.resources', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GCPRESOURCES_RESOURCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=374,
)

# pytype: disable=module-attr
_GCPRESOURCES_RESOURCE.fields_by_name['error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_GCPRESOURCES_RESOURCE.containing_type = _GCPRESOURCES
_GCPRESOURCES_RESOURCE.oneofs_by_name['_resource_type'].fields.append(
  _GCPRESOURCES_RESOURCE.fields_by_name['resource_type'])
_GCPRESOURCES_RESOURCE.fields_by_name['resource_type'].containing_oneof = _GCPRESOURCES_RESOURCE.oneofs_by_name['_resource_type']
_GCPRESOURCES_RESOURCE.oneofs_by_name['_resource_uri'].fields.append(
  _GCPRESOURCES_RESOURCE.fields_by_name['resource_uri'])
_GCPRESOURCES_RESOURCE.fields_by_name['resource_uri'].containing_oneof = _GCPRESOURCES_RESOURCE.oneofs_by_name['_resource_uri']
_GCPRESOURCES.fields_by_name['resources'].message_type = _GCPRESOURCES_RESOURCE
DESCRIPTOR.message_types_by_name['GcpResources'] = _GCPRESOURCES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GcpResources = _reflection.GeneratedProtocolMessageType('GcpResources', (_message.Message,), {

  'Resource' : _reflection.GeneratedProtocolMessageType('Resource', (_message.Message,), {
    'DESCRIPTOR' : _GCPRESOURCES_RESOURCE,
    '__module__' : 'third_party.py.google_cloud_pipeline_components.google_cloud_pipeline_components.proto.gcp_resources_pb2'
    # @@protoc_insertion_point(class_scope:gcp_launcher.GcpResources.Resource)
    })
  ,
  'DESCRIPTOR' : _GCPRESOURCES,
  '__module__' : 'third_party.py.google_cloud_pipeline_components.google_cloud_pipeline_components.proto.gcp_resources_pb2'
  # @@protoc_insertion_point(class_scope:gcp_launcher.GcpResources)
  })
_sym_db.RegisterMessage(GcpResources)
_sym_db.RegisterMessage(GcpResources.Resource)


# @@protoc_insertion_point(module_scope)
