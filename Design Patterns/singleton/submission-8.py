class Singleton:
    _unique_instance = None
    _initialized = False

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if not cls._unique_instance:
            cls._unique_instance = super().__new__(cls)
        return cls._unique_instance

    def __init__(self):
        if self.__class__._initialized:
            self._value = None
            self.__class__._initialized = True
        return


    def getValue(self) -> str:
        return self._value

    def setValue(self, value: str):
        self._value = value
