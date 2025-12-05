# Enclomiphene Dose–Response Model

This module provides a **simple, heuristic model** of how enclomiphene dose tiers might influence:

- Luteinising hormone (LH)  
- Total testosterone  
- Estradiol (E2) trends

in a **generic research scenario**.

It is designed as an educational tool for understanding **directional changes**, not as a clinically accurate predictor.

---

## 🎯 What the model does

The Python script `scripts/enclomiphene_dose_model.py`:

- Accepts a daily oral dose input (e.g. 6.25, 12.5, 25, 50 mg)  
- Maps that dose into a **relative response band** using a simple curve  
- Outputs approximate percentage changes for:
  - LH  
  - Testosterone  
  - A qualitative estradiol trend (e.g. “slight increase”, “moderate increase”)  

Under the hood, the model uses:

- A basic **sigmoid-shaped relationship** between dose and response  
- Hard caps to prevent unrealistic values  
- Conservative defaults that can be adjusted in code

---

## 🧪 Example usage

From the project root:

```bash
python scripts/enclomiphene_dose_model.py
