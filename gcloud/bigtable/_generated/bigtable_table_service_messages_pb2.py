# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/bigtable/admin/table/v1/bigtable_table_service_messages.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gcloud.bigtable._generated import bigtable_table_data_pb2 as google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/bigtable/admin/table/v1/bigtable_table_service_messages.proto',
  package='google.bigtable.admin.table.v1',
  syntax='proto3',
  serialized_pb=b'\nDgoogle/bigtable/admin/table/v1/bigtable_table_service_messages.proto\x12\x1egoogle.bigtable.admin.table.v1\x1a\x38google/bigtable/admin/table/v1/bigtable_table_data.proto\"\x86\x01\n\x12\x43reateTableRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08table_id\x18\x02 \x01(\t\x12\x34\n\x05table\x18\x03 \x01(\x0b\x32%.google.bigtable.admin.table.v1.Table\x12\x1a\n\x12initial_split_keys\x18\x04 \x03(\t\"!\n\x11ListTablesRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"K\n\x12ListTablesResponse\x12\x35\n\x06tables\x18\x01 \x03(\x0b\x32%.google.bigtable.admin.table.v1.Table\"\x1f\n\x0fGetTableRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\"\n\x12\x44\x65leteTableRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"2\n\x12RenameTableRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06new_id\x18\x02 \x01(\t\"\x88\x01\n\x19\x43reateColumnFamilyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10\x63olumn_family_id\x18\x02 \x01(\t\x12\x43\n\rcolumn_family\x18\x03 \x01(\x0b\x32,.google.bigtable.admin.table.v1.ColumnFamily\")\n\x19\x44\x65leteColumnFamilyRequest\x12\x0c\n\x04name\x18\x01 \x01(\tBI\n\"com.google.bigtable.admin.table.v1B!BigtableTableServiceMessagesProtoP\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__data__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CREATETABLEREQUEST = _descriptor.Descriptor(
  name='CreateTableRequest',
  full_name='google.bigtable.admin.table.v1.CreateTableRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.bigtable.admin.table.v1.CreateTableRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table_id', full_name='google.bigtable.admin.table.v1.CreateTableRequest.table_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table', full_name='google.bigtable.admin.table.v1.CreateTableRequest.table', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initial_split_keys', full_name='google.bigtable.admin.table.v1.CreateTableRequest.initial_split_keys', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=163,
  serialized_end=297,
)


_LISTTABLESREQUEST = _descriptor.Descriptor(
  name='ListTablesRequest',
  full_name='google.bigtable.admin.table.v1.ListTablesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.bigtable.admin.table.v1.ListTablesRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=299,
  serialized_end=332,
)


_LISTTABLESRESPONSE = _descriptor.Descriptor(
  name='ListTablesResponse',
  full_name='google.bigtable.admin.table.v1.ListTablesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tables', full_name='google.bigtable.admin.table.v1.ListTablesResponse.tables', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=334,
  serialized_end=409,
)


_GETTABLEREQUEST = _descriptor.Descriptor(
  name='GetTableRequest',
  full_name='google.bigtable.admin.table.v1.GetTableRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.bigtable.admin.table.v1.GetTableRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=411,
  serialized_end=442,
)


_DELETETABLEREQUEST = _descriptor.Descriptor(
  name='DeleteTableRequest',
  full_name='google.bigtable.admin.table.v1.DeleteTableRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.bigtable.admin.table.v1.DeleteTableRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=444,
  serialized_end=478,
)


_RENAMETABLEREQUEST = _descriptor.Descriptor(
  name='RenameTableRequest',
  full_name='google.bigtable.admin.table.v1.RenameTableRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.bigtable.admin.table.v1.RenameTableRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_id', full_name='google.bigtable.admin.table.v1.RenameTableRequest.new_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=480,
  serialized_end=530,
)


_CREATECOLUMNFAMILYREQUEST = _descriptor.Descriptor(
  name='CreateColumnFamilyRequest',
  full_name='google.bigtable.admin.table.v1.CreateColumnFamilyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.bigtable.admin.table.v1.CreateColumnFamilyRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='column_family_id', full_name='google.bigtable.admin.table.v1.CreateColumnFamilyRequest.column_family_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='column_family', full_name='google.bigtable.admin.table.v1.CreateColumnFamilyRequest.column_family', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=533,
  serialized_end=669,
)


_DELETECOLUMNFAMILYREQUEST = _descriptor.Descriptor(
  name='DeleteColumnFamilyRequest',
  full_name='google.bigtable.admin.table.v1.DeleteColumnFamilyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.bigtable.admin.table.v1.DeleteColumnFamilyRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=671,
  serialized_end=712,
)

