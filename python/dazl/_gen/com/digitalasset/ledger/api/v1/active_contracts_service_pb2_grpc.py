# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import active_contracts_service_pb2 as com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_active__contracts__service__pb2


class ActiveContractsServiceStub(object):
  """Allows clients to initialize themselves according to a fairly recent state of the ledger without reading through all transactions that were committed since the ledger's creation.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetActiveContracts = channel.unary_stream(
        '/com.digitalasset.ledger.api.v1.ActiveContractsService/GetActiveContracts',
        request_serializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_active__contracts__service__pb2.GetActiveContractsRequest.SerializeToString,
        response_deserializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_active__contracts__service__pb2.GetActiveContractsResponse.FromString,
        )


class ActiveContractsServiceServicer(object):
  """Allows clients to initialize themselves according to a fairly recent state of the ledger without reading through all transactions that were committed since the ledger's creation.
  """

  def GetActiveContracts(self, request, context):
    """Returns a stream of the latest snapshot of active contracts. Getting an empty stream means that the active contracts set is empty and the client should listen to transactions using ``LEDGER_BEGIN``.
    Clients SHOULD NOT assume that the set of active contracts they receive reflects the state at the ledger end.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ActiveContractsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetActiveContracts': grpc.unary_stream_rpc_method_handler(
          servicer.GetActiveContracts,
          request_deserializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_active__contracts__service__pb2.GetActiveContractsRequest.FromString,
          response_serializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_active__contracts__service__pb2.GetActiveContractsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.digitalasset.ledger.api.v1.ActiveContractsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
