from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        http = event["requestContext"]["http"]
        path = http["path"]
        method = http["method"]
        response = {}
        if method == "GET" and path == "/hello":
            response["statusCode"] = 200
            response["message"] = "Hello from Lambda"
        else:
            response["statusCode"] = 400
            response["message"] = f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
        return response
    

HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.handle_request(event=event, context=context)
