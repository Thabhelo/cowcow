# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: reward.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'reward.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0creward.proto\x12\x06\x63owcow\"(\n\x0e\x42\x61lanceRequest\x12\x16\n\x0e\x63ontributor_id\x18\x01 \x01(\t\"M\n\x0f\x42\x61lanceResponse\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\r\x12\x14\n\x0ctotal_earned\x18\x02 \x01(\r\x12\x13\n\x0btotal_spent\x18\x03 \x01(\r\"t\n\x0eHistoryRequest\x12\x16\n\x0e\x63ontributor_id\x18\x01 \x01(\t\x12\x17\n\nstart_time\x18\x02 \x01(\x04H\x00\x88\x01\x01\x12\x15\n\x08\x65nd_time\x18\x03 \x01(\x04H\x01\x88\x01\x01\x42\r\n\x0b_start_timeB\x0b\n\t_end_time\"\xe5\x01\n\x0bTransaction\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12&\n\x04type\x18\x02 \x01(\x0e\x32\x18.cowcow.Transaction.Type\x12\x0e\n\x06\x61mount\x18\x03 \x01(\r\x12\x11\n\ttimestamp\x18\x04 \x01(\x04\x12\x18\n\x0b\x64\x65scription\x18\x05 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0crecording_id\x18\x06 \x01(\tH\x01\x88\x01\x01\"\x1d\n\x04Type\x12\n\n\x06\x45\x41RNED\x10\x00\x12\t\n\x05SPENT\x10\x01\x42\x0e\n\x0c_descriptionB\x0f\n\r_recording_id2\x8b\x01\n\rRewardService\x12=\n\nGetBalance\x12\x16.cowcow.BalanceRequest\x1a\x17.cowcow.BalanceResponse\x12;\n\nGetHistory\x12\x16.cowcow.HistoryRequest\x1a\x13.cowcow.Transaction0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reward_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BALANCEREQUEST']._serialized_start=24
  _globals['_BALANCEREQUEST']._serialized_end=64
  _globals['_BALANCERESPONSE']._serialized_start=66
  _globals['_BALANCERESPONSE']._serialized_end=143
  _globals['_HISTORYREQUEST']._serialized_start=145
  _globals['_HISTORYREQUEST']._serialized_end=261
  _globals['_TRANSACTION']._serialized_start=264
  _globals['_TRANSACTION']._serialized_end=493
  _globals['_TRANSACTION_TYPE']._serialized_start=431
  _globals['_TRANSACTION_TYPE']._serialized_end=460
  _globals['_REWARDSERVICE']._serialized_start=496
  _globals['_REWARDSERVICE']._serialized_end=635
# @@protoc_insertion_point(module_scope)
