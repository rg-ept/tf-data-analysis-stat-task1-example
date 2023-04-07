import pandas as pd
import numpy as np


chat_id = 42877418

def solution(x: np.array) -> float:
      err = np.random.normal(loc=-29, scale=np.exp(1), size=x.shape) 
      v_mean = np.mean(x + err)  
      return v_mean / 10
