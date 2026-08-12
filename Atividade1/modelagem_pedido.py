class Pedido:

    def __init__(self, id_pedido):
        self.id_pedido = id_pedido
        self._status = "Pendente"  # Estado interno protegido contra acesso direto

    @property
    def status(self):
        return self._status

    def atualizar_status(self, novo_status):
        # Método controlado de via única para alteração de estado sensível
        self._status = novo_status