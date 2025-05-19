# Copyright 2025 Anti-Patrones
# This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
# http://creativecommons.org/licenses/by-sa/4.0/

from fastapi import APIRouter, Query, HTTPException
from typing import Dict, Optional, Any

from app.models.accounting import BalancesResponse, ErrorResponse
from app.services.accounting_service import get_account_balances

router = APIRouter(prefix="/api/accounting", tags=["accounting"])

@router.get("/balances", response_model=BalancesResponse, responses={500: {"model": ErrorResponse}})
def get_accounting_balances(
    page: int = Query(1, ge=1, description="Página actual"),
    per_page: int = Query(10, ge=1, le=100, description="Elementos por página"),
    sort_by: str = Query("id", description="Campo por el cual ordenar"),
    sort_order: str = Query("asc", description="Orden ascendente o descendente"),
    search: Optional[str] = Query(None, description="Término de búsqueda")
):
    try:
        result = get_account_balances(page, per_page, sort_by, sort_order, search)
        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "message": str(e)
        })
