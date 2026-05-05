from __future__ import annotations

import unittest
from pathlib import Path

from src.data_factory import build_sample_dataset
from src.modeling import run_analysis


class DriverAssignmentOptimizationTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.base_dir = Path(__file__).resolve().parents[1]

    def test_dataset_factory_creates_files(self) -> None:
        dataset_info = build_sample_dataset(self.base_dir)
        self.assertEqual(dataset_info["dataset_source"], "synthetic_driver_assignment_marketplace")
        self.assertTrue(Path(dataset_info["dataset_path"]).exists())
        self.assertTrue(Path(dataset_info["dataset_reference_path"]).exists())

    def test_analysis_contract(self) -> None:
        report = run_analysis(self.base_dir)
        self.assertEqual(report["dataset_source"], "synthetic_driver_assignment_marketplace")
        self.assertEqual(report["candidate_row_count"], 320)
        self.assertEqual(report["assigned_order_count"], 80)
        self.assertGreater(report["avg_driver_accept_prob"], 0.5)
        self.assertTrue(Path(report["assignments_artifact"]).exists())
        self.assertTrue(Path(report["report_artifact"]).exists())


if __name__ == "__main__":
    unittest.main()
