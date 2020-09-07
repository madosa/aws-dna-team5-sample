import json
from functools import partial
from typing import Any, Dict, Optional

import inflection
from pydantic import BaseModel, validator

camelize = partial(inflection.camelize, uppercase_first_letter=False)


class LambdaApiGatewayResponse(BaseModel):
    class LambdaResponseBody(BaseModel):
        data: Any

    status_code: int
    body: str
    headers: Dict[str, Any]
    is_base64_encoded: bool = False

    @validator("body", pre=True)
    def check_body(cls, value):  # noqa
        return cls.LambdaResponseBody(data=value).json()

    def dict(
        self,
        *,
        include=None,
        exclude=None,
        by_alias=False,
        skip_defaults=None,
        exclude_unset=False,
        exclude_defaults=False,
        exclude_none=False,
    ) -> Dict[str, Any]:
        output = super(LambdaApiGatewayResponse, self).dict()
        return {camelize(key): value for key, value in output.items()}


class LambdaApiGatewayEvent(BaseModel):
    class Config:
        alias_generator = camelize

    body: Optional[Dict[str, Any]]
    resource: Optional[str]
    path: Optional[str]
    http_method: Optional[str]
    is_base64_encoded: Optional[bool]
    query_string_parameters: Optional[Dict[str, Any]]
    multi_value_query_string_parameters: Optional[Dict[str, Any]]
    path_parameters: Optional[Dict[str, Any]]
    stage_variables: Optional[Dict[str, Any]]
    headers: Optional[Dict[str, Any]]
    multi_value_headers: Optional[Dict[str, Any]]
    request_context: Optional[Dict[str, Any]]

    @validator("body", pre=True)
    def check_body(cls, v):  # noqa
        if v:
            return json.loads(v)
        return v
