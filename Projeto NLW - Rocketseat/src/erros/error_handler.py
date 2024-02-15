from src.views.http_response import HttpResponse
from .error_types.unprocessable_entity import HttpUnprocessableEntityError


#exception trata os erros como objetos vindos da classe exception
def handle_errors(error:  Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "erros":[{
                "title": error.name,
                "detail": error.message
            }]
            }
        )


    return HttpResponse(
        status_code=500, #erros genéricos
        body={
            "erros":[{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )