def calculate_perimeter(height, weight):
    perimeter = (height + weight) * 2
    print(f"Периметр прямоугольника, равен {perimeter}")


a, b = map(int, input().split())

calculate_perimeter(a, b)
