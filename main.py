from game import Game

FILENAME = "./Wyniki/test.csv"


def main():
    results = []
    ticTacToe = Game()
    # perform 100 game sets
    for j in range(1, 501):
        menace = player = draw = 0
        # perform 50 games
        for i in range(1, 50):
            score = ticTacToe.play()
            if score == 0:
                draw += 1
            elif score == 1:
                menace += 1
            elif score == 2:
                player += 1
            else:
                raise ValueError("ERROR in a game")
        results.append([j, menace, player, draw])

    # save results into file
    excelFile = open(FILENAME, "wt")
    for i in range(0, int(len(results))):
        excelFile.write(str(results[i][0]) + ' ' + str(results[i][1]) + ' ' + str(results[i][2]) + ' ' + str(results[i][3]) + '\n')
    excelFile.close()
    print("[nr, menace, player, draw]")
    print(results)


main()
