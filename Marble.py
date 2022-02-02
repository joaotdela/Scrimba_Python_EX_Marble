import random
bag = ('green', 'green', 'green', 'green', 'green',
       'black', 'red', 'red', 'red', 'white')
start_purse = 1000
purse = start_purse
result = 0
rounds = 3
marble = 'none'
print(f'You start the game with {start_purse} gold pieces')
for draw in range(1, rounds+1):
    bet = int(input(
        'Current Purse: {purse} Last draw: {marble} \nRound {draw} - How much do you want to bet?: '))
    marble = random.choice(bag)
    if marble == 'green':
        result = bet
    elif marble == 'black':
        result = 10*bet
    elif marble == 'white':
        result = -5*bet
    else:
        result = -bet
    purse += result
    if purse < 0.5 * start_purse:
        print(f'Game over! You lost to much gold!!!')
        break
    # print results
    print(f'purse: {purse}, last result: ({marble}): {result}')
    print('')
# print final results
print('starting/ ending purse: ', start_purse, '/', purse)
print('gain/loss: ', ((purse-start_purse)/start_purse * 100), '%')
