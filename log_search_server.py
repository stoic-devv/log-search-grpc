from concurrent import futures
import logging
import requests
import grpc

import log_search_pb2_grpc
import log_search_pb2

class LogSearchServicer(log_search_pb2_grpc.LogSearchServicer):

    def GetLogs(self, request, context):
        url = "https://uvz1k07zeg.execute-api.us-east-2.amazonaws.com/prod/logs"
        params = {'t': request.time_stamp, 'dt': request.time_interval}

        response = requests.get(url=url, params=params)
        return log_search_pb2.Response(status_code=response.status_code, content=response.content)
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    log_search_pb2_grpc.add_LogSearchServicer_to_server(
        LogSearchServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()