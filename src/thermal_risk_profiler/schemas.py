from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EnvironmentPoint:
    tdb: float
    rh: float
    v10m: float
    tr: float | None = None
    tr_method: str = "shade"


@dataclass(frozen=True)
class PersonProfile:
    met: float = 1.2
    clo: float = 0.5
    posture: str = "standing"


@dataclass(frozen=True)
class RiskResult:
    utci: float | None
    utci_stress_category: str | None
    phs_sweat_loss: float | None
    phs_dlim_tre: float | None
    phs_dlim_tre_sweat: float | None
    is_utci_valid: bool
    is_phs_valid: bool
