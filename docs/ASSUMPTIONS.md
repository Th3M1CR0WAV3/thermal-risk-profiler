# Assumptions

## Environmental modeling
- `tr_method="shade"` assumes `tr = tdb` for a baseline shaded condition.
- UTCI uses the BOM-reported wind speed at 10 m (`v10m`).
- PHS uses wind speed scaled to 1.1 m with `scale_wind_speed_log`.

## PHS inputs
- Default posture is `standing`.
- Clothing (`clo`) and metabolic rate (`met`) must be provided for PHS.

## Future stages
- Shade vs sun scenarios will incorporate `pythermalcomfort` solar gain and delta MRT.
