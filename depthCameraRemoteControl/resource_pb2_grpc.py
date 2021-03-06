# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import resource_pb2 as resource__pb2


class ResourceServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UploadImage = channel.unary_unary(
        '/whale.resource.proto.ResourceService/UploadImage',
        request_serializer=resource__pb2.UploadFileReq.SerializeToString,
        response_deserializer=resource__pb2.UploadFileResp.FromString,
        )
    self.UploadModel = channel.unary_unary(
        '/whale.resource.proto.ResourceService/UploadModel',
        request_serializer=resource__pb2.UploadModelReq.SerializeToString,
        response_deserializer=resource__pb2.UploadFileResp.FromString,
        )
    self.UploadFaceImage = channel.unary_unary(
        '/whale.resource.proto.ResourceService/UploadFaceImage',
        request_serializer=resource__pb2.UploadFaceImageReq.SerializeToString,
        response_deserializer=resource__pb2.UploadFileResp.FromString,
        )
    self.GetFileInfo = channel.unary_unary(
        '/whale.resource.proto.ResourceService/GetFileInfo',
        request_serializer=resource__pb2.GetFileReq.SerializeToString,
        response_deserializer=resource__pb2.FileResp.FromString,
        )
    self.UploadAvatar = channel.unary_unary(
        '/whale.resource.proto.ResourceService/UploadAvatar',
        request_serializer=resource__pb2.UploadAvatarReq.SerializeToString,
        response_deserializer=resource__pb2.UploadFileResp.FromString,
        )
    self.UploadFirmware = channel.unary_unary(
        '/whale.resource.proto.ResourceService/UploadFirmware',
        request_serializer=resource__pb2.UploadFileReq.SerializeToString,
        response_deserializer=resource__pb2.UploadFileResp.FromString,
        )


class ResourceServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def UploadImage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadModel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadFaceImage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFileInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadAvatar(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadFirmware(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ResourceServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UploadImage': grpc.unary_unary_rpc_method_handler(
          servicer.UploadImage,
          request_deserializer=resource__pb2.UploadFileReq.FromString,
          response_serializer=resource__pb2.UploadFileResp.SerializeToString,
      ),
      'UploadModel': grpc.unary_unary_rpc_method_handler(
          servicer.UploadModel,
          request_deserializer=resource__pb2.UploadModelReq.FromString,
          response_serializer=resource__pb2.UploadFileResp.SerializeToString,
      ),
      'UploadFaceImage': grpc.unary_unary_rpc_method_handler(
          servicer.UploadFaceImage,
          request_deserializer=resource__pb2.UploadFaceImageReq.FromString,
          response_serializer=resource__pb2.UploadFileResp.SerializeToString,
      ),
      'GetFileInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetFileInfo,
          request_deserializer=resource__pb2.GetFileReq.FromString,
          response_serializer=resource__pb2.FileResp.SerializeToString,
      ),
      'UploadAvatar': grpc.unary_unary_rpc_method_handler(
          servicer.UploadAvatar,
          request_deserializer=resource__pb2.UploadAvatarReq.FromString,
          response_serializer=resource__pb2.UploadFileResp.SerializeToString,
      ),
      'UploadFirmware': grpc.unary_unary_rpc_method_handler(
          servicer.UploadFirmware,
          request_deserializer=resource__pb2.UploadFileReq.FromString,
          response_serializer=resource__pb2.UploadFileResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'whale.resource.proto.ResourceService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
