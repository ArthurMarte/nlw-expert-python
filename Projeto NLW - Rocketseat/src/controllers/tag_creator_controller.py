from typing import Dict
from src.drivers.barcode_handlers import BarcodeHandler

class TagCreatorController:
    #implementar as regras de negócio

    #usuário só tera acesso ao método create, os outros são métodos privados
    def create(self, product_code:str) -> Dict:
        path_from_tag = self.__create_tag(product_code)
        formatted_response = self.__format_response(path_from_tag)
        return formatted_response


    #cria a tag
    def __create_tag(self, product_code:str) -> str:
        barcode_handler = BarcodeHandler()
        path_from_tag = barcode_handler.create_barcode(product_code)
        return path_from_tag
    

    #formata a resposta que eu quero que seja devolvida
    def __format_response(self, path_from_tag: str) -> Dict:
        return{
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f'{path_from_tag}.png'
            }
        }