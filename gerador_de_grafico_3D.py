# classe criada para fazer as operações com gráficos 3D
class grafico_3D:

# função init
    def __init__(self, comeca_x, comeca_y, termina_x, termina_y):

        self.comeca_x = comeca_x
        self.comeca_y = comeca_y
        self.termina_x = termina_x
        self.termina_y = termina_y

# função para inserir e mostrar os limites desse gráfico
    def inserir_e_mostrar_limite_grafico_3D(self):

        import numpy as np
        import matplotlib.pyplot as plot
        from time import sleep

        comeca_x = float(input("Digite o ponto de partida de x: "))
        comeca_y = float(input("Digite o ponto de partida de y: "))
        termina_x = float(input("Digite o ponto de término de x: "))
        termina_y = float(input("Digite o ponto de término de y: "))
        print("Baseado nos limites gerados, seu gráfico é: ")

        sleep(2)

        x, y = np.mgrid[comeca_x:termina_x, comeca_y:termina_y]
        z = x * y + 6 * 10

        fig = plot.figure(figsize=(7, 7))
        ax = fig.add_subplot(projection="3d")
        ax.plot_surface(x, y, z)

        plot.show()

        sleep(5)

# opçoões de menu com tratamento de erro e condicionais aplicadas
    def opcoes_limite_grafico(self):

        from time import sleep

        try:

            print("Olá, esse é um programa de inserir limites em um gráfico 3D.")

            sleep(3)

            print("Ele é outro teste e é facilmente editável, em sua base de códigos, também.")

            sleep(3)

            print("Se quiser, você pode editar o valor recebido por z, para mostrar gráficos diferentes.")

            sleep(3)

            while True:

                print("As suas opções são:")

                sleep(2)

                print("[ 1 ] Inserir os limites do gráfico")

                sleep(2)

                print("[ 2 ] Sair")

                sleep(2)

                opcao = int(input("Digite sua opção: "))

                if opcao == 1:

                    comeca_x = 0
                    comeca_y = 0
                    termina_x = 0
                    termina_y = 0

                    grafico_recebedor = grafico_3D(comeca_x, comeca_y, termina_x, termina_y)
                    grafico_recebedor.inserir_e_mostrar_limite_grafico_3D()

                elif opcao == 2:

                    print("Tudo bem, entendo que tenha encerrado o programa.")

                    sleep(2)

                    print("Tenha um bom dia!")

                    sleep(2)

                    break

                else:

                    print("Sinto muito mas a sua opção foi inválida. Tente novamente!")

                    sleep(3)

        except ValueError:

            print("A opção inserida não tem um valor válido. Tente novamente!")

            sleep(2)

        except KeyboardInterrupt:

            print("O programa foi encerrado antes da hora, pelo usuário!")

            sleep(2)

            print("Até mais!")

            sleep(2)

# atribuição dos valores para a função init chamá-los
comeca_x = 0
comeca_y = 0
termina_x = 0
termina_y = 0

# atribuir a classe gráfico 3D a uma variável que atuará por fora, a chamando.
grafico = grafico_3D(comeca_x, comeca_y, termina_x, termina_y)

# chamada de uma função da classe para rodar o programa
grafico.opcoes_limite_grafico()