_CREATETABLEREQUEST.fields_by_name['table'].message_type = google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__data__pb2._TABLE
_LISTTABLESRESPONSE.fields_by_name['tables'].message_type = google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__data__pb2._TABLE
_CREATECOLUMNFAMILYREQUEST.fields_by_name['column_family'].message_type = google_dot_bigtable_dot_admin_dot_table_dot_v1_dot_bigtable__table__data__pb2._COLUMNFAMILY
DESCRIPTOR.message_types_by_name['CreateTableRequest'] = _CREATETABLEREQUEST
DESCRIPTOR.message_types_by_name['ListTablesRequest'] = _LISTTABLESREQUEST
DESCRIPTOR.message_types_by_name['ListTablesResponse'] = _LISTTABLESRESPONSE
DESCRIPTOR.message_types_by_name['GetTableRequest'] = _GETTABLEREQUEST
DESCRIPTOR.message_types_by_name['DeleteTableRequest'] = _DELETETABLEREQUEST
DESCRIPTOR.message_types_by_name['RenameTableRequest'] = _RENAMETABLEREQUEST
DESCRIPTOR.message_types_by_name['CreateColumnFamilyRequest'] = _CREATECOLUMNFAMILYREQUEST
DESCRIPTOR.message_types_by_name['DeleteColumnFamilyRequest'] = _DELETECOLUMNFAMILYREQUEST

CreateTableRequest = _reflection.GeneratedProtocolMessageType('CreateTableRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATETABLEREQUEST,
  __module__ = 'google.bigtable.admin.table.v1.bigtable_table_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.table.v1.CreateTableRequest)
  ))
_sym_db.RegisterMessage(CreateTableRequest)

ListTablesRequest = _reflection.GeneratedProtocolMessageType('ListTablesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTTABLESREQUEST,
  __module__ = 'google.bigtable.admin.table.v1.bigtable_table_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.table.v1.ListTablesRequest)
  ))
_sym_db.RegisterMessage(ListTablesRequest)

ListTablesResponse = _reflection.GeneratedProtocolMessageType('ListTablesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTTABLESRESPONSE,
  __module__ = 'google.bigtable.admin.table.v1.bigtable_table_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.table.v1.ListTablesResponse)
  ))
_sym_db.RegisterMessage(ListTablesResponse)

GetTableRequest = _reflection.GeneratedProtocolMessageType('GetTableRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTABLEREQUEST,
  __module__ = 'google.bigtable.admin.table.v1.bigtable_table_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.table.v1.GetTableRequest)
  ))
_sym_db.RegisterMessage(GetTableRequest)

DeleteTableRequest = _reflection.GeneratedProtocolMessageType('DeleteTableRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETETABLEREQUEST,
  __module__ = 'google.bigtable.admin.table.v1.bigtable_table_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.table.v1.DeleteTableRequest)
  ))
_sym_db.RegisterMessage(DeleteTableRequest)

RenameTableRequest = _reflection.GeneratedProtocolMessageType('RenameTableRequest', (_message.Message,), dict(
  DESCRIPTOR = _RENAMETABLEREQUEST,
  __module__ = 'google.bigtable.admin.table.v1.bigtable_table_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.table.v1.RenameTableRequest)
  ))
_sym_db.RegisterMessage(RenameTableRequest)

CreateColumnFamilyRequest = _reflection.GeneratedProtocolMessageType('CreateColumnFamilyRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATECOLUMNFAMILYREQUEST,
  __module__ = 'google.bigtable.admin.table.v1.bigtable_table_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.table.v1.CreateColumnFamilyRequest)
  ))
_sym_db.RegisterMessage(CreateColumnFamilyRequest)

DeleteColumnFamilyRequest = _reflection.GeneratedProtocolMessageType('DeleteColumnFamilyRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETECOLUMNFAMILYREQUEST,
  __module__ = 'google.bigtable.admin.table.v1.bigtable_table_service_messages_pb2'
  # @@protoc_insertion_point(class_scope:google.bigtable.admin.table.v1.DeleteColumnFamilyRequest)
  ))
_sym_db.RegisterMessage(DeleteColumnFamilyRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), b'\n\"com.google.bigtable.admin.table.v1B!BigtableTableServiceMessagesProtoP\001')
import abc
from grpc.beta import implementations as beta_implementations
from grpc.early_adopter import implementations as early_adopter_implementations
from grpc.framework.alpha import utilities as alpha_utilities
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
