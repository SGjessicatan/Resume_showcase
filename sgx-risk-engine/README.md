# SGX Bank Risk Engine

Market-risk model built from scratch on public SGX data: VaR / Expected Shortfall
(historical, parametric, GARCH-filtered), formal backtesting (Kupiec, Christoffersen),
and stress scenarios.

> Status: work in progress. Built as an independent portfolio project.
> All code and analysis are original and use public price data only.

## Roadmap
- [x] Step 1: Repo setup, data loader, data-quality checks
- [ ] Step 2: Historical and parametric VaR / ES
- [ ] Step 3: GARCH-filtered VaR
- [ ] Step 4: Backtesting (traffic-light, Kupiec, Christoffersen)
- [ ] Step 5: Stress scenarios
- [ ] Step 6: Model documentation and limitations

## Setup
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m pytest
jupyter notebook notebooks/01_data_and_returns.ipynb
```

© 2026 Jessica. All rights reserved.
