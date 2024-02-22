#classes e objetos
'''
class Livro:
   def __init__(self, titulo, autor, ano) :
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

meuLivro = Livro("Harry Potter", "JK Rowling", 2005)

print(meuLivro.titulo)

#metodos

class Livro:
   def __init__(self, titulo, autor, ano) :
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

   def __str__(self):
       return f"{self.titulo} foi escrito por {self.autor} em {self.ano}"
   
meuLivro = Livro("Harry Potter", "JK Rowling", 2005)

print(meuLivro)
'''

#metodos de instancia
'''
class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor 
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 5

    def frear(self):
        self.velocidade -= 5

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano} {self.cor} {self.velocidade}km/h"
    
meuCarro = Carro("Ford", "Fiesta", 2019, "Preto")

print(meuCarro)
meuCarro.acelerar()
print(meuCarro)
meuCarro.acelerar()
print(meuCarro)
meuCarro.acelerar()
print(meuCarro)
meuCarro.acelerar()
print(meuCarro)
meuCarro.acelerar()
print(meuCarro)

'''        
'''
class Fruta:
    def __init__(self, nome, cor, sabor, peso=0):
        self.nome = nome
        self.cor = cor
        self.sabor = sabor
        self.peso = peso

    def __str__(self):
        return f"{self.nome} {self.cor} {self.sabor} {self.peso}kg"
    
    def aumentaPeso(self, peso):
        self.peso += peso

    def diminuiPeso(self, peso):
        self.peso -= peso
    
minhaFruta1 = Fruta("Maçã", "Vermelha", "Doce")
minhaFruta2 = Fruta("Banana", "Amarela", "Doce")
minhaFruta3 = Fruta("Laranja", "Laranja", "Ácida")

print(minhaFruta1)
print(minhaFruta2)
print(minhaFruta3)

minhaFruta1.aumentaPeso(0.5)
minhaFruta2.aumentaPeso(0.3)
minhaFruta3.aumentaPeso(0.7)

print(minhaFruta1)
print(minhaFruta2)
print(minhaFruta3)

'''
'''
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.acordado = False
        self.comendo = False
        self.dirigindo = False

    def __str__(self):
        return f"{self.nome} está acordado: {self.acordado}, comendo: {self.comendo}, dirigindo: {self.dirigindo}"


    def acordar(self):
        self.acordado = True
        if self.acordado:
            print(f"{self.nome} está acordado")
        else:
            print(f"{self.nome} está dormindo")

    def dormir(self):
        self.acordado = False
        if self.acordado:
            print(f"{self.nome} está acordado")
        else:
            print(f"{self.nome} está dormindo")

    def comer(self):
        self.comendo = True
        if self.comendo:
            print(f"{self.nome} está comendo")
        else:
            print(f"{self.nome} não está comendo")

    def pararDeComer(self):
        self.comendo = False
        if self.comendo:
            print(f"{self.nome} está comendo")
        else:
            print(f"{self.nome} não está comendo")

    def dirigir(self):
        self.dirigindo = True
        if self.dirigindo:
            print(f"{self.nome} está dirigindo")
        else:
            print(f"{self.nome} não está dirigindo")

    def pararDeDirigir(self):
        self.dirigindo = False
        if self.dirigindo:
            print(f"{self.nome} está dirigindo")
        else:
            print(f"{self.nome} não está dirigindo")

    

pessoa1 = Pessoa("João")
print(pessoa1)
pessoa1.acordar()
print(pessoa1)
pessoa1.comer()
print(pessoa1)
pessoa1.pararDeComer()
print(pessoa1)
pessoa1.dirigir()
print(pessoa1)
pessoa1.pararDeDirigir()
print(pessoa1)
pessoa1.dormir()
print(pessoa1)

'''
'''
#criar um programa que manipula frases

class Frase:
    def __init__(self, frase):
        self.frase = frase

    def __str__(self):  
        return f"{self.frase}"
    
    def maiuscula(self):
        return self.frase.upper()
    
    def minuscula(self):
        return self.frase.lower()
    
    def inverte(self):
        return self.frase[::-1]
    
    def quantidadeDeLetras(self):
        return len(self.frase)
    
    def quantidadeDePalavras(self):
        return len(self.frase.split())
    
    def quantidadeDeVogais(self):
        vogais = "aeiou"
        cont = 0
        for letra in self.frase:
            if letra in vogais:
                cont += 1
        return cont
    
    def quantidadeDeConsoantes(self):
        consoantes = "bcdfghjklmnpqrstvwxyz"
        cont = 0
        for letra in self.frase:
            if letra in consoantes:
                cont += 1
        return cont
    
    def contemPalavra(self, palavra):
        return palavra in self.frase
    
frase = Frase("O rato roeu a roupa do rei de roma")

while True:
        print("1 - Maiuscula")
        print("2 - Minuscula")
        print("3 - Inverte")
        print("4 - Quantidade de letras")
        print("5 - Quantidade de palavras")
        print("6 - Quantidade de vogais")
        print("7 - Quantidade de consoantes")
        print("8 - Contem palavra")
        print("9 - Sair")
        opcao = int(input("Digite uma opção: "))
        if opcao == 1:
            print(frase.maiuscula())
        elif opcao == 2:
            print(frase.minuscula())
        elif opcao == 3:
            print(frase.inverte())
        elif opcao == 4:
            print(frase.quantidadeDeLetras())
        elif opcao == 5:
            print(frase.quantidadeDePalavras())
        elif opcao == 6:
            print(frase.quantidadeDeVogais())
        elif opcao == 7:
            print(frase.quantidadeDeConsoantes())
        elif opcao == 8:
            palavra = input("Digite a palavra: ")
            print(frase.contemPalavra(palavra))
        elif opcao == 9:
            break
        else:
            print("Opção inválida")
'''
'''
class Evento:
    def __init__(self, lugaresDisponiveis = 10):
        self.lugaresDisponiveis = lugaresDisponiveis
        self.lugaresOcupados = 0

    def __str__(self):
        return f"Lugares disponíveis: {self.lugaresDisponiveis}, lugares ocupados: {self.lugaresOcupados}"
    
    def reservarLugar(self, lugares):
        if self.lugaresDisponiveis >= lugares:
            self.lugaresDisponiveis -= lugares
            self.lugaresOcupados += lugares
        elif self.lugaresDisponiveis < lugares:
            print("Não há lugares disponíveis")

    def cancelarReserva(self, lugares):
        if self.lugaresOcupados >= lugares:
            self.lugaresDisponiveis += lugares
            self.lugaresOcupados -= lugares
        elif self.lugaresOcupados == 0:
            print("Não há lugares ocupados")

evento = Evento()
print(evento)
evento.reservarLugar(5)
print(evento)
evento.reservarLugar(5)
print(evento)
evento.reservarLugar(5)
print(evento)
evento.cancelarReserva(5)
print(evento)
evento.cancelarReserva(5)
print(evento)
evento.cancelarReserva(5)
print(evento)
'''

