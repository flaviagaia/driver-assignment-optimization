from __future__ import annotations

import csv
import json
from pathlib import Path
from random import Random
from typing import Dict, List


PUBLIC_DATASET_REFERENCE = {
    "primary_reference": {
        "name": "NYC TLC Trip Record Data",
        "url": "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page",
        "role": "Public mobility marketplace reference used here as inspiration for distance, utilization, and last-mile matching dynamics.",
    },
    "notes": [
        "The runtime dataset is synthetic and represents candidate order-driver matches.",
        "The project focuses on dispatch scoring and assignment quality rather than exact route optimization.",
    ],
}


def _write_csv(path: Path, rows: List[Dict[str, object]]) -> None:
    if not rows:
        return
    with path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_sample_dataset(base_dir: Path, order_count: int = 80, candidates_per_order: int = 4) -> Dict[str, str]:
    rng = Random(42)
    rows: List[Dict[str, object]] = []
    for order_index in range(order_count):
        region = ["north", "south", "east", "west"][order_index % 4]
        for candidate_index in range(candidates_per_order):
            distance_to_pickup_km = round(0.4 + candidate_index * 0.8 + rng.uniform(0.0, 1.2), 2)
            driver_accept_prob = round(max(0.15, 0.9 - 0.12 * candidate_index - 0.06 * distance_to_pickup_km), 4)
            estimated_pickup_delay_min = round(3.0 + distance_to_pickup_km * 2.6 + rng.uniform(0.0, 2.0), 2)
            utilization_score = round(0.4 + ((order_index + candidate_index) % 5) * 0.1, 2)
            rows.append(
                {
                    "order_id": f"ORD-{order_index + 1:04d}",
                    "driver_id": f"DRV-{(order_index * candidates_per_order + candidate_index + 1):04d}",
                    "region": region,
                    "distance_to_pickup_km": distance_to_pickup_km,
                    "estimated_pickup_delay_min": estimated_pickup_delay_min,
                    "driver_accept_prob": driver_accept_prob,
                    "utilization_score": utilization_score,
                }
            )

    raw_dir = base_dir / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    dataset_path = raw_dir / "driver_assignment_candidates.csv"
    reference_path = raw_dir / "public_dataset_reference.json"
    _write_csv(dataset_path, rows)
    reference_path.write_text(json.dumps(PUBLIC_DATASET_REFERENCE, ensure_ascii=False, indent=2), encoding="utf-8")

    return {
        "dataset_source": "synthetic_driver_assignment_marketplace",
        "dataset_path": str(dataset_path),
        "dataset_reference_path": str(reference_path),
    }
