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

## 🚀 Características implementadas

### KPIs Financieros
- **Flujo de Caja**: Análisis de flujo de caja operativo, de inversión, financiación y acumulado
- **Análisis de Ventas**: Ventas totales, crecimiento, ventas por cliente
- **Cuentas por Cobrar y Pagar**: Saldos promedio, antigüedad, rotación
- **Egresos por Proveedor**: Total de egresos, porcentaje del total, tendencias

### Modelos de Machine Learning
- **Pronóstico de Ventas**: Modelo ARIMA/SARIMA para predecir ventas futuras
- **Detección de Anomalías**: Identificación de transacciones inusuales en el flujo de caja

## 🗂️ Estructura del proyecto

```
AP-ERP-Analyzer-BE/
├── app/
│   ├── __init__.py          # Configuración de la aplicación
│   ├── main.py              # Punto de entrada de la API
│   ├── data/                # Datos de entrada (CSV, SQL)
│   ├── models/              # Modelos de datos Pydantic
│   ├── routers/             # Endpoints de la API
│   ├── services/            # Lógica de negocio
│   └── utils/               # Funciones de utilidad
├── requirements.txt         # Dependencias del proyecto
└── run.py                   # Script para ejecutar la aplicación
```

## 🔧 Requisitos del sistema

- Python 3.9 o superior
- FastAPI
- Pandas
- NumPy
- Scikit-learn
- Statsmodels

## 🚀 Instalación y ejecución

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:

```bash
python run.py
```

La API estará disponible en: `http://localhost:5002`
Documentación interactiva: `http://localhost:5002/docs`

## 🔌 API Endpoints

### KPIs Financieros
- `GET /api/kpis/financial/cash-flow`: Análisis de flujo de caja
- `GET /api/kpis/financial/summary`: Resumen financiero general

### Análisis de Ventas
- `GET /api/kpis/sales/`: Análisis completo de ventas
- `GET /api/kpis/sales/by-period`: Ventas agrupadas por período
- `GET /api/kpis/sales/by-customer`: Ventas agrupadas por cliente

### Cuentas por Cobrar y Pagar
- `GET /api/kpis/accounts/`: Análisis de cuentas por cobrar y pagar
- `GET /api/kpis/accounts/receivable`: Análisis de cuentas por cobrar
- `GET /api/kpis/accounts/payable`: Análisis de cuentas por pagar

### Análisis de Gastos
- `GET /api/kpis/expenses/`: Análisis de gastos por proveedor
- `GET /api/kpis/expenses/by-period`: Gastos agrupados por período
- `GET /api/kpis/expenses/by-supplier`: Gastos agrupados por proveedor

### Modelos de ML
- `POST /api/ml/train/sales-forecast`: Entrenar modelo de pronóstico de ventas
- `GET /api/ml/sales-forecast`: Obtener pronóstico de ventas
- `POST /api/ml/train/anomaly-detection`: Entrenar modelo de detección de anomalías
- `GET /api/ml/anomaly-detection`: Obtener detección de anomalías en flujo de caja

## 📝 License

This project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](http://creativecommons.org/licenses/by-sa/4.0/).
