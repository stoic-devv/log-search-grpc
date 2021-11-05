from concurrent import futures
from app_constants import Constants

import logging
import requests
import grpc

import log_search_pb2_grpc
import log_search_pb2

class LogSearchServicer(log_search_pb2_grpc.LogSearchServicer):

    """
        Returns the log messages from Lambda via a GET request
    """
    def GetLogs(self, request, context):
        logging.info("Received client message")
        params = {Constants.TIME_PARAM.value: request.time_stamp, Constants.INTERVAL_PARAM.value: request.time_interval}
        response = requests.get(url=Constants.URL.value, params=params)
        return log_search_pb2.Response(status_code=response.status_code, content=response.content)
        
"""
Runs the server listening to the client grpc calls
"""
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    log_search_pb2_grpc.add_LogSearchServicer_to_server(
        LogSearchServicer(), server)
    server.add_insecure_port('[::]:'+ Constants.PORT_NUM.value)
    logging.info('Starting server')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()