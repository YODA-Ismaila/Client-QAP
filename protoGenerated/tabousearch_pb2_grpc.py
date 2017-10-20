# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import messages_pb2 as messages__pb2


class TabouSearchServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.InitTransaction = channel.unary_unary(
        '/ts.TabouSearchService/InitTransaction',
        request_serializer=messages__pb2.InitTransactionRequest.SerializeToString,
        response_deserializer=messages__pb2.MultiFitnessResponse.FromString,
        )
    self.SendFitness = channel.unary_unary(
        '/ts.TabouSearchService/SendFitness',
        request_serializer=messages__pb2.MultiFitnessRequest.SerializeToString,
        response_deserializer=messages__pb2.MultiFitnessResponse.FromString,
        )
    self.StopTransaction = channel.unary_unary(
        '/ts.TabouSearchService/StopTransaction',
        request_serializer=messages__pb2.StopRequest.SerializeToString,
        response_deserializer=messages__pb2.StopResponse.FromString,
        )


class TabouSearchServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def InitTransaction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendFitness(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopTransaction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TabouSearchServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'InitTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.InitTransaction,
          request_deserializer=messages__pb2.InitTransactionRequest.FromString,
          response_serializer=messages__pb2.MultiFitnessResponse.SerializeToString,
      ),
      'SendFitness': grpc.unary_unary_rpc_method_handler(
          servicer.SendFitness,
          request_deserializer=messages__pb2.MultiFitnessRequest.FromString,
          response_serializer=messages__pb2.MultiFitnessResponse.SerializeToString,
      ),
      'StopTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.StopTransaction,
          request_deserializer=messages__pb2.StopRequest.FromString,
          response_serializer=messages__pb2.StopResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ts.TabouSearchService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
