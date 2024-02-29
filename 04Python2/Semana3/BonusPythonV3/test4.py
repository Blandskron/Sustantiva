for column in range(0, 5):
    for row in range(0, 5):
        if column + row % 2 == 0:
            break
    else:
        print(f'{column}, {row}')