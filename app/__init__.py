# Copyright 2025 Anti-Patrones
# This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
# http://creativecommons.org/licenses/by-sa/4.0/

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar rutas
from app.routes.health import router as health_router
from app.routes.accounting import router as accounting_router

def create_app(config_name='development'):
    """Crea y configura la aplicación FastAPI"""
    
    app = FastAPI(
        title="AP-ERP-Analyzer-BE",
        description="API para análisis de datos ERP",
        version="0.1.0"
    )
    
    # Configurar CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # En producción, especificar orígenes permitidos
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Registrar rutas
    app.include_router(health_router)
    app.include_router(accounting_router)
    
    return app