import functools

from takagi.models import LambdaApiGatewayEvent, LambdaApiGatewayResponse


def api_response(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            status_code, raw_response = func(*args, **kwargs)
            headers = {"Content-Type": "application/json"}
            response = LambdaApiGatewayResponse(status_code=status_code, body=raw_response, headers=headers).dict()
            return response
        except Exception as e:
            print(e)

    return wrapper


def api_gateway_event(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        event, context = args
        try:
            return func(LambdaApiGatewayEvent.parse_obj(event), context)
        except Exception as e:
            print(e)

    return wrapper
