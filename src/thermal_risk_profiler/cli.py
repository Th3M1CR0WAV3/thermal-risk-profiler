from __future__ import annotations

import argparse
import json

from .engine import compute_risk, risk_result_to_dict
from .schemas import EnvironmentPoint, PersonProfile


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compute UTCI and PHS for a point in time.")
    parser.add_argument("--tdb", type=float, required=True, help="Dry-bulb temperature (°C)")
    parser.add_argument("--rh", type=float, required=True, help="Relative humidity (%)")
    parser.add_argument("--v10m", type=float, required=True, help="Wind speed at 10 m (m/s)")
    parser.add_argument(
        "--tr", type=float, default=None, help="Mean radiant temperature (°C)"
    )
    parser.add_argument(
        "--tr-method",
        choices=["shade", "sun"],
        default="shade",
        help="Tr method (shade assumes tr=tdb).",
    )
    parser.add_argument("--met", type=float, default=1.2, help="Metabolic rate (met)")
    parser.add_argument("--clo", type=float, default=0.5, help="Clothing insulation (clo)")
    parser.add_argument(
        "--posture",
        type=str,
        default="standing",
        choices=["standing", "seated"],
        help="Posture used in PHS model.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    environment = EnvironmentPoint(
        tdb=args.tdb,
        rh=args.rh,
        v10m=args.v10m,
        tr=args.tr,
        tr_method=args.tr_method,
    )
    person = PersonProfile(met=args.met, clo=args.clo, posture=args.posture)
    result = compute_risk(environment, person)

    print(json.dumps(risk_result_to_dict(result), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
