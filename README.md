[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org) [![jupyter](https://img.shields.io/badge/Jupyter-Lab-F37626.svg?style=flat&logo=Jupyter)](https://jupyterlab.readthedocs.io/en/stable) [![Flare](https://img.shields.io/badge/flare-network-e62058.svg?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzNCIgaGVpZ2h0PSIzNCI+PHBhdGggZD0iTTkuNC0uMWEzMjAuMzUgMzIwLjM1IDAgMCAwIDIuOTkuMDJoMi4yOGExMTA2LjAxIDExMDYuMDEgMCAwIDEgOS4yMy4wNGMzLjM3IDAgNi43My4wMiAxMC4xLjA0di44N2wuMDEuNDljLS4wNSAyLTEuNDMgMy45LTIuOCA1LjI1YTkuNDMgOS40MyAwIDAgMS02IDIuMDdIMjAuOTJsLTIuMjItLjAxYTQxNjEuNTcgNDE2MS41NyAwIDAgMS04LjkyIDBMMCA4LjY0YTIzNy4zIDIzNy4zIDAgMCAxLS4wMS0xLjUxQy4wMyA1LjI2IDEuMTkgMy41NiAyLjQgMi4yIDQuNDcuMzcgNi43LS4xMiA5LjQxLS4wOXoiIGZpbGw9IiNFNTIwNTgiLz48cGF0aCBkPSJNNy42NSAxMi42NUg5LjJhNzU5LjQ4IDc1OS40OCAwIDAgMSA2LjM3LjAxaDMuMzdsNi42MS4wMWE4LjU0IDguNTQgMCAwIDEtMi40MSA2LjI0Yy0yLjY5IDIuNDktNS42NCAyLjUzLTkuMSAyLjVhNzA3LjQyIDcwNy40MiAwIDAgMC00LjQtLjAzbC0zLjI2LS4wMmMtMi4xMyAwLTQuMjUtLjAyLTYuMzgtLjAzdi0uOTdsLS4wMS0uNTVjLjA1LTIuMSAxLjQyLTMuNzcgMi44Ni01LjE2YTcuNTYgNy41NiAwIDAgMSA0LjgtMnoiIGZpbGw9IiNFNjIwNTciLz48cGF0aCBkPSJNNi4zMSAyNS42OGE0Ljk1IDQuOTUgMCAwIDEgMi4yNSAyLjgzYy4yNiAxLjMuMDcgMi41MS0uNiAzLjY1YTQuODQgNC44NCAwIDAgMS0zLjIgMS45MiA0Ljk4IDQuOTggMCAwIDEtMi45NS0uNjhjLS45NC0uODgtMS43Ni0xLjY3LTEuODUtMy0uMDItMS41OS4wNS0yLjUzIDEuMDgtMy43NyAxLjU1LTEuMyAzLjM0LTEuODIgNS4yNy0uOTV6IiBmaWxsPSIjRTUyMDU3Ii8+PC9zdmc+&colorA=FFFFFF)](https://dev.flare.network/) [<img src="https://github.com/user-attachments/assets/e545d7f0-cfac-4dc1-9112-065bc5e46f7c" width="31" alt="FTSO">](https://flare.network/ftso/)

# Flare Metrics

A set of tools for web-scrapping and analysing Flare Network's data providers. 

1. FTSOv2 metrics (delegating):
    - [x] [Flare Systems Explorer](https://songbird-systems-explorer.flare.rocks)
        -  Songbird delegation data for current entities
        -  Songbird delegation data for specific reward epochs
    - [ ] [Useyourspark monitor](https://www.useyourspark.com/analytics/monitor)

2. FTSO (v1) metrics (delegating):
    - [x] [flaremetrics.io](flaremetrics.io)
          - Compatibility for both Flare and Songbird
    - [ ] [FTSO monitor](https://flare-ftso-monitor.flare.network/data-providers)
    - [ ] [flare-base.io](https://flare-base.io)
    - [ ] [solidifi](https://solidifi.app/ftso-data-providers)

3. Validator metrics (staking): 
    - [x] [flaremetrics.io](https://flaremetrics.io)
    - [ ] [solidifi](https://solidifi.app/validators)
    - [ ] [flare.builders](https://www.flare.builders/validators)
    - [ ] [flarescan](https://flarescan.com/validators)
        

Note: Staking is currently live only on Flare. The data of the FTSO providers from [flare-metrics.io](flaremetrics.io) does not include C-chain addresses. As such, matching FTSO addresses with validator nodes can be done only based on the names. An alternative is to use a different source for extracting FTSO data, such as the [FTSO monitor](https://flare-ftso-monitor.flare.network/data-providers), which only includes FTSO data.

## Setup


Poetry is used for dependency management. Whenever new dependencies are added, run:
```
poetry install
```
To use Jupyter Lab, set the kernel to the fast-updates-monitoring environment created by poetry:
```
poetry run python -m ipykernel install --user --name=fast-updates-analysis
```
Open Jupyter lab as follows:
```
poetry run jupyter lab
```
For simply activating the virtual environment, run:
```
poetry shell
```

To add new dependencies, use: `poetry add dependency`.


## Web scrapping

There are two types of data that one can import: validator data which refers to the validator nodes on the P-chains, and FTSO data for the data providers on the C-chains. To import validator data, navigate to the root directory, activate the virtual environment with `poetry shell` and run:
```
python data_scripts/flare_metrics_validator.py
```
Alternatively, one can run the script without manually activating the shell using:
```
poetry run python data_scripts/flare_metrics_validator.py
```
The same applies to the other scripts.

This will create a dataframe within the `data` sub-directory, with information about all current validators on Flare.

For FTSO data, there are multiple available sources: [flaremetrics.io](flaremetrics.io), [Flare Systems Explorer](https://songbird-systems-explorer.flare.rocks/entities/ftsoDataProvider) (currently supporting only Songbird and testnets for FTSOv2), and [FTSO monitor](https://flare-ftso-monitor.flare.network/data-providers) for FTSOv1. Run one of the following from the root directory:
```
poetry run python data_scripts/flare_metrics_ftso.py
poetry run python data_scripts/sys_explorer_ftso.py
```
Note that the `flare_metrics_ftso.py` script will import Flare network data by default. If songbird data is needed instead, the `network` parameter within `flare_metrics_ftso.py` should be changed before running the script.

For FTSOv2, one can further uses the Flare Systems Explorer to extract data for a specific reward epoch by running (make sure to set the desired reward epoch id within the python script -- check the [Systems Explorer](https://songbird-systems-explorer.flare.rocks/reward-epoch) for the desired epochs)
```
poetry run python data_scripts/sys_explorer_epoch.py
```


