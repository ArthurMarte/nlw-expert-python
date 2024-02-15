from .tag_creator_controller import TagCreatorController
from src.drivers.barcode_handlers import BarcodeHandler
from unittest.mock import patch

#mock é um  módulo do python que permite criar objetos simulados para substituir outros

@patch.object(BarcodeHandler, 'create_barcode') #simula  que o método create_barcode da classe BarcodeHandler está sendo mockado
def test_create(mock_create_barcode):
    mock_value = 'image_path'
    mock_create_barcode.return_value = mock_value #retorna um valor fictício de mock_value
    tag_creator_controller = TagCreatorController()

    result = tag_creator_controller.create(mock_value)

    assert isinstance(result, dict), "Result should be a dictionary"
    assert "data" in result
    assert "type" in result["data"]
    assert "count" in result["data"]
    assert "path" in result["data"]

    assert result['data']['type'] == 'Tag Image'
    assert result['data']['count'] == 1
    assert result['data']['path'] == f'{mock_value}.png'