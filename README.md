# AP-ERP-Analyzer-BE

Backend para análisis de datos ERP.

# Copyright 2025 Anti-Patrones
# This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
# http://creativecommons.org/licenses/by-sa/4.0/

## Estructura

```
AP-ERP-Analyzer-BE/
├── app/
│   └── __init__.py
├── datasets/
│   └── Dataset.sql
├── requirements.txt
└── run.py
```

## Requisitos

- Python 3.12+
- Flask, Pandas, NumPy

## Uso

Iniciar servidor:
```
python run.py
```

Endpoints:
- `GET /health-check`: Estado del servidor
- `GET /api/data/summary`: Resumen de datos del dataset

## License

This project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](http://creativecommons.org/licenses/by-sa/4.0/).
