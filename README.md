# Endocrine Response Lab — Open Research Toolkit

The **Endocrine Response Lab** is an open-source toolkit for exploring how different compounds may influence the hypothalamic–pituitary–testicular axis (HPTA), with a particular focus on **SERMs (such as enclomiphene)** and **selective androgen receptor modulators (SARMs)** in research models.

> ⚠️ **Important:** All models and calculators in this repository are **for educational and research discussion only**.  
> They are **not** medical tools, are not validated for clinical decision-making, and are **not** intended to guide human use of any substance.

---

## 🔍 What this project provides

This repository collects:

- **Simple endocrine modelling scripts** (Python)  
- **Research-focused calculators**, e.g.:
  - Enclomiphene dose–response visualisation (testosterone / LH trend modelling)  
  - SARM suppression likelihood scoring (qualitative risk model)  
- **Documentation pages** that explain:
  - HPTA feedback basics  
  - How SERMs differ mechanistically from SARMs  
  - How suppression and recovery are conceptualised in research models  

The aim is to make endocrine concepts **more transparent and reproducible** for researchers, developers and educators.

---
Further information & Sourcing : [Enclomiphene in the UK](https://maxmusclelabs.com/buy-enclomiphene-uk/)

## 🧰 Included tools (initial release)

### 1. Enclomiphene Dose–Response Model

Script: `scripts/enclomiphene_dose_model.py`  
Docs: `docs/enclomiphene-dose-response.md`

This script contains a **very simple, parameterised dose–response curve** that estimates relative changes in:

- LH  
- Total testosterone  
- Estradiol (qualitative trend)

Based on dose tiers commonly discussed in the literature (e.g. 6.25–50 mg/day).  
It’s designed as a **starting point for simulation**, not a substitute for real clinical data.

---

### 2. SARM Suppression Risk Calculator

Script: `scripts/sarm_suppression_calculator.py`  
Docs: `docs/sarm-suppression-calculator.md`

This tool models **relative suppression risk** (low / moderate / high) for different SARMs, based on:

- Compound “suppressiveness class”  
- Dose  
- Duration of exposure  

It outputs a simple risk score and a short textual interpretation for research discussion.

---

## 📚 Documentation & GitHub Pages

The `/docs` folder is structured so it can be served via **GitHub Pages** as a small documentation site:

- `docs/index.md` — Project overview + navigation  
- `docs/enclomiphene-dose-response.md` — Deep dive on the enclomiphene model  
- `docs/sarm-suppression-calculator.md` — Explanation of suppression modelling  
- `docs/hpta-recovery-model.md` — Conceptual notes on recovery after suppression  

Once GitHub Pages is enabled, these become browseable HTML pages that can be cited and linked as supporting material.

---

## 🚀 Getting started

### 1. Install dependencies

Currently the scripts only require Python ≥3.9 and `matplotlib` for optional plotting:

```bash
pip install -r requirements.txt

