# aiforsea-traffic-management

Dear Evaluators,

Please run `Traffic Management.ipynb` from top to bottom to allow some of the intermediate data to be generated. 
The most important function that must be in defined in ram is `def preprocess()` which wraps 6 other preprocessing functions in the same cell.
This notebook has consistently hovered around 80% of my 16gb ram so 8gb may be a problem. I have been generously using del though to clean up.

To predict, please insert your dataframe into the last cell in my Traffic Management.ipynb, titled "Prediction on Test Set from Grab".
```
#test_from_grab = insert your test df here.
```

It was a great challenge that allowed me to learn things i wouldn't otherwise.

Thank you.


Required libraries:
* numpy
* pandas
* sklearn
* matplotlib
* seaborn
* dask (not really, just if you want faster random forest training)
* geohash.py


Models used: 
1. Naive  RMSE: 0.0549
2. RandomForestRegressor(max_depth = 10, n_estimators = 30)  RMSE: 0.0427
