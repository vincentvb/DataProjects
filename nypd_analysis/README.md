# NYPD Analysis

This project examines the racial breakdown of complaints filed to the NYPD and plots the data using both pie and line charts.

All data is provided by [ProPublica](https://www.propublica.org/datastore/dataset/civilian-complaints-against-new-york-city-police-officers).

### Setting up Environment

Ensure you have Python3 and pip installed:

```
brew install python
```

Install project dependencies:

```
pip install -r requirements.txt
```

### Running Scripts

You can run the following scripts to either generate the line charts, pie charts, or all of them:

```
CHART=pie python init.py //generates pie charts

CHART=line python init.py //generates line charts

python init.py //generates all charts
```