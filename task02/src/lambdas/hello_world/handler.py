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
        body = {}
        if method == "GET" and path == "/hello":
            body["statusCode"] = 200
            body["message"] = "Hello from Lambda"
            return {"statusCode": 200, "body": body}
        else:
            body["statusCode"] = 400
            body["message"] = f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
        return {"statusCode": 400, "body": body}


HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.handle_request(event=event, context=context)
