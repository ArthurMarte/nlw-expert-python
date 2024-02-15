from .tag_creator_validator import tag_creator_validator
from src.erros.error_types.unprocessable_entity import HttpUnprocessableEntityError


class MockRequest:
    def __init__(self, json) -> None:
        self.json = json


def test_tag_creator_validator():
    req = MockRequest(json={'product_code': '12354'})
    response = tag_creator_validator(req)

def test_tag_creator_validator_with_error():
    req = MockRequest(json={'product_code': 12354})

    #se lançar um erro, ele tem que cair no Excption e sua exessão tem que ser do tipo
    #HttpUnprocessableEntityError
    try:
        response = tag_creator_validator(req)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
