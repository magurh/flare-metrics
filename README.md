# Flare Metrics



### Notes
----------------------------

All the required dependencies are listed in `requirements.txt`. You can install these with  `pip`, for instance, using:
```
pip install -r requirements.txt
```


### Web scrapping
----------------------------

To import data from the `validators` section of `flare-metrics.io`, navigate to the root directory and run from the command line:
```
python data_scripts/validator_scrapper.py
```

This will create a dataframe within the `data` sub-directory, with information about all current validators. 

Note: Ensure that the command line is using the same Python environments as your preferred editor.


