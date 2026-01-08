# Thermal Risk Profiler

A lightweight demo tool that uses `pythermalcomfort` to compute UTCI and PHS thermal
stress indices for a single point in time. It is designed as a staged, extensible
project that will later incorporate Australian BOM weather observations.

## Repository name (proposal)
`thermal-risk-profiler`

## Folder structure (proposal)
```
thermal-risk-profiler/
├── docs/
├── src/thermal_risk_profiler/
├── tests/
└── .github/workflows/
```

## Roadmap
- **Stage 0 (current):** engine that computes UTCI + PHS from provided inputs.
- **Stage 1:** fetch BOM observations for a location + timestamp (nearest station).
- **Stage 2:** add “shade vs sun” scenarios using `pythermalcomfort` solar gain / delta MRT.
- **Stage 3:** polish UI/outputs and add simple risk tiers.

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
```

## Example usage
```bash
python -m thermal_risk_profiler \
  --tdb 32 \
  --rh 55 \
  --v10m 4.2 \
  --tr-method shade \
  --met 2.0 \
  --clo 0.5 \
  --posture standing
```

## Notes
See `docs/ARCHITECTURE.md` and `docs/ASSUMPTIONS.md` for implementation details and
assumptions behind the current stage.