'''
#manipulando listas

class Lista:
    def __init__(self, lista):
        self.lista = lista

    def __str__(self):
        return f"{self.lista}"
    
    def adicionarElemento(self, elemento):
        self.lista.append(elemento)

    def removerElemento(self, elemento):
        if elemento in self.lista:
            self.lista.remove(elemento)
        else:
            print("Elemento não encontrado")

    def buscarMaior(self):
        return max(self.lista)
    
    def buscarMenor(self):
        return min(self.lista)
    
    def calcularMedia(self):
        return sum(self.lista) / len(self.lista)

    def ordenarLista(self):
        self.lista.sort()

    def inverterLista(self):
        self.lista.reverse()

    def limparLista(self):
        self.lista.clear()

lista = Lista([2, 1, 3, 5, 4])
print(lista)
lista.adicionarElemento(6)
print(lista)
lista.removerElemento(6)
print(lista)
print(lista.buscarMaior())
print(lista.buscarMenor())
print(lista.calcularMedia())
lista.ordenarLista()
print(lista)
lista.inverterLista()
print(lista)
lista.limparLista()
print(lista)
'''

#encapsulamento
'''
__nome = "João" #privado
_nome = "João" #protegido
nome = "João" #público
'''

#getters e setters
'''
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome

    def getPreco(self):
        return self.__preco
    
    def setPreco(self, preco):
        self.__preco = preco

    def __str__(self):
        return f"{self.__nome} R${self.__preco}"
    
produto = Produto("Camisa", 50)
print(produto)
produto.setNome("Calça")
print(produto.getNome())
produto.setPreco(100)
print(produto.getPreco())
print(produto)
'''

