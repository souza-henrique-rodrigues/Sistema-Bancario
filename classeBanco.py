class Banco:
    def __init__(self,nome: str,cnpj:str ,numeroBanco: int):
        self.__nome = str(nome)
        self.__cnpj = str(cnpj)
        self.__numeroBanco = int(numeroBanco)
        self.__contasBancarias = []
    
    
    @classmethod
    def criarBancoClass(cls):
       
        nome = input("Informe o nome do banco: ")
        cnpj = input("Informe o CNPJ do banco (apenas números, 14 dígitos): ")
        numeroBanco = int(input("Informe o número do banco: "))
        return cls(nome, cnpj, numeroBanco)
    
    
    @property
    def nome(self):
        return f"{self.__nome}"
    
    @nome.setter
    def nome(self,novoNome):
        if isinstance(novoNome, str) and len(novoNome) >= 3 and  novoNome.isalpha():
            self.__nome = novoNome
        else:
            raise ValueError("Erro ao inserir nome, campo deve conter no minimo 3 letras e somente caracteres.")
    
    @property
    def cnpj(self):
        return f"{self.__cnpj}"
    
    @cnpj.setter
    def cnpj(self,novoCnpj):
        if isinstance(novoCnpj, str) and len(novoCnpj) == 14 and novoCnpj.isdigit():
            self.__cnpj = novoCnpj
        else:
            raise ValueError("Erro ao inserir cnpj, campo deve conter 14 digitos, inserido sem barra, hifen e espaco entre cada digito")
    
    @property
    def numeroBanco(self):
        return f"{self.numeroBanco}"
    
    @numeroBanco.setter
    def numeroBanco(self,numeroBanco):
        if isinstance(numeroBanco, int):
            self.__numeroBanco = numeroBanco
        else:
            raise ValueError("Erro ao inserir campo numero Banco, campo deve conter apenas numeros inteiros.")
    
    
    def info(self):
        print(f"{self.__nome}")
        print(f"{self.__cnpj}")
        print(f"{self.__numeroBanco}")


    def infoContas(self):
        for conta in self.__contasBancarias:
            conta.info()
    

    def criarConta(self,listaPessoas):
        from classeContaCorrente import ContaCorrente
        from classeContaPoupanca import ContaPoupanca
        cpf = input("Informe o cpf da conta para cadastro: ").lower()
        
        for pessoa in listaPessoas:
            if pessoa.cpf == cpf:
                tipoConta = input("opção: [1] conta poupanca | opção: [2] conta corrente ").lower()
                if tipoConta == "1":
                    saldo = float(input("Informe o saldo a ser adiconado a conta: "))
                    senha = input("Crie uma senha para conta: ")
                    rendimento= float(input(("Rendimento mensal R$: ")))
                    
                    contaPoupanca = ContaPoupanca(pessoa,self,self.__numeroBanco,saldo,senha,rendimento,)
                    self.__contasBancarias.append(contaPoupanca)
                
                elif tipoConta == "2":
                    saldo = float(input("Informe o saldo a ser adiconado a conta: "))
                    senha = input("Crie uma senha para conta: ")
                    taxaMensal = float(input("Taxa mensal para manutenção conta R$: "))
                    
                    contaCorrente = ContaCorrente(pessoa,self,self.__numeroBanco,saldo,senha,taxaMensal)
                    self.__contasBancarias.append(contaCorrente)
                    
            else:
                print("cpf não encontrado")     
        
    
    def fecharConta(self):
        numero = input("Informe o numero da conta: ")
        for conta in self.__contasBancarias:
            if conta.numeroConta == numero:
                self.__contasBancarias.remove(conta)
        