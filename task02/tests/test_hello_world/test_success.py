from tests.test_hello_world import HelloWorldLambdaTestCase


class TestSuccess(HelloWorldLambdaTestCase):

    def test_success(self):
        event = {}
        http = {"path": "/hello", "method": "GET"}
        event["requestContext"] = {"http": http}
        self.assertEqual(self.HANDLER.handle_request(event, dict())["statusCode"], 200)
        self.assertEqual(self.HANDLER.handle_request(event, dict())["body"]["statusCode"], 200)
        self.assertEqual(self.HANDLER.handle_request(event, dict())["body"]["message"], "Hello from Lambda")

    def test_bad_request(self):
        event = {}
        http = {"path": "/st", "method": "POST"}
        event["requestContext"] = {"http": http}
        self.assertEqual(self.HANDLER.handle_request(event, dict())["statusCode"], 400)
        self.assertEqual(self.HANDLER.handle_request(event, dict())["body"]["statusCode"], 400)
        self.assertEqual(self.HANDLER.handle_request(event, dict())["body"]["message"], "Bad request syntax or unsupported method. Request path: /st. HTTP method: POST")
