### Timeseries analysis of commodity data

get_historical_prices_save.py is a python command line program to fetch historical data from investing.com.

The program basically makes use of requests and pandas' html parser.

#### Usage:

`python getCommodityPrice.py <start date> <end date> <commodity name>`

*Parameters:*

`start date`: beginning of the date range for commodity data. YYYY-MM-DD  
`end date`: ending of the date range for commodity data. YYYY-MM-DD  
`commodity name`: gold or silver  

#### Output:
<mean> <variance> <commodity name>
