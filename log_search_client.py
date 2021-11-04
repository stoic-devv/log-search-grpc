import logging
import log_search_pb2_grpc
import log_search_pb2
import grpc
import sys

def get_params(args):
    if len(args) != 2:
        logging.error("Invalid arguments")
    return log_search_pb2.QueryParams(time_stamp=args[0], time_interval=args[1])

def run(args):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = log_search_pb2_grpc.LogSearchStub(channel)
        response = stub.GetLogs(get_params(args))
        print(response.status_code, response.content)


if __name__ == '__main__':
    logging.basicConfig()
    args = sys.argv[1:]
    run(args)