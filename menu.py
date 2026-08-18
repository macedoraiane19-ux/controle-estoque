from produtos import Produto
from estoque import Estoque 

estoque = Estoque()

def mostrar_menu():
    print('='*10,'CONTROLE DE ESTOQUE','='*10)
    print('[1] Adicionar produto')
    print('[2] Mostrar estoque')
    print('[3] Buscar produto ')
    print('[4] Editar produto')
    print('[5] Remover produto')
    print('[0] Sair')

    return input('Escolha uma opção: ')

def adicionando_produto():
    nome = input('Nome: ')
    categoria = input('Categoria: ')
    id_produto = int(input('ID: '))
    quantidade = int(input('Quantidade: '))
    preco = float(input('Preço: '))

    produto = Produto(nome,categoria, id_produto, quantidade, preco)
    estoque.adicionar_produto(produto)



def iniciar_estoque():
    while True:
        opcao = int(mostrar_menu())
      # Adicionar Produto
        if opcao == 1:
            print('Adicionar produto:')
            adicionando_produto()
      # Mostrar estoque
        elif opcao == 2:
            print('Mostrando Estoque')
            estoque.mostrar_estoque()
      # Buscar produto
        elif opcao == 3:
            id_produto = int(input('Digite o ID do produto:'))
            produto=estoque.buscar_produto(id_produto)
            if produto:
                print(f'Nome= {produto.nome} | Categoria= {produto.categoria} | ID = {produto.id} | Quantidade:{produto.quantidade} | Preço= R${produto.preco:.2f}')
      # Editar produto
        elif opcao == 4:
            id_produto = int(input('Digite o ID do produto:'))
            estoque.editar_produto(id_produto)
            
      # Remover produto
        elif opcao == 5:
            id_produto = int(input('Digite o ID do produto: '))
            estoque.remover_produto(id_produto)
      # sair do programa
        elif opcao == 0:
            print('Programa encerrado.')
            break

        else:
            print('Opção inválida.')

