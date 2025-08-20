"""Application-level configs."""
from typing import Any

from nfl.config.confload import Loader, required, required_secret, optional, to_bool

CONFIG_LOADERS: list[Loader] = [
    # These are optional for now. Later decide which should be required.
    required(key='BAO_ADDR'),
    required(key='OPENBAO_SECRETS_PATH'),

    # Override to have the X API wait when we encounter a rate limit.
    optional(
        key='X_DOT_COM_WAIT_ON_RATE_LIMIT',
        converter=to_bool, default_val='False'
    ),

    # Override to default to web scraping if the X API fails.
    optional(
        key='X_DOT_COM_WEBSCRAPE_BACKUP',
        converter=to_bool, default_val='True'
    ),

    optional(
        key='X_DOT_CON_MAX_RESULTS',
        default_val='20'
    ),

    optional(
        key='CACHE_FILE',
        default_val='cache.csv'
    )
]

SECRETS_LOADERS: list[Loader] = [
    required_secret(key='X_DOT_COM_API_SECRET', path='test'),
    required_secret(key='X_DOT_COM_API_KEY', path='test'),
    # todo: For local testing, we're using a bearer over API keys.
    required_secret(key='X_DOT_COM_BEARER_TOKEN', path='test')
]

def update_config_from_environment(config: dict[str, Any]) -> None:
    """
    Return an updated config dict whose values are from the OS environment.

    :param config: The dict to update.
    """
    config.update(
        dict(loader() for loader in CONFIG_LOADERS)
    )

def update_config_from_secrets(config: dict[str, Any]) -> None:
    config.update(
        dict(loader() for loader in SECRETS_LOADERS)
    )