'''
class Pet:
    def __init__(self, nome, idade, peso):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso

    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome

    def getIdade(self):
        return self.__idade
    
    def setIdade(self, idade):
        self.__idade = idade

    def getPeso(self):
        return self.__peso
    
    def setPeso(self, peso):
        self.__peso = peso

    def exibirPet(self):
        print(f"{self.__nome} {self.__idade} anos {self.__peso}kg")
        
    
def mostrarMenu():
    print("1 - Cadastrar pet")
    print("2 - Exibir pet")
    print("3 - Sair")
    opcao = int(input("Digite uma opção: "))

    return opcao

def main():

    pet = Pet("", 0, 0)

    while True:
        opcao = mostrarMenu()
        if opcao == 1:
            nome = input("Digite o nome do pet: ")
            pet.setNome(nome)
            idade = int(input("Digite a idade do pet: "))
            pet.setIdade(idade)
            peso = float(input("Digite o peso do pet: "))
            pet.setPeso(peso)
        elif opcao == 2:
            pet.exibirPet()
        elif opcao == 3:
            break
        else:
            print("Opção inválida")


main()
'''
'''
class Termometro:
    def __innit__(self, temperatura):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, temperatura):
        if temperatura > 100 or temperatura < -100:
            print("Temperatura inválida")
        else:
            self.__temperatura = temperatura

    def __str__(self):
        return f"{self.__temperatura}°C"
    
def mostrarMenu():
    print("1 - Alterar temperatura")
    print("2 - Exibir temperatura")
    print("3 - Sair")
    opcao = int(input("Digite uma opção: "))

    return opcao

def main():
    
        termometro = Termometro()
    
        while True:
            opcao = mostrarMenu()
            if opcao == 1:
                temperatura = float(input("Digite a temperatura: "))
                termometro.temperatura = temperatura
            elif opcao == 2:
                print(termometro)
            elif opcao == 3:
                break
            else:
                print("Opção inválida")

main()

'''
'''
class Animal :
    def fazerSom(self):
        print("animal faz um som")
        
    
class Cachorro(Animal):
    def latir(self):
        print("au au au au")

class Gato(Animal):
    def miar(self):
        print("miau miau miau")


cachorro = Cachorro()
cachorro.fazerSom()
cachorro.latir()

gato = Gato()
gato.fazerSom()
gato.miar()

'''
'''
class Mamifero:
    def __init__(self):
        print("sou mamífero")

class Voador:
    def __init__(self):
        print("sou voador")
    def voar(self):
        print("voando")

class Nadador:
    def __init__(self):
        print("sou nadador")
    def nadar(self):
        print("nadando")

class Morcego(Mamifero, Voador):
    def __init__(self):
        Mamifero.__init__(self)
        Voador.__init__(self)
        print("sou morcego")

class Baleia(Mamifero, Nadador):
    def __init__(self):
        Mamifero.__init__(self)
        Nadador.__init__(self)
        print("sou baleia")

morcego = Morcego()
baleia = Baleia()

morcego.voar()
baleia.nadar()
'''
'''
class Animal:
    def som(self):
        print("animal faz um som")

class Cachorro(Animal):
    def som(self):
        super().som()
        print("au au au")

#animal = Animal()
#animal.som()
cachorro = Cachorro()
cachorro.som()
'''
'''
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self):
        print (f"{self.marca} {self.modelo} {self.ano}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor):
        super().__init__(marca, modelo, ano)
        self.cor = cor

    def exibir_info(self):
        super().exibir_info()
        print(f"Cor: {self.cor}")

#veiculo = Veiculo("Ford", "Fiesta", 2019)
#veiculo.exibir_info()
carro = Carro("Ford", "Fiesta", 2019, "Preto")
carro.exibir_info()
'''

#sobrecarga
'''
class Impressora:
    def imprimir(self, dado):
        if isinstance(dado, str):
            print(f"Imprimindo string: {dado}")
        elif isinstance(dado, list):
            print("Imprimindo lista")
            for i in dado:
                print(i)
        elif isinstance(dado, dict):
            print("Imprimindo dicionário")
            for k, v in dado.items():
                print(f"{k}: {v}")
        else:
            print("Tipo de dado não suportado")

impressora = Impressora()
impressora.imprimir("Olá mundo")
impressora.imprimir([1, 2, 3, 4, 5])
impressora.imprimir({"nome": "João", "idade": 30})

'''

class Estudante:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade
    
    def set_idade(self, idade):
        self.idade = idade

    def get_nota(self):
        return self.nota
    
    def set_nota(self, nota):
        self.nota = nota

    def exibir_estudante(self):
        print(f"{self.nome} {self.idade} anos {self.nota} pontos")

def menu():
    print("1 - Cadastrar estudante")
    print("2 - Exibir estudante")
    print("3 - Alterar cadastro")
    print("4 - Sair")
    opcao = int(input("Digite uma opção: "))

    return opcao

def main():

    lista_estudantes = []

    while True:

        opcao = menu()

        if opcao == 1:
            nome = input("Digite o nome do estudante: ")
            idade = int(input("Digite a idade do estudante: "))
            nota = float(input("Digite a nota do estudante: "))
            estudante = Estudante(nome, idade, nota)
            lista_estudantes.append(estudante)
        elif opcao == 2:
            for estudante in lista_estudantes:
                estudante.exibir_estudante()
        elif opcao == 3:
            nome = input("Digite o nome do estudante: ")
            for estudante in lista_estudantes:
                if estudante.get_nome() == nome:
                    nova_nota = float(input("Digite a nova nota: "))
                    estudante.set_nota(nova_nota)
                else:
                    print("Estudante não encontrado")
        elif opcao == 4:
            break
        else:
            print("Opção inválida")

main()
