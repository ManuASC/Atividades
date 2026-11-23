
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponivel = "Sim"

    def descricao(self):
        print("\n--- Descrição do Livro ---")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")
        print(f"Disponível: {self.disponivel}")

    def emprestar(self):
        if self.disponivel == "Sim":
            self.disponivel = "Não"
            print("Livro emprestado com sucesso!")
        else:
            print("Este livro já está emprestado.")

    def devolver(self):
        if self.disponivel == "Não":
            self.disponivel = "Sim"
            print("Livro devolvido com sucesso!")
        else:
            print("Este livro já está disponível.")

livros = [
    Livro("Black Clover", "Yuki Tabata", 192),
    Livro("Diário de uma Apotecária", "Natsu Hyuga", 178),
    Livro("Noragami", "Adachitoka", 192),
    Livro("Bungou Stray Dogs", "Kafka Asagiri", 192)
]

while True:
    print("\n===== BIBLIOTECA DE MANGÁS =====")
    print("1 - Ver livros")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- LIVROS DISPONÍVEIS ---")
        for i, livro in enumerate(livros):
            print(f"\n{i + 1} - {livro.titulo}")
            livro.descricao()

    elif opcao == "2":
        print("\nQual livro deseja emprestar?")

        for i, livro in enumerate(livros):
            print(f"{i + 1} - {livro.titulo} ({livro.disponivel})")

        escolha = int(input("Digite o número do livro: "))

        if 1 <= escolha <= len(livros):
            livros[escolha - 1].emprestar()
        else:
            print("Opção inválida!")

    elif opcao == "3":
        print("\nQual livro deseja devolver?")

        for i, livro in enumerate(livros):
            print(f"{i + 1} - {livro.titulo} ({livro.disponivel})")

        escolha = int(input("Digite o número do livro: "))

        if 1 <= escolha <= len(livros):
            livros[escolha - 1].devolver()
        else:
            print("Opção inválida!")

    elif opcao == "4":
        print("Obrigado por utilizar a biblioteca!")
        break

    else:
        print("Opção inválida! Tente novamente.")
