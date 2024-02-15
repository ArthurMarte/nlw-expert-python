from barcode import Code128
from barcode.writer import ImageWriter

#dá acesso apenas ao processo de utilizar o barcode, não a biblioteca como um todo
class BarcodeHandler:
    def create_barcode(self, product_code: str) -> str:
        tag = Code128(product_code, writer = ImageWriter()) #faz a imagem com o código do produto
        path_from_tag = f'{tag}'
        tag.save(path_from_tag)

        return path_from_tag