# Copyright 2025 Anti-Patrones
# This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
# http://creativecommons.org/licenses/by-sa/4.0/

from fastapi import APIRouter
from typing import Dict

router = APIRouter(tags=["health"])

@router.get("/health-check", response_model=Dict[str, str])
def health_check():
    return {
        "status": "ok", 
        "message": "AP-ERP-Analyzer-BE is running",
        "version": "0.1.0"
    }
