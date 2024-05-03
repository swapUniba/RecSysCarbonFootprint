# Balancing Carbon Footprint and Algorithm Performance in Recommender Systems: a Comprehensive Benchmark

Repository for the paper "Balancing Carbon Footprint and Algorithm Performance in Recommender Systems: a Comprehensive Benchmark"

The system tracks the emissions of a given recommendation algorithm on a given dataset. It performs the model execution by applying the default parameters set or by applying the hyperparameters tuning carrying out the grid search. It also saves the metrics and the parameters configuration obtained during each run.

**Recommendations models, datasets and metrics refers to [@Recbole](https://recbole.io/) implementation.**

**Emission tracking is made by mean of [@CodeCarbon](https://mlco2.github.io/codecarbon/) library.**


## Requirements
* **Global requirements**: Python >= 3.7 (tested on 3.8.5 and 3.11.4)
* **System requirements**: see [requirements.txt](https://github.com/swapUniba/RecSysCarbonFootprint/blob/main/requirements.txt)


## Scripts

1. [src/tuning_tracker.py](https://github.com/swapUniba/RecSysCarbonFootprint/blob/main/src/tuning_tracker.py) performs the hyper-parameter tuning of a given algorithm on a given dataset (both passed as script’s arguments), carrying out the grid-search.

NOTES:
- All the available models and datasets are defined in [src/config/global_config.py](https://github.com/swapUniba/RecSysCarbonFootprint/blob/main/src/config/global_config.py) file.
- All the grid-search params ranges for each model are defined in [src/config/hyperparam.py](https://github.com/swapUniba/RecSysCarbonFootprint/blob/main/src/config/hyperparam/) folder.
- The results are saved in results folder.
- Parameters names are case unsensitive while parameters values are case sensitive.

**Example**
```python
$ python3 src/tuning_tracker.py --dataset=mind --model=BPR
```
2. [src/default_tracker.py](https://github.com/swapUniba/RecSysCarbonFootprint/blob/main/src/default_tracker.py) tracks the emissions of a given algorithm with default and statically defined parameters on a given dataset (both passed as script’s arguments).
Note that 

NOTES:
- All the available models and datasets are defined in [src/config/global_config.py](https://github.com/swapUniba/RecSysCarbonFootprint/blob/main/src/config/global_config.py) file.
- The deafult parameters are definded in [src/config/params_config.py](https://github.com/swapUniba/RecSysCarbonFootprint/blob/main/src/config/params_config.py) file.
- The results are saved in results_shared folder.
- Parameters names are case unsensitive while parameters values are case sensitive.
- We use this script to run data reduction experiments; to do this, use as dataset name "_\<dataset\>_\_split\_\<_n_\>", where _n_ is the amount of training data, ranging in [2,4,6,8,10].

**Example**
```python
$ python3 src/default_tracker.py --dataset=mind --model=BPR
```

**Example with data reduction**
```python
$ python3 src/default_tracker.py --dataset=mind_split_6 --model=BPR
```
3. [src/config/clear_cache.py](https://github.com/swapUniba/RecSysCarbonFootprint/blob/main/src/clear_cache.py) the libraries and modules above mentioned automatically generate a series of intermediate results, serializations and logs, this script was created to remove them from file system, especially useful in the early stages of work.

It accepts the following arguments:

| Flag | Description |
|---|---|
|--log|It removes the contents of the **log** folder.|
|--tb|It removes the contents of the **log_tensorboard** folder.|
|--results|It removes the contents of the **results** and **results_shared** folders.|
|--saved|It removes the contents of the **saved** folder.|
|--all|It removes all the previous folders.|

**Example**
```python
$ python3 src/clear_cache.py --saved
```


## Datasets

* data/amazon_books_60core_kg: dataset about books. Knowledge data is also available.
* data/mind: dataset about news. Knowledge data is not available.
* data/movielens: dataset about movies, version size 1M. Knowledge data is also available.

As we previously stated, each dataset is provided with reduced amount of training data as:
* data/amazon_books_60core_kg_split_[2,4,6,8,10]
* data/mind_split_[2,4,6,8,10]
* data/movielens_[2,4,6,8,10]

## Acknowledgments

- Huge thanks to **[@albertovalerio](https://github.com/albertovalerio)** and **[@FranchiniFelice720034](https://github.com/FranchiniFelice720034)** for the technical support.
- **[@Recbole](https://recbole.io/)**
- **[@CodeCarbon](https://mlco2.github.io/codecarbon/)**

## License

Distributed under the [MIT](https://choosealicense.com/licenses/mit/) License. See `LICENSE` for more information.