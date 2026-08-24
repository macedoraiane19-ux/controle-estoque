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
    try:
        nome = input('Nome: ')
        categoria = input('Categoria: ')
        id_produto = estoque.gerar_id()
        quantidade = int(input('Quantidade: '))
        preco = float(input('Preço: '))

        if not nome.strip() or not categoria.strip():
            print('Nome e categoria são obrigatórios.')
            return

        if quantidade < 0 or preco < 0 :
            print('Quantidade  e Preço não podem ser negativos.')
            return


        produto = Produto(nome,categoria, id_produto, quantidade, preco)
        estoque.adicionar_produto(produto)
        print(f'ID gerado para o produto: {id_produto}')

    except ValueError:
        print('Quantidade e Preço devem ser números.')



def iniciar_estoque():
    while True:
        try:
         opcao = int(mostrar_menu())
        except ValueError:
            print('Digite apenas números.')
            continue

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

            try:
                id_produto = int(input('Digite o ID do produto:'))
                produto=estoque.buscar_produto(id_produto)
                if produto:
                 print(f'Nome= {produto.nome} | Categoria= {produto.categoria} | ID = {produto.id} | Quantidade:{produto.quantidade} | Preço= R${produto.preco:.2f}')

            except ValueError:
                print('ID deve ser um número.')   

      # Editar produto

        elif opcao == 4:

            try:
                id_produto = int(input('Digite o ID do produto:'))
                estoque.editar_produto(id_produto)

            except ValueError:
                print('ID deve ser um número.')
            
      # Remover produto

        elif opcao == 5:

            try:
                id_produto = int(input('Digite o ID do produto: '))
                estoque.remover_produto(id_produto)

            except ValueError:
                print('ID deve ser um número.')

      # sair do programa

        elif opcao == 0:
            print('Programa encerrado.')
            break

        else:
            print('Opção inválida.')

