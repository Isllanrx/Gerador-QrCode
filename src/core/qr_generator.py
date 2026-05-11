from pathlib import Path
import qrcode

class QRGenerator:
    def __init__(self, output_dir: str = "Qr_code"):
        self.output_dir = Path(output_dir)
        self._ensure_output_dir()

    def _ensure_output_dir(self):
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate(self, data: str, file_name: str) -> str:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        safe_file_name = "".join(c for c in file_name if c.isalnum() or c in "._- ").strip()
        file_path = self.output_dir / safe_file_name
        img.save(str(file_path))
        return str(file_path)
