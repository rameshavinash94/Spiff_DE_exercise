from JsonLoaders import JsonURLLoader, JsonFileLoader
class JsonLoaderFactory:
    """
    Factory for creating JSON loaders.
    """
    def get_loader(self, source) -> JsonURLLoader or JsonFileLoader:
        """
        Create a JSON loader.

        Args:
            source (str): URL or filename.

        Raises:
            ValueError: If the source is not a URL or filename.

        Returns:
            _type_: JsonURLLoader or JsonFileLoader
        """
        
        if source.startswith(("http://", "https://")) and source.endswith(".json"):
            return JsonURLLoader(source)
        elif source.endswith(".json"):
            return JsonFileLoader(source)
        else:
            raise ValueError(source)