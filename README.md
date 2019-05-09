# pred

Prediction tool

## Usage

At the first step, create a new dataset

```python
from pred import Dataset, Predict

ds = Dataset('dataset.csv')
```

At the second step, make forecasting 

```python
pr = Predict(ds)
pr.predict()
```
