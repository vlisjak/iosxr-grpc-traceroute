import grpc
import iosxr_pb2 as pb2
import iosxr_pb2_grpc as pb2_grpc
import json

# Install:
# python -m pip install grpcio
# python -m pip install protobuf

# Download .proto file:
# https://github.com/nleiva/xrgrpc/blob/v0.6.0/proto/ems/ems_grpc.proto

# Run:
# python -m grpc_tools.protoc --proto_path=. ./iosxr.proto --python_out=. --grpc_python_out=.

if __name__ == "__main__":

    target = "10.52.157.183:57344"
    username = "cisco"
    password = "cisco123"

    lsp_name = "srte_c_10_ep_1.1.1.8"
    lsp_endpoint = "10.0.0.8"
    lsp_source = "1.1.1.10"

    # grpc_payload = '{"Cisco-IOS-XR-mpls-traceroute-act:mpls-traceroute": {"sr-mpls": {"policy": {"name": "srte_c_10_ep_1.1.1.8", "lsp-endpoint": "10.0.0.8"}}, "request-options-parameters":{"source": "1.1.1.10"}}}'

    grpc_payload = {
        "Cisco-IOS-XR-mpls-traceroute-act:mpls-traceroute": {
            "sr-mpls": {
                "policy": {
                    "name": lsp_name,
                    "lsp-endpoint": lsp_endpoint
                }
            },
            "request-options-parameters": {
                "source": lsp_source
            }
        }
    }

    metadata = (
        ("username", username),
        ("password", password),
    )

    with grpc.insecure_channel(target, options=(("grpc.enable_http_proxy", 0),)) as channel:
        stub = pb2_grpc.gRPCExecStub(channel)

        message = pb2.ActionJSONArgs(ReqId=0, yangpathjson=json.dumps(grpc_payload))

        result = []
        for m in stub.ActionJSON(message, metadata=metadata):
            result.append(m)

        try:
            result_json = json.loads(result[0].yangjson)
            for path in result_json["Cisco-IOS-XR-mpls-traceroute-act:output"]["mpls-traceroute-response"]["paths"]["path"][0]["hops"]["hop"]:
                print(path)
        except:
            result_json = json.loads(result[0].errors)
            print(result_json)
