"""Application-level configs."""
from typing import Any

from nfl.config.confload import Loader, required, required_secret

CONFIG_LOADERS: list[Loader] = [
    # In a production system, secrets would derive from a secrets' manager.
    required(key='X_DOT_COM_API_SECRET'),
    required(key='X_DOT_COM_API_KEY'),
    required_secret(key='foo', path='test')
]

def update_config_from_environment(config: dict[str, Any]) -> None:
    """
    Return an updated config dict whose values are from the OS environment.

    :param config: The dict to update.
    """
    config.update(
        dict(loader() for loader in CONFIG_LOADERS)
    )
