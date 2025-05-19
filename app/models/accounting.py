# Copyright 2025 Anti-Patrones
# This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
# http://creativecommons.org/licenses/by-sa/4.0/

from typing import Optional, Dict, Any
from pydantic import BaseModel

class PaginationResponse(BaseModel):
    page: int
    per_page: int
    total_records: int
    total_pages: int

class AccountBalance(BaseModel):
    id: int
    code: float
    accounting_id: int
    name: str
    initial_balance: float
    final_balance: float
    debit_movement: float
    credit_movement: float
    third_party_type_id: str
    third_party_id: int
    currency_id: str
    year: int
    month: int
    deleted_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class BalancesResponse(BaseModel):
    status: str
    data: Dict[str, Any]

class ErrorResponse(BaseModel):
    status: str
    message: str
