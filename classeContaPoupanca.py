from classeContaBancaria import ContaBancaria


class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, banco, numeroConta, saldo, senha,rendimento: float,saquesMensais: int = 3):
        super().__init__(titular, banco, numeroConta, saldo, senha)
        self.__rendimento = rendimento
        self.__saquesMensais = saquesMensais
    
    
    @property
    def rendimento(self):
        return f"R$ {self.__rendimento:.2f}"
    
    @rendimento.setter
    def rendimento(self,novoRendimento):
        if isinstance(novoRendimento, float) and novoRendimento > 0:
            self.__rendimento = novoRendimento
            
    @property
    def saquesMensais(self):
        return f"{self.__saquesMensais}"
    
    @saquesMensais.setter
    def saquesMensais(self):
        pass
    
    
    def info(self):
        print(f"{self.banco}")
        print(f"{self.numeroConta}")
        print(f"{self.titular}")
        print(f"R${self.saldo:.2f}")
        print(f"{self.rendimento}")
        print(f"{self.rendimento}")
        print(f"{self.saquesMensais}")
    
    
    def novoMes(self):
        rendimentoMensal = (self.__rendimento * self._saldo) / 100
        self._saldo += rendimentoMensal
        self.__saquesMensais = 3
        return rendimentoMensal
    
    
    def saque(self,valorSaque):
        if self.__saquesMensais == 0:
            print("Limite de saques atindigos, operação cancelada") 
        else:
            if super().saque(valorSaque):
                self.__saquesMensais -= 1
    
    
    def saqueInput(self):
        if self.__saquesMensais == 0:
            print("Limite de saques atindigos, operação cancelada") 
        else:
            if super().saque():
                self.__saquesMensais -= 1
               
        
      
            
        
        
        
        
        
        