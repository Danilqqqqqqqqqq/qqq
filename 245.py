def check_triangle(a, b, c):
    # Проверяем существование треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        return "Из указанных длин невозможно построить треугольник."

    # Определяем тип треугольника
    if a == b == c:
        return "Это равносторонний треугольник."
    elif a == b or a == c or b == c:
        return "Это равнобедренный треугольник."
    else:
        return "Это разносторонний треугольник."

# Основная логика программы
if __name__ == "__main__":
    try:
        print("Введите длины трех сторон треугольника (целые числа): ")
        side_a = int(input("Длинна первой стороны: "))
        side_b = int(input("Длинна второй стороны: "))
        side_c = int(input("Длинна третьей стороны: "))
        
        result = check_triangle(side_a, side_b, side_c)
        print(result)
    except ValueError:
        print("Ошибка! Нужно вводить целые числа.")