# AP-ERP-Analyzer-BE

**Backend para la visualización de indicadores clave (KPIs) en sistemas ERP**

> Proyecto desarrollado durante la Hackathon 2025 — Reto: Visualización de indicadores clave para la gestión empresarial en plataformas ERP.

## 🧠 Propósito del proyecto

Este backend está diseñado para apoyar a pequeñas y medianas empresas que utilizan sistemas ERP, permitiéndoles transformar grandes volúmenes de datos operativos, administrativos y contables en información comprensible para la toma de decisiones. Se enfoca en procesar datasets estructurados y exponer endpoints REST para alimentar dashboards interactivos.

## 📊 Objetivo del reto

- Desarrollar un módulo funcional que permita la visualización dinámica de KPIs empresariales.
- Proveer datos listos para ser visualizados en dashboards construidos con herramientas como Streamlit, Dash o Plotly.
- Facilitar el análisis financiero, operativo y administrativo para usuarios no técnicos.
- Utilizar datos simulados con estructura realista de ERP (facturas, inventario, nómina, egresos, etc.).

## 🗂️ Estructura del proyecto

```
AP-ERP-Analyzer-BE/
├── app/
│   └── __init__.py
├── datasets/
│   └── Dataset.sql
├── requirements.txt
└── run.py
```


## 🔧 Requisitos del sistema

- Python 3.12 o superior
- FastAPI
- Pandas
- NumPy

Instalación de dependencias:

```bash
pip install -r requirements.txt

```
python run.py
```

Endpoints:
- `GET /health-check`: Estado del servidor
- `GET /api/data/summary`: Resumen de datos del dataset

## License

This project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](http://creativecommons.org/licenses/by-sa/4.0/).
