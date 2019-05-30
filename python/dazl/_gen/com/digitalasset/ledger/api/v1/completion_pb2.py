# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/ledger/api/v1/completion.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import trace_context_pb2 as com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/digitalasset/ledger/api/v1/completion.proto',
  package='com.digitalasset.ledger.api.v1',
  syntax='proto3',
  serialized_options=_b('\n\036com.digitalasset.ledger.api.v1B\024CompletionOuterClass'),
  serialized_pb=_b('\n/com/digitalasset/ledger/api/v1/completion.proto\x12\x1e\x63om.digitalasset.ledger.api.v1\x1a\x32\x63om/digitalasset/ledger/api/v1/trace_context.proto\x1a\x17google/rpc/status.proto\"\xa2\x01\n\nCompletion\x12\x12\n\ncommand_id\x18\x01 \x01(\t\x12\"\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.Status\x12\x16\n\x0etransaction_id\x18\x03 \x01(\t\x12\x44\n\rtrace_context\x18\xe8\x07 \x01(\x0b\x32,.com.digitalasset.ledger.api.v1.TraceContextB6\n\x1e\x63om.digitalasset.ledger.api.v1B\x14\x43ompletionOuterClassb\x06proto3')
  ,
  dependencies=[com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_COMPLETION = _descriptor.Descriptor(
  name='Completion',
  full_name='com.digitalasset.ledger.api.v1.Completion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command_id', full_name='com.digitalasset.ledger.api.v1.Completion.command_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='com.digitalasset.ledger.api.v1.Completion.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='com.digitalasset.ledger.api.v1.Completion.transaction_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_context', full_name='com.digitalasset.ledger.api.v1.Completion.trace_context', index=3,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  ],
  serialized_start=161,
  serialized_end=323,
)

_COMPLETION.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_COMPLETION.fields_by_name['trace_context'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2._TRACECONTEXT
DESCRIPTOR.message_types_by_name['Completion'] = _COMPLETION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Completion = _reflection.GeneratedProtocolMessageType('Completion', (_message.Message,), dict(
  DESCRIPTOR = _COMPLETION,
  __module__ = 'com.digitalasset.ledger.api.v1.completion_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.Completion)
  ))
_sym_db.RegisterMessage(Completion)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
