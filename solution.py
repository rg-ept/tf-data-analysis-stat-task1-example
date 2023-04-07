import pandas as pd
import numpy as np


chat_id = 42877418

def solution(x: np.array) -> float:
      err = np.random.normal(-29+np.exp(1), x.size) 
      v_mean = np.mean(x/10+err)  
      return v_mean
