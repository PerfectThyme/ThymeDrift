def ValidationStep(object):
    def __init__(self, name: str = None) -> None:
        self.name = name
        self.validations = []
