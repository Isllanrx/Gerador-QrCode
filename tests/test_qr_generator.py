import unittest
import os
from pathlib import Path
from src.core.qr_generator import QRGenerator

class TestQRGenerator(unittest.TestCase):
    def setUp(self):
        self.output_dir = "test_qrcodes"
        self.generator = QRGenerator(output_dir=self.output_dir)

    def tearDown(self):
        # Limpa os arquivos de teste
        if os.path.exists(self.output_dir):
            for file in os.listdir(self.output_dir):
                os.remove(os.path.join(self.output_dir, file))
            os.rmdir(self.output_dir)

    def test_generate_qr(self):
        data = "https://google.com"
        file_name = "test_qr.png"
        path = self.generator.generate(data, file_name)
        
        self.assertTrue(os.path.exists(path))
        self.assertEqual(Path(path).name, file_name)

if __name__ == "__main__":
    unittest.main()
