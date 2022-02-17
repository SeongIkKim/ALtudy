def transpose_board(board):
  return list(zip(*board))

def game_status(board_size, board):
  transposed = transpose_board(board)
  board_count = {'B':0, 'R':0, '.':0}
  blue_line = red_line = 0
  for line in board:
    if set(line) == set('B'):
      blue_line += 1
    for cell in line:
      try:
        board_count[cell] += 1
      except:
        return "Impossible"
  for line in transposed:
    if set(line) == set('R'):
      red_line += 1

  if blue_line + red_line > 1 \
          or abs(board_count['B'] - board_count['R']) > 1:
    # TODO 여기에 들어가야하는 테스트케이스가 너무 많아서 어떻게 해야할지 모르겠다.
    return 'Impossible'
  if blue_line + red_line == 0 and board_count['.'] > 0 :
    return 'Nobody wins'
  if blue_line > red_line:
    return 'Blue wins'
  if blue_line < red_line:
    return 'Red wins'


def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1, 1):
    board_size = int(input())
    board = []
    for _ in range(board_size):
      board.append(list(input().strip()))

    ans = game_status(board_size, board)

    print("Case #{}: {}".format(test_case, ans))


if __name__ == "__main__":
  main()
