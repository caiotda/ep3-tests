import sys
sys.path.append("..")
import ep3

def main():
        smallMDP = ep3.BlackjackMDP(valores_cartas=[1, 5], multiplicidade=2, limiar=15, custo_espiada=1)
        mediumMDP = ep3.BlackjackMDP(valores_cartas=[1,5,7], multiplicidade=2, limiar=15, custo_espiada=1)
        preEmptyState = (11, None, (1,0))
        print('Começando os testes da Parte 1...\n')


        tests = [
            ################## Testes de Pegar #######################
            ([((5, None, (2, 1)), 1, 0)], smallMDP, (0, 1, (2, 2)), 'Pegar', # Espia e o jogo continua
            'Puxa corretamente a carta espiada'),
            ([((12, None, None), 1, 12)], smallMDP, preEmptyState, 'Pegar', # Espia e o jogo acaba
            'Puxa a última carta do baralho e o jogo acaba'),
            ([((12, None, None), 1, 12)], smallMDP, (11, 0, (1,0)), 'Pegar', 'Espia a última carta e ganha o jogo'),

            ([((18, None, None), 1, 0)], mediumMDP, (13 ,1, (1,1,1)), 'Pegar', 'Jogador passa do limiar quando puxa uma carta específica'),

            ([
                ((2, None, (0,2)), 1/3, 0), #Puxou a carta de valor 1
                ((6, None, (1,1)), 2/3, 0), #Puxou a carta de valor 5
            ], smallMDP, (1, None, (1, 2)), 'Pegar', 'Ao pegar uma carta, reetorna os estados futuros com probabilidades corretas'),
            ###################### Testes de espiar ##################
            ([], smallMDP, ((1, 1, (1, 2))), 'Espiar', 'Falha em tentar espiar duas vezes'),
            ([
                ((0, 0, (2,2)), 1/2, -1),
                ((0, 1, (2,2)), 1/2, -1)
            ], smallMDP, (0, None, (2,2)), 'Espiar', 'Retorna as cartas que podem ser espiadas'),
            #################### Testes de Sair ######################
            ([
                ((11, None, None), 1, 11)
            ], smallMDP, (11, None, (0, 1)), 'Sair', 'Ao sair do jogo, retorna a mão do usuario')
        ]

        results = 0
        for goal, mdp, state, action, suite  in tests:
            test = mdp.succAndProbReward(state, action)
            if goal == test:
                print('{}: PASS'.format(suite))
                results += 1
            else:
                print('{}: FAILED'.format(suite))
                print('Expected: {}, \nreceived: {}'.format(goal, test))
        print('\nBateria de testes concluida. {}/{} testes aprovados'.format(results, len(tests)))

if __name__ == "__main__":
    main()