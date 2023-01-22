class JsonURLLoader:
    """
    Load JSON data from a URL.
    """

    def __init__(self, url):
        self.url = url
        
    def load(self) -> dict:
        """
        Load JSON data from a URL.

        Returns:
            dict: JSON data.
        """
        import json
        import urllib.request
        with urllib.request.urlopen(self.url) as url:
            data = json.loads(url.read().decode())
        return data

class JsonFileLoader:
    """ 
    Load JSON data from a file.
    """
    def __init__(self, filename):
        self.filename = filename

    def load(self) -> dict:
        """
        Load JSON data from a file.
        Returns:
            dict : JSON data.
        """
        import json
        with open(self.filename) as json_file:
            data = json.load(json_file)
        return data