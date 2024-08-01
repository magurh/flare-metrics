# Flare Metrics

A set of tools for web-scrapping [flare-metrics.io](flare-metrics.io) and analysing Flare Network's data providers.

- [x] Validator data
- [ ] FTSO data


### Setup
----------------------------

1. Create and Activate Virtual Environment
On Windows:

```
python -m venv venv
venv\Scripts\activate
```

On MacOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```
pip install -r requirements.txt
```


### Web scrapping
----------------------------

To import data from the `validators` section of `flare-metrics.io`, navigate to the root directory and run:
```
python data_scripts/validator_scrapper.py
```

This will create a dataframe within the `data` sub-directory, with information about all current validators. 




