
from classeBanco import Banco
from classePessoa import Pessoa

class Main:
    
    listaPessoas = []
    listaBancos = []
    listaContas = []
            
    def cadastrarPessoa(self):
        nome = input("Informe o primeiro nome: ")
        sobrenome = input("Informe o sobrenome: ")
        idade = int(input("Informe a idade: "))
        cpf = input("Informe o cpf: ")
        
        pessoa = Pessoa(nome,sobrenome,idade,cpf)
        self.listaPessoas.append(pessoa)
        
        
    def cadastrarBanco(self):
        from classeBanco import Banco
        nome = input("Informe o nome do banco: ")
        cnpj = input("Informe o cnpj: ")
        numero = int(input("Informe o numero do banco: "))
        
        banco = Banco(nome,cnpj,numero)
        self.listaBancos.append(banco)
    
    
    def cadastrarConta(self):
        cnpj = input("Informe o cnpj do banco que sera criada conta: ")
        
        for banco in self.listaBancos:
            if banco.cnpj == cnpj:
                banco.criarConta(self.listaPessoas)
    
    def informacoesPessoa(self):
        cpf = input("Informe o cpf da pessoa : ")
        for pessoa in self.listaPessoas:
            if pessoa.cpf == cpf:
                pessoa.info()                
        

if __name__ == "__main__":
    
    programa = Main()
    run = True
    while run:
        
        pergunta = input("\n1: Cadastrar pessoa\n2: Cadastrar banco\n3: Cadastrar conta\n4: Informações pessoa\n0: Finalizar programa")
        
        
        match pergunta:
            
            case "1":
                programa.cadastrarPessoa()
                
            case "2":
                programa.cadastrarBanco()
            
            case "3":
                programa.cadastrarConta()   
            
            case "4":
                programa.informacoesPessoa()           
                
            
            case "0":
                print("Programa finalizado")
                run = False
                





















