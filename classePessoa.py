class Pessoa:
    def __init__(self,nome: str,sobrenome: str,idade: int,cpf:str = ''):
        self.nome = str(nome)
        self.sobrenome = str(sobrenome)
        self.idade = int(idade)
        self.__cpf = str(cpf)
        self.__contasBancarias = []
    
    
    @property
    def cpf(self):
        return f"{self.__cpf}"
    
    @cpf.setter
    def cpf(self,cpf):
        if isinstance(cpf, str) and len(cpf) == 11 and cpf.isdigit():
            self.__cpf = cpf
        else:
            raise ValueError("Erro ao inserir cpf, prencher este campo com 11 digitos sem espaco, ponto e hifen entre cada digito.")
    
    def info(self):
        print(f"Nome: {self.nome}")
        print(f"Sobrenome: {self.sobrenome}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}\n")
    
    
    def infoContas(self):
        for conta in self.__contasBancarias:
            conta.info()

