import random


class Game:
    def __init__(self, fee):
        self.turn = 0
        self.coin = None
        self.player_money = 0
        self.bank_money = 0

    def __repr__(self):
        return 'Player total: {0} | Bank total: {1}'.format(self.player_money, self.bank_money)

    def toss_coin(self):
        toss = random.randint(0, 1)
        if toss == 0:
            self.turn += 1
            self.coin = 'Head'
            return True
        else:
            self.coin = 'Tails'
            return False


def main():
    try:
        fee = int(input('Entrance fee: '))
    except Exception as e:
        print(e)

    game = Game(fee)

    while input('Try your luck (y / n) ? ') == 'y':
        game.turn = 0

        print('Coin toss results:\n')
        while game.toss_coin():
            print(game.coin)

        player_win = 2**game.turn
        bank_win = fee - 2**game.turn
        game.player_money += player_win - fee
        game.bank_money += bank_win

        print('Tails\n\nNumber of Head coins: {0}'.format(game.turn))
        print('You win: {0} | Bank wins: {1}'.format(player_win, bank_win))
        print(game)


if __name__ == '__main__':
    main()