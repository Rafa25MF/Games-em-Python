import random

pokemons = {
    "Charmander": {"vida": 30, "dano": 4, "defesa": 3},
    "Squirtle": {"vida": 30, "dano": 4, "defesa": 3},
    "Bulbasaur": {"vida": 30, "dano": 4, "defesa": 3}
}


def menu():
    escolha = int(input("\nOlá treinador, escolha seu pokémon!"
                        "\n[ 1 ] Charmander"
                        "\n[ 2 ] Squirtle"
                        "\n[ 3 ] Bulbasaur"
                        "\nQual será a sua escolha? "))
    nomes = ["Charmander", "Squirtle", "Bulbasaur"]
    jogador = nomes[escolha - 1]
    inimigo = random.choice(nomes)
    print(f'\nVocê escolheu: {jogador}')
    print(f'O oponente escolheu: {inimigo}')
    batalha(jogador, inimigo)



def imagens():
    print('\033[33m--------------------------------------------------------------')
    print('  |                                                         |')
    print('  |                     BATALHA POKÉMON                     |')
    print('  |                                                         |')
    print('--------------------------------------------------------------')
    print("\n⠀⠀⠀⣀⠔⠒⠒⠂⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠐⠒⠒⠂⠠⡀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠈⡖⡤⠄⠀")
    print("⠀⠀⢰⢅⠀⠀⢀⣤⢄⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠀⠀⡠⢠⠂⠀⠀⠀⠡⡀⠀   ⠀⠀⢀⡀⠀⠀⠀⡐⠁⠀⠀⠠⠐⠂⠀⠁⠀⠀⠀⠀")
    print("⠀⠀⣾⡆⠀⠀⠀⢸⠼⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⢰⣷⣾⠀⠀⠀⠀⠀⡇⠀   ⠀⠰⡁⠐⢉⣉⣭⡍⠁⠂⠉⠘⡀⠀⠀⠀⠀⠂⠡⠀")
    print("⠀⢀⢗⠂⠀⠀⡀⠈⢉⠅⠇⠀⠀⠀⠀⠀⠀⢠⣄⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠜⢨⠢⠔⡀⠀⠠⠘⠛⠛⠀⠀⠀⠀⢸⡇⠀   ⢀⣊⠀⡄⠻⠿⠋⠀⠀⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⢀")
    print("⠀⠈⠢⣓⠔⣲⠖⡫⠊⡘⠀⠀⠀⠀⠀⠀⠲⡟⠙⡆   ⠀⠀⠀⢀⣀⣀⠀⠀⠀⠰⠀⠀⠀⠀⠡⡀⠀⠈⠀⠒⠂⠄⡀⢀⠀⡀⠀   ⡎⣾⠀⠁⣴⡆⠀⠡⢺⣿⣆⠀⢠⢱⣄⠀⠀⠀⠀⠈")
    print("⠀⢀⢀⠠⠘⣇⠖⢄⠀⠉⠐⠠⢄⣀⡀⠀⠜⠀⠀⣁   ⠀⡴⠊⠀⠀⠀⠉⢆⠀⡔⢣⠀⠀⠀⠀⠐⡤⣀⠀⠀⠀⠀⠀⣀⠄⠀⠀   ⡑⠟⠀⠀⠀⠀⠀⢀⣸⡿⠟⠀⠀⠈⢿⣿⡦⡀⠀⡰")
    print("⠘⣏⣀⣀⣀⠃⠀⠀⠑⣀⣀⣀⣰⠼⠇⠈⠄⠀⠈⡻   ⢸⠀⠀⠀⢠⠀⠀⠈⣼⠀⠀⠣⠀⠀⠀⡰⡀⠀⠉⠀⠀⠰⠉⠀⠁⠠⢄   ⠙⠔⠦⣤⣥⣤⣤⣤⡤⠆⠀⠀⠀⠀⢀⢀⠀⠈⠎⠀")
    print("⠀⠁⠀⠀⢰⠀⠀⠀⠀⠠⠀⠡⡀⠀⠀⠀⠈⡖⠚⠀   ⢰⠀⠀⠀⠀⠇⠀⢀⢿⠀⢀⠇⡐⠀⠈⠀⠈⠐⠠⠤⠤⠤⠀⠀⠀⠀⢨   ⠀⠀⠈⣰⡋⢉⠉⠁⠒⠂⢇⢠⡆⠀⠸⢴⣿⠀⠘⠀")
    print("⠀⠀⠀⡠⠘⠀⠀⠀⠀⢀⠆⠀⠐⡀⠀⡠⠊⣠⠀⠀   ⠀⢓⠤⠤⠊⠀⠀⢸⠀⠣⠀⡰⠁⠀⠀⡀⠀⠀⠀⠸⠀⢰⠁⠐⠂⠈⠁   ⠀⠀⠘⡿⠃⠀⠨⠒⢆⣸⣿⠁⠀⡠⡇⠈⠋⠀⠰⠀")
    print("⠀⠀⢐⠀⠀⠁⡀⠀⠀⢀⠀⠀⠀⢨⠀⡠⡴⠂⠀⠀   ⠀⠀⠑⢀⠀⠀⠀⠈⣄⠖⠉⠑⢄⠠⠊⠀⠢⢄⣠⣃⣀⡆⠀⠀⠀⠀⠀   ⠀⠀⠀⠛⠒⠒⠁⠀⠈⠷⡤⠤⠐⠀⠘⠒⠒⠖⠁⠀")
    print("⠀⢀⣨⣤⠀⠀⠐⠃⠐⠚⠢⠀⠀⠈⠑⠊⠀⠀⠀⠀   ⠀⠀⠀⠀⠑⠠⢀⣀⠎⠀⠀⠀⠈⡄⠀⠀⠀⢠⢃⠠⠃⠐⡀⠀⠀⠀⠀   ")
    print("⠀⠘⠓⠋⠉⠁⠀⠀⠀⠀⠀⠓⢶⡾⠗⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⢀⠯⠉⠤⢴⡃⠁⠀⠀⠀⡇⠀⠀⠀⠀   ")
    print("                        ⠀⠀ ⠀⠀⠰⡁⠀⠀⠀⠠⠂⠀⠀⠀⠀⠑⢄⠀⠀⢀⠲⠁⠀⠀⠀")
    print("                              ⠘⠒⠑⠔⠁⠀⠀⠀⠀⠀⠀⠀⠁⠉⠀⠀⠀⠀⠀⠀")



