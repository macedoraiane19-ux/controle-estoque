from produtos import Produto

class Estoque:
    def __init__(self):
        self.produtos = {}


# Criando ID automáticamente.

    def gerar_id(self):
        if not self.produtos:
            return 1

        return max(self.produtos.keys()) + 1


# Adiciona um produto no estoque:

    def adicionar_produto(self, produto):
        if produto.id in self.produtos:
            print('Já existe um produto com esse ID.')
            return
        
        self.produtos[produto.id] = produto
        print(f'{produto.nome} foi adicionado no estoque.')

# Mostra o que tem no estoque:

    def mostrar_estoque(self):
        if not self.produtos:
            print('O estoque está vazio.')
            return

        print('Produtos:')
        for produto in self.produtos.values():
            print(f'Nome= {produto.nome} | Categoria= {produto.categoria} | ID = {produto.id} | Quantidade:{produto.quantidade} | Preço= R${produto.preco:.2f}')

# Remove um produto do estoque:

    def remover_produto(self, id_produto):
        if id_produto not in self.produtos:
            print('Produto não encontrado.')
            return

        produto = self.produtos[id_produto]

        while True:

            confirmacao = input( f'Tem certeza que deseja remover "{produto.id}-{produto.nome}"? (s/n): ').lower().strip()

            if confirmacao == 's':
             break

            if confirmacao == 'n':
                print('Operação Cancelada.')
                return

            print('Digite apenas "s" para SIM e "n" para NÃO.')

        del self.produtos[id_produto]
        print(f'O {produto.nome} foi removido.')
    

# Editar um produto no estoque

    def editar_produto(self, id_produto):
        if id_produto not in self.produtos:
            print('Produto não encontrado.')
            return

        
        produto = self.produtos[id_produto]
        print(f'Editando produto:{produto.id}{produto.nome}')

        try:

            novo_nome = input('Novo nome: ')
            novo_preco= float(input('Novo preço: '))
            nova_categoria= input('Nova categoria: ')
            nova_quantidade= int(input('Nova quantidade: '))

        except ValueError:
            print('Preço e Quantidade devem ser números.')
            return

        if not novo_nome.strip() or not nova_categoria.strip():
            print('Nome e categoria são obrigatórios.')
            return

        if nova_quantidade < 0 or novo_preco < 0:
            print('Quantidade e Preço não podem ser negativos.')
            return


        produto.nome = novo_nome
        produto.preco = novo_preco
        produto.categoria = nova_categoria
        produto.quantidade = nova_quantidade
        print('Produto atualizado com sucesso.')

# Buscar um produto.

    def buscar_produto(self, id_produto):
        if id_produto not in self.produtos:
           print('Produto não encontrado.')
           return
        
        produto = self.produtos[id_produto]
        return produto

    

