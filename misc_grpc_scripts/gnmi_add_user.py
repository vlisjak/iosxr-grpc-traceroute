from pygnmi.client import gNMIclient
import pprint as pp

ip = '10.255.0.2'
port = 57400

new_user = {
    "username": "newuser2",
    "config": {
        "username": "newuser2",
        "password": "Test1234",
        "role": "root-lr"
    }
}

oc_config = [(
    "openconfig-system:system", {
        "aaa": {
            "authentication": {
                "users": {
                    "user": new_user
                }
            }
        }
    }
)]

if __name__ == '__main__':
    with gNMIclient(target=(ip, port), username='cisco', password='cisco', grpc_options=[("grpc.enable_http_proxy", 0),], insecure=True, debug=True) as gc:
        # Step 1: Retrieve existing configuration
        gc.capabilities()
        response = gc.get(path=['openconfig-system:system'], encoding='json_ietf', datatype='all')
        existing_users = response['notification'][0]['update'][0]['val']['aaa']['authentication']['users']['user']
        print('EXISTING USERS:')
        pp.pprint(existing_users)

        print('UPDATE RESULT:')
        update_request = gc.set(update=oc_config, encoding='json_ietf')
        pp.pprint(update_request)