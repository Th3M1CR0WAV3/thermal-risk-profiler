from __future__ import annotations

from dataclasses import asdict
from math import isnan
from typing import Any

from pythermalcomfort.models import phs, utci
from pythermalcomfort.utilities import scale_wind_speed_log

from .schemas import EnvironmentPoint, PersonProfile, RiskResult


def _resolve_tr(environment: EnvironmentPoint) -> float:
    if environment.tr_method == "shade":
        return environment.tdb
    if environment.tr_method == "sun":
        if environment.tr is None:
            raise ValueError("tr must be provided when tr_method is 'sun'.")
        return environment.tr
    raise ValueError(f"Unsupported tr_method '{environment.tr_method}'.")


def _extract_utci(result: Any) -> tuple[float | None, str | None]:
    if isinstance(result, dict):
        return result.get("utci"), result.get("stress_category")
    if isinstance(result, (float, int)):
        return float(result), None
    return None, None


def _extract_phs_fields(result: Any) -> dict[str, float | None]:
    if not isinstance(result, dict):
        return {
            "phs_sweat_loss": None,
            "phs_dlim_tre": None,
            "phs_dlim_tre_sweat": None,
        }
    return {
        "phs_sweat_loss": result.get("sweat_loss"),
        "phs_dlim_tre": result.get("dlim_tre"),
        "phs_dlim_tre_sweat": result.get("dlim_tre_sweat"),
    }


def compute_risk(environment: EnvironmentPoint, person: PersonProfile) -> RiskResult:
    tr = _resolve_tr(environment)
    utci_result = utci(tdb=environment.tdb, tr=tr, v=environment.v10m, rh=environment.rh)
    utci_value, utci_category = _extract_utci(utci_result)

    v_1_1m = scale_wind_speed_log(v=environment.v10m, z1=10, z2=1.1)
    phs_result = phs(
        tdb=environment.tdb,
        tr=tr,
        v=v_1_1m,
        rh=environment.rh,
        met=person.met,
        clo=person.clo,
        posture=person.posture,
    )

    phs_fields = _extract_phs_fields(phs_result)

    is_utci_valid = utci_value is not None and not isnan(float(utci_value))
    is_phs_valid = any(
        value is not None and not isnan(float(value)) for value in phs_fields.values()
    )

    return RiskResult(
        utci=utci_value,
        utci_stress_category=utci_category,
        is_utci_valid=is_utci_valid,
        is_phs_valid=is_phs_valid,
        **phs_fields,
    )


def risk_result_to_dict(result: RiskResult) -> dict[str, Any]:
    return asdict(result)
