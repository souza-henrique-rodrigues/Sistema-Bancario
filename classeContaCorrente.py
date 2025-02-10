
from classeContaBancaria import ContaBancaria


class ContaCorrente(ContaBancaria):
    def __init__(self, titular, banco, numeroConta, saldo, senha,taxaMensal: float):
        super().__init__(titular, banco, numeroConta, saldo, senha)
        self.__taxaMensal = float(taxaMensal)
    
    
    @property
    def taxaMensal(self):
        return f"R${self.__taxaMensal:.2f}"
    
    @taxaMensal.setter
    def taxaMensal(self,taxa):
        if isinstance(taxa, float) and taxa > 0:
            self.__taxaMensal = taxa
            
    
    def info(self):
        print(f"{self.banco}")
        print(f"{self.numeroConta}")
        print(f"{self.titular}")
        print(f"R${self.saldo:.2f}")
        print(f"{self.taxaMensal}")
    
    def novoMes(self):
        self._saldo -= self.__taxaMensal
        
        
         

    