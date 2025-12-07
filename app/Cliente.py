class Cliente:
    def __init__(self, nome, tel):
        self._nome = nome
        self._telefone = tel

    # Método GET
    def get_nome(self):
        return self._nome

    # Método SET
    def set_nome(self, nome):
        self._nome = nome
