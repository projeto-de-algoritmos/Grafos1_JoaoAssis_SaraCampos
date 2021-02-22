
from collections import defaultdict

class Graph:
 
    def __init__(self):
 
        self.graph = defaultdict(list) ## Representamos o grafo como uma lista de adjacência
    def addVertice(self,u,v):
        self.graph[u].append(v)
 
    def BFS(self, inicio,fim):
 
        # Marcando todos os vertices como não visitados
        
        visitado = [False] * (max(self.graph) + 1)
        # Criamos uma variavel auxiliar fila para atravessar o grafo
        filaNos = []
 
        # Marcamos o no de origem como visitado e o colocamos na fila
        filaNos.append(inicio)
        visitado[inicio] = True
        try:
            while filaNos:
    
                # Após visitar um vertice, retiramos ele da fila
                noAtual = filaNos[0]
                inicio = filaNos.pop(0)
                print (inicio, end = " ")
                if(noAtual == fim): ##Se encontrarmos o vertice que procuramos, encerramos a busca
                    return True
                # Pegamos todos os vertices adjacentes do vertice visitado atualmente, e se ele ainda não tiver sido visitado o adcionamos a fila para podermos visitar os seus vertices adjacentes
                for i in self.graph[inicio]:
                    if visitado[i] == False:
                        filaNos.append(i)
                        visitado[i] = True
            return False
        except:
            return False
    
 

g = Graph()

direcionado = input("Deseja operar um grafo: 1)Direcionado2)Não direcionado") == '1'
while(True):
    
    print("Deseja: \n1)Adicionar mais um nó ao grafo\n2)Procurar um nó atraveś do BFS\n4)Fechar o programa")
    option = int(input("Digite a opção desejada"))
    if(option == 4):
        break
    if(option == 1):
        no1 = int(input("Digite o nó filho"))
        no2 = int(input("Digite o nó filho"))
        g.addVertice(no1,no2)
        if(input):
            g.addVertice(no2,no1)
    if(option == 2):
        inicio = int(input("Digite o nó de inicio da busca"))
        fim = int(input("Digite o nó de fim da busca"))
        if(g.BFS(inicio,fim)):
            print("Caminho encontrado!")
        else:
            print("Caminho não encontrado")
        

