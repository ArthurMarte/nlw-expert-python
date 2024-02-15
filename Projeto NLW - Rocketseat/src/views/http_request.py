from typing import Dict #cada elemento que estamos usando estão em formato de dicionários


#caso os elementos não tenham nada, seram preenchidos com o None
class HttpRequest:
    def  __init__(
            self, 
            header: Dict = None, 
            body: Dict = None,  
            query_params: Dict = None 
    ) -> None:
        self.header = header
        self.body = body
        self.query_params = query_params
