class Singleton:
    _unique_instance = None

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if not cls._unique_instance:
            cls._unique_instance = super().__new__(cls)
            cls._unique_instance._value = None
        return cls._unique_instance

    def getValue(self) -> str:
        return self._value

    def setValue(self, value: str):
        self._value = value
