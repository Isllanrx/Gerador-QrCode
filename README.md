# QR Code Generator - Technical Documentation

Standardized system for QR Code generation utilizing a modular architecture.

## System Architecture

```mermaid
graph TD
    A[main.py] --> B[src.ui.app.QRCodeApp]
    B --> C[src.core.qr_generator.QRGenerator]
    B --> D[src.utils.validators]
    B --> E[src.data.countries]
    C --> F[FileSystem /Qr_code]
```

## Module Description

- **src/core**: Logic for QR code encoding and file persisting.
- **src/ui**: GUI implementation using CustomTkinter.
- **src/data**: Static datasets and configuration.
- **src/utils**: Pure functions for validation and sanitization.

## Dependency Management

The project uses PEP 517 standards. Dependencies are listed in `requirements.txt` and `pyproject.toml`.

- qrcode
- pillow
- customtkinter

## Installation

```bash
pip install -r requirements.txt
```

## Execution

```bash
python main.py
```

## Quality Assurance

Unit tests focus on the generation core:

```bash
$env:PYTHONPATH="."; python tests/test_qr_generator.py
```

## Technical Specification

- **Error Correction**: QR Code Error Correction Level L.
- **Output Format**: PNG.
- **DPI/Size**: Box size 10, Border 4.
- **Security**: Filename sanitization via whitelist (alphanumeric).
```
