import os

from aws_cdk import Stack
from aws_cdk.aws_apigateway import LambdaRestApi
from aws_cdk.aws_lambda import Function, Runtime, Code
from constructs import Construct


class DailyDragonStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        lambda_function = Function(
            self, 'DailyDragonMainHandler',
            runtime=Runtime.PYTHON37,
            handler='handler.lambda_handler',
            code=Code.from_asset(os.path.join(os.getcwd(), 'daily_dragon_handler.py'))
        )

        api = LambdaRestApi(
            self, 'DailyDragopAPIGateway',
            handler=lambda_function,
            proxy=True
        )
