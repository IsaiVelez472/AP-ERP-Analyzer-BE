import pandas as pd
from typing import Literal

# Carga el CSV una sola vez al inicio
df = pd.read_csv("app/data/extracted_data.csv")

# Convertimos año y mes a una sola columna de fecha
df["fecha"] = pd.to_datetime(df["year"].astype(str) + "-" + df["month"].astype(str) + "-01")

# ========= 1. Ventas Mensuales =========
def ventas_mensuales():
    """
    Devuelve ventas mensuales agregadas por año y mes.
    Suponemos que ventas se reflejan en cuentas con saldo positivo y código >= 4 (Ingresos).
    """
    ventas = df[df["code"] >= 4]
    resumen = (
        ventas.groupby(["year", "month"])["final_balance"]
        .sum()
        .reset_index()
        .sort_values(["year", "month"])
    )
    resumen.columns = ["año", "mes", "ventas"]
    return resumen.to_dict(orient="records")


# ========= 2. Flujo de Caja =========
def flujo_caja(tipo: Literal["operativo", "inversion", "financiacion", "todos"] = "todos"):
    """
    Calcula el flujo de caja por tipo o total acumulado.
    Clasificación basada en prefijos de código contable (1 = activo, 2 = pasivo, etc.)
    """

    # Mapeo simplificado por ejemplo:
    clasificacion = {
        "operativo": lambda x: x >= 1 and x < 2,
        "inversion": lambda x: x >= 2 and x < 3,
        "financiacion": lambda x: x >= 3 and x < 4,
    }

    data = df.copy()
    if tipo != "todos":
        data = data[data["code"].apply(clasificacion[tipo])]

    flujo = (
        data.groupby("fecha")["final_balance"]
        .sum()
        .sort_index()
        .cumsum()
        .reset_index()
    )
    flujo.columns = ["fecha", "flujo_acumulado"]
    return flujo.to_dict(orient="records")


# ========= 3. Egresos por Proveedor =========
def egresos_por_proveedor():
    """
    Agrupa los egresos (movimientos negativos) por proveedor y muestra su total y porcentaje.
    """
    egresos = df[df["final_balance"] < 0]

    resumen = (
        egresos.groupby("third_party_id")["final_balance"]
        .sum()
        .reset_index()
    )
    resumen["porcentaje"] = (resumen["final_balance"] / resumen["final_balance"].sum()) * 100
    resumen = resumen.sort_values("final_balance")
    resumen.columns = ["proveedor_id", "total_egresos", "porcentaje"]

    return resumen.to_dict(orient="records")
