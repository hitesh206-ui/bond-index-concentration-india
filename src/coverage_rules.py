"""Coverage classification rules for bond index concentration analysis."""

from __future__ import annotations


def classify_coverage(
    constituents_available: bool,
    weights_available: bool,
    methodology_available: bool,
) -> str:
    """Classify index coverage based on available information."""
    if constituents_available and weights_available:
        return "Full"
    if constituents_available or weights_available:
        return "Partial"
    if methodology_available:
        return "Methodology-cap-only"
    return "Insufficient"


def coverage_score(coverage_type: str) -> int:
    """Map coverage class to an ordinal score."""
    scores = {
        "Full": 3,
        "Partial": 2,
        "Methodology-cap-only": 1,
        "Insufficient": 0,
    }
    return scores.get(coverage_type, 0)
