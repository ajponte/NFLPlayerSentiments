# Note: This script is very much for dev/test purposes only.
"""Utils for interacting with Hashicorp/Openbao."""
import os

import hvac


class SecretsManagerException(Exception):
    def __init__(self, message: str, cause: Exception | None = None):
        self._message = message
        self._cause = cause

    @property
    def message(self) -> str:
        return self._message

    @property
    def cause(self) -> Exception:
        return self._cause

class OpenBaoApiClient:
    """API client wrapper for OpenBao."""
    def __init__(self):
        # todo: Add RSA cert
        self._client = hvac.Client(
            # `BAO_ADDR`, `VAULT_TOKEN` are the suggested env var names from Hashicorp.
            url=os.environ.get('BAO_ADDR', None),
            token=os.environ.get('VAULT_TOKEN', None)
        )
        self.__is_authenticated(self._client)
        print('Hashicorp Secrets client authenticated.')


    def add_secret_value(self, *, path: str, secret: dict) -> dict:
        """
        Writes the secret under `secrets/path`

        :param path: Secrets path.
        :param secret: Secret key/value pair as a dict.
        :return: The response from setting the secret in the vault.
        :raise: SecretsManagerException - Upon error.
        """
        try:
            create_response = self._client.secrets.kv.v2.create_or_update_secret(
                path=path,
                secret=secret
            )
            print(f'Set secret value at path {path}')
            return create_response
        except Exception as e:
            message = f'Exception while setting secret value at path {path}'
            print(message)
            raise SecretsManagerException(message, cause=e) from e

    def read_secret_value(self, *, path: str) -> dict:
        """
        Reads secrets from the path.

        :param path: The secrets path to read from.
        :return: The read response data.
        :raise: SecretsManagerException - Upon error.
        """
        try:
            read_response = self._client.secrets.kv.read_secret_version(
                path=path,
                # See https://github.com/hvac/hvac/pull/907
                raise_on_deleted_version=False
            )
            print(f'Successfully read secrets from path {path}')
            return read_response['data']
        except Exception as e:
            message = f'Exception while reading secret value at path {path}'
            print(message)
            raise SecretsManagerException(message, cause=e) from e

    @classmethod
    def __is_authenticated(cls, client: hvac.Client):
        """Return True only if the Client has been authenticated."""
        assert client.is_authenticated(), 'Hashicorp is not authenticated!'

# def test_bao():
#     client = OpenBaoApiClient()
#     assert client._client.is_authenticated()
#     print('Bao authenticated')
#
#     client.add_secret_value(path='test', secret={'foo': 'bar'})
#
#     resp = client.read_secret_value(path='test')
#     print(f'resp: {resp}')
#
# test_bao()
