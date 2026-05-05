from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Dict, List

from .data_factory import build_sample_dataset


def _read_rows(path: str) -> List[Dict[str, str]]:
    with Path(path).open("r", encoding="utf-8", newline="") as csv_file:
        return list(csv.DictReader(csv_file))


def _score_candidate(row: Dict[str, str]) -> float:
    accept_prob = float(row["driver_accept_prob"])
    distance = float(row["distance_to_pickup_km"])
    pickup_delay = float(row["estimated_pickup_delay_min"])
    utilization = float(row["utilization_score"])
    return round((accept_prob * 0.5) + (utilization * 0.2) - (distance * 0.08) - (pickup_delay * 0.03), 4)


def _best_assignments(rows: List[Dict[str, str]]) -> List[Dict[str, object]]:
    grouped: Dict[str, List[Dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["order_id"], []).append(row)

    assignments: List[Dict[str, object]] = []
    for order_id, candidates in sorted(grouped.items()):
        best_row = max(candidates, key=_score_candidate)
        assignments.append(
            {
                "order_id": order_id,
                "driver_id": best_row["driver_id"],
                "score": _score_candidate(best_row),
                "distance_to_pickup_km": float(best_row["distance_to_pickup_km"]),
                "estimated_pickup_delay_min": float(best_row["estimated_pickup_delay_min"]),
                "driver_accept_prob": float(best_row["driver_accept_prob"]),
                "utilization_score": float(best_row["utilization_score"]),
            }
        )
    return assignments


def _mean(values: List[float]) -> float:
    return round(sum(values) / len(values), 4) if values else 0.0


def run_analysis(base_dir: Path) -> Dict[str, object]:
    dataset_info = build_sample_dataset(base_dir)
    rows = _read_rows(dataset_info["dataset_path"])
    assignments = _best_assignments(rows)

    report = {
        "dataset_source": dataset_info["dataset_source"],
        "candidate_row_count": len(rows),
        "assigned_order_count": len(assignments),
        "avg_assignment_score": _mean([row["score"] for row in assignments]),
        "avg_distance_to_pickup_km": _mean([row["distance_to_pickup_km"] for row in assignments]),
        "avg_estimated_pickup_delay_min": _mean([row["estimated_pickup_delay_min"] for row in assignments]),
        "avg_driver_accept_prob": _mean([row["driver_accept_prob"] for row in assignments]),
        "optimization_goal": "maximize acceptance and utilization while controlling pickup distance and delay",
    }

    processed_dir = base_dir / "data" / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)
    assignments_path = processed_dir / "optimized_assignments.json"
    report_path = processed_dir / "driver_assignment_report.json"
    report["assignments_artifact"] = str(assignments_path)
    report["report_artifact"] = str(report_path)
    assignments_path.write_text(json.dumps(assignments, ensure_ascii=False, indent=2), encoding="utf-8")
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report
