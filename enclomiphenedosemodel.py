#!/usr/bin/env python3
"""
Enclomiphene Dose–Response Model (Illustrative Only)

This script models a simple, heuristic relationship between daily
enclomiphene dose and relative changes in LH and testosterone in a
generic research context.

⚠️ Not a clinical tool. Not for human dosing decisions.
"""

import math

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


# ----- Tunable parameters (heuristic, not data-derived) -----

# Max relative % increase for LH and testosterone at high doses
MAX_LH_INCREASE = 120.0     # %
MAX_T_INCREASE = 80.0       # %

# Dose at which ~50% of max effect is reached (mg)
LH_ED50 = 12.5
T_ED50 = 12.5

# Curve steepness
LH_STEEPNESS = 0.25
T_STEEPNESS = 0.22


def sigmoid_response(dose_mg: float, max_effect: float, ed50: float, k: float) -> float:
    """
    Simple sigmoidal dose–response curve.
    Returns a percentage change relative to baseline.
    """
    if dose_mg <= 0:
        return 0.0
    return max_effect / (1.0 + math.exp(-k * (dose_mg - ed50)))


def estradiol_trend(t_increase_pct: float) -> str:
    """
    Qualitative estradiol trend based on testosterone increase.
    This is intentionally coarse and descriptive only.
    """
    if t_increase_pct < 10:
        return "minimal change"
    elif t_increase_pct < 30:
        return "slight increase"
    elif t_increase_pct < 60:
        return "moderate increase"
    else:
        return "marked increase"


def estimate_effects(dose_mg: float) -> dict:
    lh_change = sigmoid_response(dose_mg, MAX_LH_INCREASE, LH_ED50, LH_STEEPNESS)
    t_change = sigmoid_response(dose_mg, MAX_T_INCREASE, T_ED50, T_STEEPNESS)
    e2_trend = estradiol_trend(t_change)

    return {
        "dose_mg": dose_mg,
        "lh_pct": round(lh_change, 1),
        "t_pct": round(t_change, 1),
        "e2_trend": e2_trend,
    }


def print_effects(result: dict) -> None:
    print("\nEstimated relative effects (illustrative only):")
    print(f"- LH change:        +{result['lh_pct']} %")
    print(f"- Testosterone:     +{result['t_pct']} %")
    print(f"- Estradiol trend:  {result['e2_trend']}")
    print(
        "\nNote: This model is heuristic and for educational use only.\n"
        "It is not validated for clinical or individual prediction."
    )


def plot_curve() -> None:
    if plt is None:
        print("matplotlib is not installed; skipping plot.")
        return

    doses = [x / 2 for x in range(0, 101)]  # 0–50 mg in 0.5 mg steps
    lh_values = [sigmoid_response(d, MAX_LH_INCREASE, LH_ED50, LH_STEEPNESS) for d in doses]
    t_values = [sigmoid_response(d, MAX_T_INCREASE, T_ED50, T_STEEPNESS) for d in doses]

    plt.figure()
    plt.plot(doses, lh_values, label="LH (%)")
    plt.plot(doses, t_values, label="Testosterone (%)")
    plt.xlabel("Daily enclomiphene dose (mg)")
    plt.ylabel("Estimated change vs baseline (%)")
    plt.title("Illustrative Enclomiphene Dose–Response Curve")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    try:
        raw = input("Enter enclomiphene daily dose in mg (e.g. 12.5): ").strip()
        dose = float(raw)
        if dose < 0:
            raise ValueError
    except ValueError:
        print("Please enter a non-negative numeric dose value.")
        return

    result = estimate_effects(dose)
    print_effects(result)

    show_plot = input("\nPlot illustrative dose–response curves? [y/N]: ").strip().lower()
    if show_plot == "y":
        plot_curve()


if __name__ == "__main__":
    main()
