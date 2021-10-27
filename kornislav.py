def find_area(sides: list) -> int:
    sides = sorted(sides)
    side_1 = sides[0]
    side_2 = sides[2]
    return side_1 * side_2

sides = list(map(int, input().rstrip().split()))
print(find_area(sides))