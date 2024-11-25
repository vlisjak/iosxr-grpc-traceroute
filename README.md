## Install python dependencies
```
python -m pip install grpcio
python -m pip install protobuf
```

## Download .proto file
https://github.com/nleiva/xrgrpc/blob/v0.6.0/proto/ems/ems_grpc.proto

## Create stubs
```
python -m grpc_tools.protoc --proto_path=. ./iosxr.proto --python_out=. --grpc_python_out=.
```

## Router config
```
RP/0/RP0/CPU0:Headend#show run formal grpc
grpc port 57344
grpc no-tls
grpc 
grpc address-family ipv4
grpc service-layer 
```

# Sample script results
```
(myvenv310) vlisjak@vlisjak:~/mygrpc$ python ./sr_traceroute.py 
{'hop-index': '0', 'hop-origin-ip': '10.10.10.100', 'hop-destination-ip': '10.10.10.110', 'mtu': '1500', 'dsmap-label-stack': {'dsmap-label': [{'label': 140138}]}, 'return-code': 0, 'return-char': ' ', 'duration': 0}
{'hop-index': '1', 'hop-origin-ip': '10.10.10.110', 'hop-destination-ip': '10.10.101.11', 'mtu': '1500', 'dsmap-label-stack': {'dsmap-label': [{'label': 140138}]}, 'return-code': 8, 'return-char': 'L', 'duration': 56}
{'hop-index': '2', 'hop-origin-ip': '10.10.101.11', 'hop-destination-ip': '10.10.112.2', 'mtu': '1500', 'dsmap-label-stack': {'dsmap-label': [{'label': 140138}]}, 'return-code': 8, 'return-char': 'L', 'duration': 56}
{'hop-index': '3', 'hop-origin-ip': '10.10.112.2', 'hop-destination-ip': '10.10.23.3', 'mtu': '1500', 'dsmap-label-stack': {'dsmap-label': [{'label': 140138}]}, 'return-code': 8, 'return-char': 'L', 'duration': 119}
{'hop-index': '4', 'hop-origin-ip': '10.10.23.3', 'hop-destination-ip': '10.10.34.4', 'mtu': '1500', 'dsmap-label-stack': {'dsmap-label': [{'label': 140138}]}, 'return-code': 8, 'return-char': 'L', 'duration': 162}
{'hop-index': '5', 'hop-origin-ip': '10.10.34.4', 'hop-destination-ip': '10.10.45.5', 'mtu': '1500', 'dsmap-label-stack': {'dsmap-label': [{'label': 140138}]}, 'return-code': 8, 'return-char': 'L', 'duration': 212}
{'hop-index': '6', 'hop-origin-ip': '10.10.45.5', 'hop-destination-ip': '10.10.56.6', 'mtu': '1500', 'dsmap-label-stack': {'dsmap-label': [{'label': 140138}]}, 'return-code': 8, 'return-char': 'L', 'duration': 165}
{'hop-index': '7', 'hop-origin-ip': '10.10.56.6', 'hop-destination-ip': '10.10.67.7', 'mtu': '1500', 'dsmap-label-stack': {'dsmap-label': [{'label': 140138}]}, 'return-code': 8, 'return-char': 'L', 'duration': 222}
{'hop-index': '8', 'hop-origin-ip': '10.10.67.7', 'hop-destination-ip': '10.10.78.8', 'mtu': '1500', 'dsmap-label-stack': {'dsmap-label': [{'label': 0}]}, 'return-code': 8, 'return-char': 'L', 'duration': 368}
{'hop-index': '9', 'hop-origin-ip': '10.10.78.8', 'hop-destination-ip': '', 'mtu': '0', 'dsmap-label-stack': '', 'return-code': 4, 'return-char': 'F', 'duration': 521}
```
