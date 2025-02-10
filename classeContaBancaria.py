from abc import ABC,abstractmethod

from classePessoa import Pessoa
from classeBanco import Banco


class  ContaBancaria(ABC):
    def __init__(self,titular: Pessoa,banco: Banco,numeroConta: int,saldo: float,senha:str):
        self._titular = titular
        self._banco = banco
        self._numeroConta = int(numeroConta)
        self._saldo = float(saldo)
        self._senha = str(senha)
    
    
    @property
    def titular(self):
        return f"{self._titular}"
    
    @titular.setter
    def titular(self,novoTitular):
        if isinstance(novoTitular, Pessoa):
            self._titular = novoTitular
        else:
            raise ValueError("Erro ao inserir no campo titular, o titular deve ser um objeto da classe Pessoa.")
    
    @property
    def banco(self):
        return f"{self._banco}"
    
    @banco.setter
    def banco(self,novoBanco):
        if isinstance(novoBanco, Banco):
            self._banco = novoBanco
        else:
            raise ValueError("Erro ao inserir no campo banco, o banco deve ser um objeto da classe Banco.")
        
    @property
    def numeroConta(self):
        return f"{self._numeroConta}"
    
    @numeroConta.setter
    def numeroConta(self,novoNumeroConta):
        if isinstance(novoNumeroConta, int) and novoNumeroConta > 0:
            self._numeroConta = novoNumeroConta
        else:
            raise ValueError("Erro ao inserir no campo numero Conta, campo deve conter apenas digitos positivos.")
    
    @property
    def saldo(self):
        return f"R$ {self._saldo:.2f}"
    
    
    @saldo.setter
    def saldo(self,novoSaldo):
        if isinstance(novoSaldo, float) and novoSaldo >=0:
            self._saldo = novoSaldo
        else:
            raise ValueError("Erro ao inserir campo saldo, o campo pode conter valor 0 ou maior.")
    
    
    @property
    def senha(self):
        return f"{self._senha}"
    
    @senha.setter
    def senha(self,novaSenha):
        if isinstance(novaSenha, str) and len(novaSenha) >= 8:
            self._senha = novaSenha
        else:
            raise ValueError("Erro ao criar nova senha, campo deve conter no minimo 8 caracteres")

    
    @abstractmethod
    def deposito(self,valorDeposito):
        if valorDeposito <= 0:
            print("Valor de deposito não pode ser 0 ou negativo")
        
        self._saldo += valorDeposito
    
    
    @abstractmethod
    def deposito(self):
        valorDeposito = float(input("Informe o valor de deposito : "))
        if valorDeposito <= 0:
            print("Valor de deposito não pode ser igual ou menor que 0")
        self._saldo += valorDeposito
    
    
    @abstractmethod
    def verificaSenha(self,senha) -> bool:
        if senha == self._senha:
            return True
    
    
    @abstractmethod
    def verificaSenhaInput(self) -> bool:
        pass
        senha = input("Informe a senha da conta : ")
        if senha == self._senha:
            return True
        else:
            return False
        
        
    @abstractmethod
    def saque(self):
        if not self.verificaSenhaInput():
            print("Senha incorreta")
        
        if self.verificaSenhaInput():
            valorSaque = float(input("Informe o valor do saque R$ : "))
            if valorSaque <= self._saldo:
                self.saldo -= valorSaque
            else:
                print("Valor de saque acima do limite disponível em conta.")
    
    
    @abstractmethod
    def saque(self,valorSaque):
        if not self.verificaSenhaInput():
            print("Senha incorreta")
            
        if valorSaque <= self._saldo:
            self._saldo -= valorSaque
        else:
            print("Valor de saque acima do limite disponível em conta.")
            
            
        