import logging
from app_constants import Constants
import log_search_pb2_grpc
import log_search_pb2
import grpc
import sys

"""
Returns the params in proto format
"""
def get_params(args):
    if len(args) != 2:
        logging.error("Invalid arguments")
    return log_search_pb2.QueryParams(time_stamp=args[0], time_interval=args[1])

"""
Client code
"""
def run(args):
    with grpc.insecure_channel(Constants.HOST_NAME.value+Constants.PORT_NUM.value) as channel:
        logging.info('Sending message to server')
        stub = log_search_pb2_grpc.LogSearchStub(channel)
        response = stub.GetLogs(get_params(args))
        # if required for additional info
        #print(response.status_code, response.content)
        if response.status_code != 200:
            print(False)
        else:
            print(True)


if __name__ == '__main__':
    logging.basicConfig()
    args = sys.argv[1:]
    run(args)