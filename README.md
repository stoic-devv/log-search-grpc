# Client server model using gRPC

This is a client-server model that fetches data from via REST call from a lambda function. The communication between the client and the server happen in via a RPC call. gRPC is used to facilitate this RPC call. 

Check out this repository for lambda function: [log-search-func](https://github.com/stoic-devv/log-search-func)

##  Build and run configurations

### Build requirements
1. Python >= `3.8`
2. `pip` >= ` 9.0.1`
3. `grpcio` and `grpcio-tools`<br/>
More on installation of gRPC libraries can be found [here](https://grpc.io/docs/languages/python/quickstart/)

### Running
1. To generate gRPC client and server stubs:

`python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/log_search.proto`

Note that these stubs are already included in this repository.

2. To run server execute:

`python log_search_server.py`

3. To execute client:

`python log_search_client.py  arg1 arg2`

where `arg1` and `arg2` are of the form `HH:MM:SS.sss`<br/>
for eg: `python log_search_client.py  19:39:37.360 00:00:05.000`

## Project structure
1. `protos/log_Search.proto`: contains IDL for our client server model
2. `log_search_client.py`: contains client code
3. `log_Search_server.py`: contains server code
4. `app_constants.py`: application constants
5. `log_search_pb2_grpc.py`/`log_search_pb2.py`: contains client and server stubs generated by gRPC from the `.proto` file


## Code flow
1. Client invokes server function by passing a gRPC message
2. Server is makes a REST call to the AWS API Gateway which serves the lambda function that is already deployed.
3. Server sends the gRPC response to the client.