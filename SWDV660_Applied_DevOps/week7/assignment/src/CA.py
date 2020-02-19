class CA:

    class _Registration:
        def __init__(self, name, publicKey):
            self.name = name
            self.publicKey = publicKey

    def __init__(self):
        self._registrations = []

    def register(self, name, publicKey):
        """
            Register with the CA

            @param {string} name
            @param {string} publicKey
        """
        self._registrations.append(self._Registration(name, publicKey))

    def validate(self, name):
        for reg in self._registrations:
            if reg.name == name:
                return reg.publicKey
        return None
