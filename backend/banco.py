class Conta:
    def __init__(self, numero: str):
        self.numero = numero
        self.saldo = 0.0  # Saldo inicial igual a zero[cite: 2]
        # Nota: A conta tem apenas os atributos número e saldo[cite: 3]


class BancoService:
    def __init__(self):
        self.contas = {}  # Dicionário em memória para armazenar as contas[cite: 2]

    def cadastrar_conta(self, numero: str) -> bool:
        """
        Solicita um número e cria uma conta com este número e saldo igual a zero[cite: 2].
        Retorna True se cadastrada com sucesso, ou False se a conta já existir.
        """
        if numero in self.contas:
            return False  # Conta já existe
        self.contas[numero] = Conta(numero)
        return True