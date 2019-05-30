# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import time_service_pb2 as com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_testing_dot_time__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class TimeServiceStub(object):
  """Optional service, exposed for testing static time scenarios.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetTime = channel.unary_stream(
        '/com.digitalasset.ledger.api.v1.testing.TimeService/GetTime',
        request_serializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_testing_dot_time__service__pb2.GetTimeRequest.SerializeToString,
        response_deserializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_testing_dot_time__service__pb2.GetTimeResponse.FromString,
        )
    self.SetTime = channel.unary_unary(
        '/com.digitalasset.ledger.api.v1.testing.TimeService/SetTime',
        request_serializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_testing_dot_time__service__pb2.SetTimeRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class TimeServiceServicer(object):
  """Optional service, exposed for testing static time scenarios.
  """

  def GetTime(self, request, context):
    """Returns a stream of time updates.
    Always returns at least one response, where the first one is the current time.
    Subsequent responses are emitted whenever the ledger server's time is updated.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetTime(self, request, context):
    """Allows clients to change the ledger's clock in an atomic get-and-set operation.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TimeServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetTime': grpc.unary_stream_rpc_method_handler(
          servicer.GetTime,
          request_deserializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_testing_dot_time__service__pb2.GetTimeRequest.FromString,
          response_serializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_testing_dot_time__service__pb2.GetTimeResponse.SerializeToString,
      ),
      'SetTime': grpc.unary_unary_rpc_method_handler(
          servicer.SetTime,
          request_deserializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_testing_dot_time__service__pb2.SetTimeRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.digitalasset.ledger.api.v1.testing.TimeService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
