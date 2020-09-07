import logging
from http import HTTPStatus
from typing import Any, Dict, Tuple

from takagi.decorators import api_gateway_event, api_response
from takagi.models import LambdaApiGatewayEvent

logger = logging.getLogger(__name__)


@api_response
@api_gateway_event
def handler(event: LambdaApiGatewayEvent, context) -> Tuple[int, Dict[str, Any]]:
    return HTTPStatus.OK, event.dict()
