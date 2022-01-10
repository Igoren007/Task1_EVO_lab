def direction(facing, turn):

    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    new_direction = directions[(directions.index(facing) + turn // 45) % 8]
    return new_direction

if __name__ == '__main__':
    print(direction('S', 180))
    print(direction('N', -135))
    print(direction('W', 495))
