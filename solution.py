import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


chat_id = 819168380

def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:
  count = np.array([x_success, y_success])
  nobs = np.array([x_cnt, y_cnt])
  zstat, p_value = proportions_ztest(count, nobs, alternative='larger')
  return p_value < 0.04
