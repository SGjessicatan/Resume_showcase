import numpy as np
import pandas as pd

from src.data import log_returns


def test_log_returns_shape_and_value():
    prices = pd.DataFrame({"A": [100.0, 110.0, 121.0]})
    r = log_returns(prices)
    assert len(r) == 2
    assert np.isclose(r["A"].iloc[0], np.log(1.1))
