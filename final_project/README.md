# ReDI School final project: battery state-of-charge estimation

Estimate continuous SOC (0–1) from temperature, voltage and current in four
MathWorks simulated recordings. Compare linear regression, polynomial regression,
decision tree, random forest and support vector regression.

## Files
- `state_of_charge_estimation.ipynb`: step-by-step loading, exploration, cleaning,
  chronological splitting, scaling, model comparison and evaluation.
- `Classifiers_1.ipynb`: teaching-style reference (not required to run this project).
- `dataset/BSOC_*_degrees.mat`: original MATLAB X/Y arrays (unchanged).
- `11. Machine Learning Final Project Intro A26.pdf`: course requirements.
- `requirements.txt`: Python dependencies.
- `outputs/simple_notebook/`: cleaned data, figures, validation/test metrics,
  test predictions, run settings and the final fitted pipeline from the simplified notebook.
  Existing files directly inside `outputs/` belong to the previous version and are retained.
- `final_presentation/`: existing presentation materials.

## Run
Use Python 3.11+ in an isolated environment, from this folder:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab state_of_charge_estimation.ipynb
```

On Windows, activate with `.venv\Scripts\activate` instead. Select that Python
kernel and **Restart Kernel and Run All Cells**. Runtime varies by hardware; kernel
SVR is the most expensive model. The default common training budget is 20,000 rows
per candidate/final fit. Set `MAX_TRAIN_SAMPLES = None` for full-data training.
Validation and test metrics always use all rows in those partitions.

## Libraries
The analysis uses NumPy, pandas, SciPy (MATLAB loading), Matplotlib and
scikit-learn. Joblib saves the fitted pipeline; JupyterLab and ipykernel run the
notebook. `pathlib` and `json` are part of Python. No seaborn, oversampling or
extra tuning library is needed.

## Method and outputs
- Load all four files with `scipy.io.loadmat`, retaining source/sample metadata.
- Treat `nominal_ambient_temp_C` as an unverified filename-derived label: the
  supplied 0-degree file bottoms out near 10°C, while the 10-degree file approaches
  0°C. Verify original simulation settings before interpreting these groups;
  no filenames or labels are silently corrected. Models use measured temperature.
- Check missing/infinite/physically impossible values, repeated measurements,
  sample identities, constant inputs, distributions and SOC-range coverage.
- Preserve legitimate repeated observations and plausible unusual values;
  inspect box plots rather than automatically deleting statistical outliers.
- Use scikit-learn chronological 60/20/20 train/validation/test splits within each
  recording, with 60-sample-position boundary gaps. The sample index is not an
  imported timestamp. Data are correlated simulations, not independent batteries.
- Fit min–max scaling inside training-only pipelines; retain SOC's physical 0–1
  scale. Held-out inputs outside training extrema may scale outside 0–1; do not
  clip them or use their extrema to fit the scaler.
- Choose the family/hyperparameters by validation RMSE, then refit the locked
  winner on the budgeted development data and evaluate once on test data.
- Report MAE/RMSE in **SOC percentage points**, R², baseline, residuals,
  subgroup errors and validation permutation importance. SOC-bin bars check target coverage, not
  classification imbalance; no classification accuracy or SMOTE is used.

Inside `outputs/simple_notebook/`, `clean_battery_soc.csv.gz` contains all retained
observations in original units, split labels and training-subset flags.
For inference, use that folder's `best_soc_pipeline.joblib` with raw columns in
the order `Temp`, `Voltage`, `Current`; the pipeline handles scaling. Load only
trusted joblib files. `run_settings.json` records the seed, training budget,
boundary gap, selected settings and measured test results. The notebook keeps
its own executed tables and plots so the explanation can be followed cell by cell.

## Sources, limitations and AI transparency
[MathWorks preparation example](https://www.mathworks.com/help/deeplearning/ug/prepare-data-for-battery-state-of-charge-estimation.html).
Direct automated access returned HTTP 403; indexed documentation supplied context
and the notebook verifies the actual local arrays. Check source redistribution
terms before publishing the supplied assets.

OpenCode assisted with notebook code, explanatory drafts and simplification to
match the reference notebook's short teaching cells. Review, adapt and
understand the work, document your own decisions/interpretations, and confirm the
scope of assistance with your teacher under the course AI policy. Complete the
notebook's conclusion prompts yourself. This simulated-data educational benchmark
is **not** a validated battery-management or safety system.
