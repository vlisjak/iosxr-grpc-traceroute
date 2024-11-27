import grpc
import iosxr_pb2 as pb2
import iosxr_pb2_grpc as pb2_grpc
import json

if __name__ == "__main__":

    target = "192.168.101.43:57400"
    username = "cisco"
    password = "Cisco!123"
    session_name = 'FILESPAN'

    grpc_payload = {
        'Cisco-IOS-XR-Ethernet-SPAN-act:packet-collection-start': { 
            'session': session_name 
            } 
        }

    metadata = (
        ("username", username),
        ("password", password),
    )

    with grpc.insecure_channel(target, options=(("grpc.enable_http_proxy", 0),)) as channel:
        stub = pb2_grpc.gRPCExecStub(channel)

        message = pb2.ActionJSONArgs(ReqId=0, yangpathjson=json.dumps(grpc_payload))
        
        print('GRPC Payload to send to router:')
        print(grpc_payload)

        result = []
        for m in stub.ActionJSON(message, metadata=metadata):
            result.append(m)
            print(message,metadata)
