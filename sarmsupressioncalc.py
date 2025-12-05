#!/usr/bin/env python3
"""
SARM Suppression Risk Calculator (Qualitative, Illustrative Only)

This script estimates a qualitative risk level (LOW / MODERATE / HIGH)
for HPTA suppression in a generic research scenario, based on:

- SARM compound
- Daily dose
- Duration of exposure in weeks

⚠️ Not a clinical tool. Not for human use decisions.
"""

from dataclasses import dataclass


@dataclass
class SARMProfile:
    name: str
    baseline_suppression: int  # 1 = low, 2 = moderate, 3 = high
    nominal_dose_mg: float     # “typical” daily dose band centre


# Heuristic profiles — can be tuned or extended.
SARM_PROFILES = {
    1: SARMProfile("RAD-140", baseline_suppression=3, nominal_dose_mg=10),
    2: SARMProfile("LGD-4033", baseline_suppression=3, nominal_dose_mg=10),
    3: SARMProfile("MK-2866 (Ostarine)", baseline_suppression=2, nominal_dose_mg=20),
    4: SARMProfile("YK-11", baseline_suppression=3, nominal_dose_mg=10),
    5: SARMProfile("S-23", baseline_suppression=3, nominal_dose_mg=10),
}


def choose_sarm() -> SARMProfile:
    print("Select SARM:")
    for idx, profile in SARM_PROFILES.items():
        print(f"{idx}) {profile.name}")
    raw = input("Enter number: ").strip()
    try:
        choice = int(raw)
        return SARM_PROFILES[choice]
    except (ValueError, KeyError):
        raise ValueError("Invalid selection.")


def dose_score(dose_mg: float, nominal: float) -> int:
    """
    Score dose intensity relative to a nominal band.
    Returns 0 (low), 1 (medium), 2 (high).
    """
    if dose_mg <= 0:
        return 0
    ratio = dose_mg / nominal if nominal > 0 else 1.0
    if ratio <= 0.75:
        return 0
    elif ratio <= 1.25:
        return 1
    else:
        return 2


def duration_score(weeks: float) -> int:
    """
    Score duration as 0 (short), 1 (medium), 2 (extended).
    """
    if weeks <= 0:
        return 0
    if weeks <= 4:
        return 0
    elif weeks <= 8:
        return 1
    else:
        return 2


def map_score_to_risk(total_score: int) -> str:
    """
    Convert combined score to qualitative risk band.
    """
    if total_score <= 3:
        return "LOW"
    elif total_score <= 5:
        return "MODERATE"
    else:
        return "HIGH"


def interpret_risk(profile: SARMProfile, total_score: int, risk_band: str) -> str:
    """
    Generate a short human-readable interpretation.
    """
    lines = []
    lines.append(f"Suppression risk: {risk_band}\n")

    if risk_band == "LOW":
        lines.append(
            "Interpretation:\n"
            f"This scenario combines a relatively {('less' if profile.baseline_suppression == 1 else 'moderately')}"
            " suppressive profile with lower overall dose/duration."
            " Within this heuristic model, the relative risk of marked HPTA suppression is lower than in more intensive scenarios."
        )
    elif risk_band == "MODERATE":
        lines.append(
            "Interpretation:\n"
            "The overall exposure sits in a mid-range band in this model."
            " A meaningful degree of HPTA suppression is plausible in research settings,"
            " especially if multiple moderate factors are combined."
        )
    else:  # HIGH
        lines.append(
            "Interpretation:\n"
            "This scenario combines a suppressive compound profile with higher dose and/or extended duration,"
            " which increases the likelihood of notable HPTA suppression in research models."
        )

    lines.append(
        "\nNote: This is a qualitative, heuristic model only and does not predict outcomes for individuals."
    )
    return "\n".join(lines)


def main():
    try:
        profile = choose_sarm()
    except ValueError as e:
        print(e)
        return

    try:
        dose_raw = input("\nEnter daily dose in mg (e.g. 10): ").strip()
        dose_mg = float(dose_raw)
        if dose_mg < 0:
            raise ValueError

        dur_raw = input("Enter duration in weeks (e.g. 8): ").strip()
        weeks = float(dur_raw)
        if weeks < 0:
            raise ValueError
    except ValueError:
        print("Please enter non-negative numeric values for dose and duration.")
        return

    base = profile.baseline_suppression
    d_score = dose_score(dose_mg, profile.nominal_dose_mg)
    t_score = duration_score(weeks)

    total = base + d_score + t_score
    risk = map_score_to_risk(total)

    print(f"\nCompound: {profile.name}")
    print(f"Baseline suppressiveness class: {base} (1=low, 2=moderate, 3=high)")
    print(f"Dose score: {d_score} (0=low, 1=medium, 2=high)")
    print(f"Duration score: {t_score} (0=short, 1=medium, 2=extended)")
    print(f"Combined score: {total}")

    print()
    print(interpret_risk(profile, total, risk))


if __name__ == "__main__":
    main()
