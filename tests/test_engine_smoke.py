from thermal_risk_profiler.engine import compute_risk
from thermal_risk_profiler.schemas import EnvironmentPoint, PersonProfile


def test_compute_risk_smoke() -> None:
    environment = EnvironmentPoint(tdb=32.0, rh=55.0, v10m=4.2)
    person = PersonProfile(met=2.0, clo=0.5, posture="standing")
    result = compute_risk(environment, person)

    assert result.utci is None or isinstance(result.utci, float)
    assert result.phs_sweat_loss is None or isinstance(result.phs_sweat_loss, float)
