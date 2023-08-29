"""_summary_

Returns:
    _type_: _description_
"""
import os
import json
from urllib.parse import urlparse
import requests
from requests.exceptions import RequestException


class C8Instance(object):
    """_summary_"""

    server: str
    user: str
    password: str
    token: str

    def __init__(self, server, user, password) -> None:
        self.server = server
        self.user = user
        self.password = password

    def connect(self, renew = False):
        """_summary_

        Args:
            _self (_type_): _description_
        """
        print("connect")
        try:
            stored_token = self.get_stored_token()
            if stored_token and not renew:
                print("previous token found")
                return stored_token
            session_url = self.server + "/csi-requesthandler/api/v2/session"
            credentials = {"username": self.user, "password": self.password}
            response = requests.post(session_url, json=credentials, timeout=20)
            # This will raise an HTTPError if the response status code
            # indicates an error (4xx or 5xx).
            response.raise_for_status()
            result = response.json()
            if result["token"]:
                self.set_token(result)
                self.store_token(get_root_name(self.server))
            return result

        # Process the response data here if needed
        except RequestException as error:
            print("An error occurred:", error)

    def store_token(self, env_name):
        """_summary_

        Args:
            env_name (_type_): _description_
        """
        # Store the environment variable in a configuration file
        config = {env_name: {"token": self.token["token"]}}

        with open("token.json", "w", encoding="UTF-*") as config_file:
            json.dump(config, config_file)

    def get_stored_token(self, env_name=None):
        """_summary_

        Args:
            env_name (_type_): _description_

        Returns:
            _type_: _description_
        """
        token_filename = "token.json"

        if os.path.exists(token_filename):
            # Load the configuration from the JSON file
            with open(token_filename, "r", encoding="UTF-*") as config_file:
                config = json.load(config_file)
            if not env_name:
                env_name = get_root_name(self.server)
                store_token = config[env_name]["token"]
                return store_token

        return None

    def c8_info(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.user, self.server

    def set_token(self, token):
        """_summary_

        Args:
            token (_type_): _description_
        """
        self.token = token

    def get_token(self):
        """_summary_"""
        return self.token

    def send_query(self, query):
        """_summary_

        Args:
            query (_type_): _description_
        """
        session_url = (
            self.server + "/csi-requesthandler/RequestHandler?" + query + "&OutputJSON=2"
        )
        head = {'Content-type': 'application/json','cookie': self.get_stored_token()}
        response = requests.get(session_url, headers=head, timeout=20)
        # print (response.json())
        return response.text

def get_root_name(url):
    """_summary_

    Args:
        url (_type_): _description_

    Returns:
        _type_: _description_
    """
    parsed_url = urlparse(url)
    root_name = parsed_url.netloc
    return root_name


def main():
    """_summary_"""
    print("C8 Instance creation")


if __name__ == "__main__":
    main()
