"""Application-level configs."""
from typing import Any

from nfl.config.confload import Loader, required, required_secret, optional

CONFIG_LOADERS: list[Loader] = [
    optional(key='OPENBAO_SECRETS_PATH', default_val='test'),
]

SECRETS_LOADERS: list[Loader] = [
    required_secret(key='X_DOT_COM_API_SECRET', path='test'),
    required_secret(key='X_DOT_COM_API_KEY', path='test'),
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
