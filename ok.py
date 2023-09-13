import math
def calculator():
    print("Добро пожаловать в инженерный калькулятор!")

    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Квадратный корень")
        print("7. Факториал")
        print("8. Синус")
        print("9. Косинус")
        print("10. Тангенс")
        print("0. Выход")

        choice = int(input("Введите номер операции: "))

        if choice == 0:
            print("До свидания!")
            break

        elif choice == 1:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            result = num1 + num2
            print("Результат сложения:", result)

        elif choice == 2:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            result = num1 - num2
            print("Результат вычитания:", result)

        elif choice == 3:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            result = num1 * num2
            print("Результат умножения:", result)

        elif choice == 4:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            if num2 != 0:
                result = num1 / num2
                print("Результат деления:", result)
            else:
                print("Ошибка! Деление на ноль недопустимо.")

        elif choice == 5:
            base = float(input("Введите число: "))
            exponent = float(input("Введите степень: "))
            result = base ** exponent
            print("Результат возведения в степень:", result)

        elif choice == 6:
            num = float(input("Введите число: "))
            if num >= 0:
                result = math.sqrt(num)
                print("Квадратный корень:", result)
            else:
                print("Ошибка! Квадратный корень из отрицательного числа недопустим.")

        elif choice == 7:
            num = int(input("Введите число: "))
            result = math.factorial(num)
            print("Факториал:", result)

        elif choice == 8:
            angle = float(input("Введите угол в градусах: "))
            result = math.sin(math.radians(angle))
            print("Синус:", result)

        elif choice == 9:
            angle = float(input("Введите угол в градусах: "))
            result = math.cos(math.radians(angle))
            print("Косинус:", result)

        elif choice == 10:
            angle = float(input("Введите угол в градусах: "))
            result = math.tan(math.radians(angle))
            print("Тангенс:", result)

        else:
            print("Ошибка! Введите правильный номер операции.")


calculator()
