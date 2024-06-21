# import json file that contains the fortune cookie messages
import json
import os
import random

class FortuneCookie:
    def __init__(self) -> None:
        self.__messages = self.retrieve_messages()

    def retrieve_messages(self) -> dict:
        """Retrieve the messages from the json file

        Returns:
            dict: The messages from the json file
        """        
        try:
            base_dir = os.path.dirname(__file__)
            file_path = os.path.join(base_dir, 'text/fortune.json')
            with open(file_path, 'r') as file:
                data = json.load(file)
                return {'message': data['fortune']}
        except FileNotFoundError:
            return {'message': ['No fortune cookie messages found']}
        
    def retrieve_fortune(self) -> str:
        """Retrieve a random message from the json file

        Returns:
            str: A random message 
        """        
        return random.choice(self.__messages['message'])
