# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import package_management_service_pb2 as com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_admin_dot_package__management__service__pb2


class PackageManagementServiceStub(object):
  """Status: experimental interface, will change before it is deemed production
  ready

  Query the DAML-LF packages supported by the ledger participant and upload
  DAR files. We use 'backing participant' to refer to this specific participant
  in the methods of this API.
  When the participant is run in mode requiring authentication, all the calls 
  in this interface will respond with UNAUTHENTICATED, if the caller fails
  to provide a valid access token, and will respond with PERMISSION_DENIED, if
  the claims in the token are insufficient to perform a given operation.
  Subsequently, only specific errors of individual calls not related to 
  authorization will be described.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListKnownPackages = channel.unary_unary(
        '/com.digitalasset.ledger.api.v1.admin.PackageManagementService/ListKnownPackages',
        request_serializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_admin_dot_package__management__service__pb2.ListKnownPackagesRequest.SerializeToString,
        response_deserializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_admin_dot_package__management__service__pb2.ListKnownPackagesResponse.FromString,
        )
    self.UploadDarFile = channel.unary_unary(
        '/com.digitalasset.ledger.api.v1.admin.PackageManagementService/UploadDarFile',
        request_serializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_admin_dot_package__management__service__pb2.UploadDarFileRequest.SerializeToString,
        response_deserializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_admin_dot_package__management__service__pb2.UploadDarFileResponse.FromString,
        )


class PackageManagementServiceServicer(object):
  """Status: experimental interface, will change before it is deemed production
  ready

  Query the DAML-LF packages supported by the ledger participant and upload
  DAR files. We use 'backing participant' to refer to this specific participant
  in the methods of this API.
  When the participant is run in mode requiring authentication, all the calls 
  in this interface will respond with UNAUTHENTICATED, if the caller fails
  to provide a valid access token, and will respond with PERMISSION_DENIED, if
  the claims in the token are insufficient to perform a given operation.
  Subsequently, only specific errors of individual calls not related to 
  authorization will be described.
  """

  def ListKnownPackages(self, request, context):
    """Returns the details of all DAML-LF packages known to the backing
    participant.
    This request will always succeed.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadDarFile(self, request, context):
    """Upload a DAR file to the backing participant.
    Depending on the ledger implementation this might also make the package 
    available on the whole ledger. This call might not be supported by some 
    ledger implementations. Canton could be an example, where uploading a DAR
    is not sufficient to render it usable, it must be activated first.
    This call may:
    - Succeed, if the package was successfully uploaded, or if the same package
    was already uploaded before. 
    - Respond with UNIMPLEMENTED, if DAR package uploading is not supported by
    the backing participant.
    - Respond with INVALID_ARGUMENT, if the DAR file is too big or malformed.
    The maximum supported size is implementation specific.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PackageManagementServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListKnownPackages': grpc.unary_unary_rpc_method_handler(
          servicer.ListKnownPackages,
          request_deserializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_admin_dot_package__management__service__pb2.ListKnownPackagesRequest.FromString,
          response_serializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_admin_dot_package__management__service__pb2.ListKnownPackagesResponse.SerializeToString,
      ),
      'UploadDarFile': grpc.unary_unary_rpc_method_handler(
          servicer.UploadDarFile,
          request_deserializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_admin_dot_package__management__service__pb2.UploadDarFileRequest.FromString,
          response_serializer=com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_admin_dot_package__management__service__pb2.UploadDarFileResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.digitalasset.ledger.api.v1.admin.PackageManagementService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
