# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: opentelemetry/proto/collector/logs/v1/logs_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from opentelemetry.proto.logs.v1 import logs_pb2 as opentelemetry_dot_proto_dot_logs_dot_v1_dot_logs__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8opentelemetry/proto/collector/logs/v1/logs_service.proto\x12%opentelemetry.proto.collector.logs.v1\x1a&opentelemetry/proto/logs/v1/logs.proto\"\\\n\x18\x45xportLogsServiceRequest\x12@\n\rresource_logs\x18\x01 \x03(\x0b\x32).opentelemetry.proto.logs.v1.ResourceLogs\"u\n\x19\x45xportLogsServiceResponse\x12X\n\x0fpartial_success\x18\x01 \x01(\x0b\x32?.opentelemetry.proto.collector.logs.v1.ExportLogsPartialSuccess\"O\n\x18\x45xportLogsPartialSuccess\x12\x1c\n\x14rejected_log_records\x18\x01 \x01(\x03\x12\x15\n\rerror_message\x18\x02 \x01(\t2\x9d\x01\n\x0bLogsService\x12\x8d\x01\n\x06\x45xport\x12?.opentelemetry.proto.collector.logs.v1.ExportLogsServiceRequest\x1a@.opentelemetry.proto.collector.logs.v1.ExportLogsServiceResponse\"\x00\x42\x98\x01\n(io.opentelemetry.proto.collector.logs.v1B\x10LogsServiceProtoP\x01Z0go.opentelemetry.io/proto/otlp/collector/logs/v1\xaa\x02%OpenTelemetry.Proto.Collector.Logs.V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'opentelemetry.proto.collector.logs.v1.logs_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(io.opentelemetry.proto.collector.logs.v1B\020LogsServiceProtoP\001Z0go.opentelemetry.io/proto/otlp/collector/logs/v1\252\002%OpenTelemetry.Proto.Collector.Logs.V1'
  _globals['_EXPORTLOGSSERVICEREQUEST']._serialized_start=139
  _globals['_EXPORTLOGSSERVICEREQUEST']._serialized_end=231
  _globals['_EXPORTLOGSSERVICERESPONSE']._serialized_start=233
  _globals['_EXPORTLOGSSERVICERESPONSE']._serialized_end=350
  _globals['_EXPORTLOGSPARTIALSUCCESS']._serialized_start=352
  _globals['_EXPORTLOGSPARTIALSUCCESS']._serialized_end=431
  _globals['_LOGSSERVICE']._serialized_start=434
  _globals['_LOGSSERVICE']._serialized_end=591
# @@protoc_insertion_point(module_scope)
