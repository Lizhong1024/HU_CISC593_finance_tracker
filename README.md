# HU_CISC593_finance_tracker

Final project for ***CISC 593-90- O-2025/Late Spring - Software Verification & Validation***. Unit tests for a ***Personal Finance Tracker*** implemented in Python.

## Setup
1. Install conda environment<br>
   `conda env create -f environment.yml`
2. Activate conda environment<br>
   `conda activate pftracker`
3. Install packages<br>
   `pip install -r requirements.txt`
4. Run unit tests<br>
    `pytest tests`

## How to run unit tests and generate HTML reports?
Example for ledger.py module:<br>
`pytest tests/test_ledger.py --html=reports/ledger.html --self-contained-html`