def batalha(jogador, inimigo):
    vida_j = 30
    vida_i = 30
    dano_j = 4
    dano_i = 4
    defesa_j = 3

    while vida_j > 0 and vida_i > 0:
        print("\n=== BATALHA ===")
        print(f"Sua vida: {vida_j} | Vida do inimigo: {vida_i}")
        print("[1] Atacar")
        print("[2] Defender")
        print("[3] Fugir")
        açao = int(input("O que você quer fazer? "))
        

        if açao == 1:
            vida_i -= dano_j
            vida_j -= dano_i
            print(f'Você atacou o {inimigo} causando {dano_j} de dano!'
                  f'\n{inimigo} atacou causando {dano_i} de dano')


        elif açao == 2:
            dano_recebido = max(dano_i - defesa_j, 0)
            vida_j -= dano_recebido
            print(f"Golpe defendido, você tomou {dano_recebido} de dano.")


        elif açao == 3:
            print("Você fugiu da batalha. Fim de jogo.")
            break


        else:
            print("Opção inválida. Tente de novo.")


        if vida_i <= 0:
            print('\n===========================================')
            print(f"Você venceu! O {inimigo} foi derrotado!")
            print('===========================================')
            print('')
            break


        if vida_j <= 0:
            print('\n===========================================')
            print(f"Você perdeu! O {inimigo} venceu a batalha.")
            print('===========================================')
            print('')
            break

imagens()
menu()
batalha()





