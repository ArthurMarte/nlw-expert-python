from flask import Flask, request, jsonify
from barcode import Code128
from barcode.writer import ImageWriter

app = Flask(__name__) #criando um servidor em flask

@app.route('/create_tag', methods=['POST']) #rotas para a pagina principal e o login
def create_tag():
    body = request.json  #requisiçãoo json
    product_code = body.get('product_code') #corpo  da requisição com o código do produto

    tag = Code128(product_code, writer = ImageWriter()) #faz a imagem com o código do produto
    path_from_tag = f'{tag}'
    tag.save(path_from_tag)

    return jsonify({'tag path': path_from_tag})




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000) #criando servidor em flask na porta 3000
