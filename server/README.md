# NFL Sentiments Backend

## Data Sourcing
### `X` (formerly Twitter)
The original source of data was Twitter.

This backend will attempt to first refresh source data
with an `X` data [X Developer Platform](https://developer.x.com/en) API call.

### Snscrape
This project uses snsrape to attempt to scrape publicly available `X` posts.
However, there's a package issue in python > `3.10`. A [fix has been uploaded](https://github.com/JustAnotherArchivist/snscrape/blob/281ebf4a706e261e8b12956a96650f2ebbaead95/snscrape/modules/__init__.py),
however not merged. We will treat [the fork](https://github.com/ajponte/snscrape) of `snscrape`
as a git submodule for this project.

### Data Lake
The Data Lake will cache all API requests.

For this version, the cache is a CSV file, defined by the `CACHE_FILE` environment variable.

## OpenBao Secrets Manager
This project uses `OpenBao` as a secrets manager.

You can look into `config.py` to see which values you need to set.
