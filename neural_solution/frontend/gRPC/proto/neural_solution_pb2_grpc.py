# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import neural_solution.frontend.gRPC.proto.neural_solution_pb2 as neural__solution__pb2


class TaskServiceStub(object):
    """Interface exported by the server
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/neural_solution.TaskService/Ping',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=neural__solution__pb2.ResponsePingMessage.FromString,
                )
        self.SubmitTask = channel.unary_unary(
                '/neural_solution.TaskService/SubmitTask',
                request_serializer=neural__solution__pb2.Task.SerializeToString,
                response_deserializer=neural__solution__pb2.TaskResponse.FromString,
                )
        self.GetTaskById = channel.unary_unary(
                '/neural_solution.TaskService/GetTaskById',
                request_serializer=neural__solution__pb2.TaskId.SerializeToString,
                response_deserializer=neural__solution__pb2.TaskStatus.FromString,
                )
        self.QueryTaskResult = channel.unary_unary(
                '/neural_solution.TaskService/QueryTaskResult',
                request_serializer=neural__solution__pb2.TaskId.SerializeToString,
                response_deserializer=neural__solution__pb2.ResponseTaskResult.FromString,
                )


class TaskServiceServicer(object):
    """Interface exported by the server
    """

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTaskById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryTaskResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TaskServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=neural__solution__pb2.ResponsePingMessage.SerializeToString,
            ),
            'SubmitTask': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitTask,
                    request_deserializer=neural__solution__pb2.Task.FromString,
                    response_serializer=neural__solution__pb2.TaskResponse.SerializeToString,
            ),
            'GetTaskById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTaskById,
                    request_deserializer=neural__solution__pb2.TaskId.FromString,
                    response_serializer=neural__solution__pb2.TaskStatus.SerializeToString,
            ),
            'QueryTaskResult': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryTaskResult,
                    request_deserializer=neural__solution__pb2.TaskId.FromString,
                    response_serializer=neural__solution__pb2.ResponseTaskResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'neural_solution.TaskService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TaskService(object):
    """Interface exported by the server
    """

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/neural_solution.TaskService/Ping',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            neural__solution__pb2.ResponsePingMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubmitTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/neural_solution.TaskService/SubmitTask',
            neural__solution__pb2.Task.SerializeToString,
            neural__solution__pb2.TaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTaskById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/neural_solution.TaskService/GetTaskById',
            neural__solution__pb2.TaskId.SerializeToString,
            neural__solution__pb2.TaskStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryTaskResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/neural_solution.TaskService/QueryTaskResult',
            neural__solution__pb2.TaskId.SerializeToString,
            neural__solution__pb2.ResponseTaskResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
