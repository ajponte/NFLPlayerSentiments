# NFL Sentiments Backend

## Data Sourcing
### `X` (formerly Twitter)
The original source of data was Twitter.

This backend will attempt to first refresh source data
with an `X` data [X Developer Platform](https://developer.x.com/en) API call.

### Data Lake
The Data Lake will cache all API requests.

For this version, the cache is a CSV file, defined by the `CACHE_FILE` environment variable.

## OpenBao Secrets Manager
This project uses `OpenBao` as a secrets manager.

You can look into `config.py` to see which values you need to set.
