
from collections import defaultdict

class Graph:
 
    def __init__(self):
 
        self.graph = defaultdict(list) ## Representamos o grafo como uma lista de adjacência
    def addVertice(self,u,v):
        if(v in self.graph[u]):
            print("ja adicionado")
        else:
            self.graph[u].append(v)
 
    def printGrafoVisitado(self, nosVisitados,noAtual):
        
        for no in self.graph.keys():
            print(no,end= '**  'if adjacente == noAtual else '*: 'if nosVisitados[no] else ': ')
            for adjacente in self.graph[no]:
                print(adjacente, end=  '* ' if nosVisitados[adjacente] else ' ')
            print("\n")
    def BFS(self, inicio,fim):
        # Marcando todos os vertices como não visitados
        visitado = [False] * (max(self.graph) + 1)
        # Criamos uma variavel auxiliar fila para atravessar o grafo
        filaNos = []
        caminho = {}
        # Marcamos o no de origem como visitado e o colocamos na fila
        filaNos.append(inicio)

        print("Iniciando busca no grafo:")
        self.printGrafoVisitado(visitado,inicio)
        print("A partir do no " + str(inicio))
        print("\n")
        try:
            visitado[inicio] = True
            self.printGrafoVisitado(visitado,inicio)
            print("*)Nos já visitados\n**)Nó atual")
            
            while filaNos:
                # Após visitar um vertice, retiramos ele da fila
                noAtual = filaNos[0]
                inicio = filaNos.pop(0)
                print('\n')
                print("Visitando os nos adjacentes ao no " + str(noAtual))
                # Pegamos todos os vertices adjacentes do vertice visitado atualmente, e se ele ainda não tiver sido visitado o adcionamos a fila para podermos visitar os seus vertices adjacentes
                for i in self.graph[inicio]:
                    print("Visitamos o no " + str(i) + " adjacente ao no " + str(inicio))
                    
                    if visitado[i] == False:
                        print("Marcamos o no " + str(i) + " como visitado e o adicionamos a fila para visitar seus adjactentes")
                        caminho[i] = inicio
                        if(i == fim):
                            return caminho
                        filaNos.append(i)
                        print("Proximos nos com adjacentes a serem visitados: " + str(filaNos))
                        visitado[i] = True
                        
                        self.printGrafoVisitado(visitado,i)
                        print("*)Nos já visitados\n**)Nó atual")
                    else:
                        print("No "+str(i) +" já visitado (Não precisamos visitar seus adjacentes novamente)")
                print("Todos os nos adjacentes do no " + str(inicio)+ " foram visitados")
            return []
        except Exception as e:
            print(e)
            return []
    
 

g = Graph()

naoDirecionado = input("Deseja operar um grafo: 1)Direcionado2)Não direcionado") == '2'
while(True):
    
    print("Deseja: \n1)Adicionar mais um nó ao grafo\n2)Procurar um nó atraveś do BFS\n4)Fechar o programa")
    option = int(input("Digite a opção desejada"))
    if(option == 4):
        break
    if(option == 1):
        no1 = int(input("Digite o nó pai"))
        no2 = int(input("Digite o nó filho"))
        g.addVertice(no1,no2)
        if(naoDirecionado):
            g.addVertice(no2,no1)
    if(option == 2):
        inicio = int(input("Digite o nó de inicio da busca"))
        fim = int(input("Digite o nó de fim da busca"))
        caminhoBusca = g.BFS(inicio,fim)
        if(len(caminhoBusca)):
            print("Caminho encontrado!")
            noCaminho = fim
            while(noCaminho!=inicio):
                print(str(noCaminho) + ' <-',end='')
                noCaminho = caminhoBusca[noCaminho]
        else:
            print("Caminho não encontrado")
        

