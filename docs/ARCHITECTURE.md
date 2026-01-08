# Architecture

## Overview
The project is organized around a small core engine that computes thermal indices
for a single environment/person point. Future stages add BOM data access and
scenario modeling without changing the core schema.

## Modules
- `thermal_risk_profiler.schemas`: dataclasses used across the project.
- `thermal_risk_profiler.engine`: stage 0 computation engine for UTCI + PHS.
- `thermal_risk_profiler.cli`: minimal CLI for invoking the engine.

## Staging strategy
- **Stage 0:** deterministic computation from provided inputs.
- **Stage 1:** add BOM observation fetching, mapping to `EnvironmentPoint`.
- **Stage 2:** expand `EnvironmentPoint` with shade vs sun parameters (solar gain).
- **Stage 3:** surface risk tiers and optional UI outputs.
