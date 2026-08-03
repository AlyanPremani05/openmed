"""Add an eval CLI to list, describe and compare benchmark suites and reports (Issue: #286)"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping

from openmed.eval.datasets.licenses import license_for
from openmed.eval.report import BenchmarkReport
from openmed.eval.suites import SUPPORTED_SUITES, suite_metadata, validate_suite_name

from ._output import (
    EXIT_ERROR,
    EXIT_USAGE,
    CliError,
    emit,
    emit_error,
    wants_json,
)

#Fallback for suites which do not contain the task metadata.

_TASK_FALLBACK: Mapping[str, str] = {
    "golden": "Synthetic-only golden de-identification fixtures suite",
    "i2b2": "credentialed i2b2 de-identification suite",
    "n2c2": "UNDEFINED suite",
    "shield": "clinical de-identification suite",
    "policy_compliance": "Policy-profile compliance suite",
    "multimodal_dicom": "This suite certifies the zero residual PHI claim for "
    "OpenMed's DICOM de-identification path",
    "code_mixed_routing": "code-mixed Hinglish de-identification suite",
    "india_health_id_leakage": "India health-ID leakage detection suite",
    "indian_multi_id": "Indian multi-identifier recognition suite",
    "indic-name-consistency": "Indic name consistency suite",
    "grounding_calibration": "Offline grounding calibration",
}

def add_benchmark_command(subparsers: argparse._SubParsersAction) -> None:
     _add_list_suites_command(subparsers)
     _add_describe_suites_command(subparsers)
     _add_compare_command(subparsers)




def _add_list_suites_command(subparsers: argparse._SubParsersAction) -> None:
     preview_parser = subparsers.add_parser(
            "list-suites",
            help="ist every registered benchmark suite with task, access, and license.",
        )
     preview_parser.set_defaults(handler=_handle_list_suites)

def _add_describe_suites_command(subparsers: argparse._SubParsersAction) -> None:
     preview_parser = subparsers.add_parser(
          "describe",
          help="Describe a suite's label/category map and access requirement."
        )
     preview_parser.add_argument(
          "suite",
          help=f"Suite name. Includes: {', '.join(SUPPORTED_SUITES)}",
        )
     preview_parser.set_default(handler=_handle_describe_suites)


def _add_compare_command(subparsers: argparse._SubParsersAction) -> None:
     pass


def _handle_list_suites():
    pass

def _handle_describe_suites():
     pass