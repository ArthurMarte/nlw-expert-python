from src.views.http_request import HttpRequest
from src.views.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController


class TagCreatorView:
    #responsabilidade para interagir com o http

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCreatorController()

        body = http_request.body
        product_code = body['product_code']

        #logica de regra de negócio (criação das tags)
        formatted_response = tag_creator_controller.create(product_code) #recebe a resposta formatada

        #retorno http
        return HttpResponse(status_code=200, body=formatted_response) # entrega a resposta formatada para o usuário