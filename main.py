from ttt import game_loop

if __name__ == '__main__':
    game_loop(algorithm='mcts', num_iterations=1500)
    # game_loop(algorithm='negamax', max_depth = 8)


