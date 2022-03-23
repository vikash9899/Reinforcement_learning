import matplotlib.pylab as plt
import seaborn as sns
from env import black_jack as bj
import numpy as np
import pandas as pd

'''
env = bj.BlackJack()

# print(env.nStates)
# print(env.nAction)
# print(env.Actions)
# print(env.States)
# print(env.nCards)
# print(env.dealers_cards)
# print(env.players_cards)
# print(env.dealers_hand)
# print(env.players_hand)

ob = env.play('Hit')
print("ob", ob)

ob1 = ()
if len(ob) > 1 and ob[5] == False:
    ob1 = env.play('Hit')

print('ob1', ob1)

ob2 = ()
if len(ob1) > 1 and ob1[5] == False: 
    ob2 = env.play('Stick') 

print('ob2', ob2)


env1 = bj.BlackJack() 
ob1 = env1.play('Stick') 
print(ob1) 
'''


def mc_greedy_policy(sa_values, state, epsilon, nA):
    prob = np.ones(nA) * epsilon / nA
    prob[np.argmax(sa_values[state])] += 1 - epsilon
    # print(np.sum(prob))
    return prob


def Monte_carlo(env, episodes, gamma=1.):
    sa_values = np.zeros((env.nS+1, env.nA), dtype=np.float16)
    visits = np.zeros((env.nS+1, env.nA), dtype=np.int16)
    Actions = ['Hit', 'Stick']

    for i in range(episodes):
        # print("Episode ", i, " :- ")
        ob = env.start()
        state = ob['nState']
        Gt = 0
        ep_detail = []
        game_over = False
        while not game_over:
            # greedy policy improvement.
            prob = mc_greedy_policy(sa_values, state, 0.2, env.nA)

            # take the action
            action = np.random.choice(np.arange(len(prob)), p=prob)

            # Take the Action
            ob = env.play(Actions[action])

            if i in range(episodes-20, episodes):
                print('ob', ob)
                print()

            ep_detail.append((state, action, ob['reward']))
            state = ob['nState']
            game_over = ob['done']

        while len(ep_detail) != 0:
            ep_detail.reverse()

            S, A, R = ep_detail.pop()

            Gt = R + gamma * Gt

            visits[S][A] = visits[S][A] + 1

            sa_values[S][A] = sa_values[S][A] + \
                (Gt - sa_values[S][A] / visits[S][A])

    return sa_values


def main():
    env = bj.BlackJack()
    Q = Monte_carlo(env, 50000)

    df = pd.DataFrame(Q)
    df.columns = ['Hit', 'Stick']
    # df['score'] = np.array(list(range(31)))
    df = df.loc[list(range(4, 22))]
    print(df)
    # print(Q[3:22, :])

    ax = sns.heatmap(df, linewidth=0.5)
    plt.show()


if __name__ == '__main__':
    main()
