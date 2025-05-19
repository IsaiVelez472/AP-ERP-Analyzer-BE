# Copyright 2025 Anti-Patrones
# This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
# http://creativecommons.org/licenses/by-sa/4.0/

import sqlite3
import pandas as pd
from typing import Dict, List, Optional, Tuple, Any

def create_sample_database() -> sqlite3.Connection:
    """
    Crea una base de datos en memoria con datos de ejemplo para contabilidad
    """
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Crear la tabla accounting_account_balances
    cursor.execute('''
    CREATE TABLE accounting_account_balances (
        id INTEGER PRIMARY KEY,
        code REAL NOT NULL,
        accounting_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        initial_balance REAL NOT NULL DEFAULT 0,
        final_balance REAL NOT NULL DEFAULT 0,
        debit_movement REAL NOT NULL DEFAULT 0,
        credit_movement REAL NOT NULL DEFAULT 0,
        third_party_type_id TEXT NOT NULL,
        third_party_id INTEGER NOT NULL,
        currency_id TEXT NOT NULL DEFAULT 'COP',
        year INTEGER NOT NULL,
        month INTEGER NOT NULL,
        deleted_at TEXT DEFAULT NULL,
        created_at TEXT DEFAULT NULL,
        updated_at TEXT DEFAULT NULL
    )
    ''')
    
    # Insertar datos de ejemplo
    sample_data = [
        (1, 1.0, 1, 'Caja', 1000.0, 1500.0, 2000.0, 1500.0, 'COMPANY', 1, 'COP', 2025, 5, None, '2025-05-01 10:00:00', '2025-05-19 12:00:00'),
        (2, 1.1, 1, 'Caja General', 500.0, 800.0, 1000.0, 700.0, 'COMPANY', 1, 'COP', 2025, 5, None, '2025-05-01 10:00:00', '2025-05-19 12:00:00'),
        (3, 1.2, 1, 'Caja Menor', 500.0, 700.0, 1000.0, 800.0, 'COMPANY', 1, 'COP', 2025, 5, None, '2025-05-01 10:00:00', '2025-05-19 12:00:00'),
        (4, 2.0, 1, 'Bancos', 5000.0, 7000.0, 5000.0, 3000.0, 'COMPANY', 1, 'COP', 2025, 5, None, '2025-05-01 10:00:00', '2025-05-19 12:00:00'),
        (5, 2.1, 1, 'Banco Nacional', 3000.0, 4000.0, 3000.0, 2000.0, 'COMPANY', 1, 'COP', 2025, 5, None, '2025-05-01 10:00:00', '2025-05-19 12:00:00'),
        (6, 2.2, 1, 'Banco Internacional', 2000.0, 3000.0, 2000.0, 1000.0, 'COMPANY', 1, 'COP', 2025, 5, None, '2025-05-01 10:00:00', '2025-05-19 12:00:00'),
        (7, 3.0, 1, 'Cuentas por Cobrar', 8000.0, 6000.0, 1000.0, 3000.0, 'COMPANY', 1, 'COP', 2025, 5, None, '2025-05-01 10:00:00', '2025-05-19 12:00:00'),
        (8, 4.0, 1, 'Inventario', 12000.0, 10000.0, 2000.0, 4000.0, 'COMPANY', 1, 'COP', 2025, 5, None, '2025-05-01 10:00:00', '2025-05-19 12:00:00'),
        (9, 5.0, 1, 'Activos Fijos', 20000.0, 19500.0, 0.0, 500.0, 'COMPANY', 1, 'COP', 2025, 5, None, '2025-05-01 10:00:00', '2025-05-19 12:00:00'),
        (10, 6.0, 1, 'Cuentas por Pagar', 5000.0, 6000.0, 2000.0, 3000.0, 'COMPANY', 1, 'COP', 2025, 5, None, '2025-05-01 10:00:00', '2025-05-19 12:00:00')
    ]
    
    cursor.executemany('''
        INSERT INTO accounting_account_balances 
        (id, code, accounting_id, name, initial_balance, final_balance, debit_movement, credit_movement, 
        third_party_type_id, third_party_id, currency_id, year, month, deleted_at, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', sample_data)
    
    conn.commit()
    return conn

def get_account_balances(
    page: int = 1, 
    per_page: int = 10, 
    sort_by: str = "id", 
    sort_order: str = "asc", 
    search: Optional[str] = None
) -> Dict[str, Any]:
    """
    Obtiene los saldos de cuentas contables con paginación y filtros
    """
    conn = create_sample_database()
    
    # Construir la consulta SQL con filtros
    query = "SELECT * FROM accounting_account_balances"
    params = []
    
    if search:
        query += " WHERE name LIKE ? OR code LIKE ?"
        search_param = f"%{search}%"
        params.extend([search_param, search_param])
    
    # Ordenar resultados
    query += f" ORDER BY {sort_by} {'ASC' if sort_order.lower() == 'asc' else 'DESC'}"
    
    # Calcular paginación
    offset = (page - 1) * per_page
    query += f" LIMIT {per_page} OFFSET {offset}"
    
    # Leer datos con pandas
    df = pd.read_sql_query(query, conn, params=params)
    
    # Obtener el total de registros para la paginación
    count_query = "SELECT COUNT(*) FROM accounting_account_balances"
    if search:
        count_query += " WHERE name LIKE ? OR code LIKE ?"
    
    cursor = conn.cursor()
    cursor.execute(count_query, params if search else [])
    total_records = cursor.fetchone()[0]
    
    # Convertir a formato JSON
    balances = df.to_dict(orient='records')
    
    conn.close()
    
    return {
        "balances": balances,
        "pagination": {
            "page": page,
            "per_page": per_page,
            "total_records": total_records,
            "total_pages": (total_records + per_page - 1) // per_page
        }
    }
