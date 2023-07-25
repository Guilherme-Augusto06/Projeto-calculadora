S = 1 

while S == 1:


    print("Essa é uma calculadora simples de 4 operações:")
    print("- Adição +")
    print("- Subtração -")
    print("- Multiplicação *")
    print("- Divisão %")
    print(" ")

    w = 1

    while w == 1:

        Adição = "a"
        Subtração = "s"
        Multiplicação = "m"
        Divisão = "d"

        print("Qual operação você deseja realizar?")
        print("Adição = a")
        print("Subtração = s")
        print("Multiplicação = m")
        print("Divisão = d")
        print(" ")
        
        z = input(" ")

        print(" ")

        x = float(input("Digite o 1° valor que deseja realizar a operação: "))
        b = float(input("Digite o 2° valor que deseja realizar a operação: "))

        g = (x + b)
        h = (x - b)
        i = (x * b)
        j = (x / b)

        if z == Adição:
            print(f"A soma será: {x} + {b}")
            print(f"O resultado será: {g}")
        elif z == Subtração:
            print(f"A subtração será: {x} - {b}")
            print(f"O resultado será: {h}")
        elif z == Multiplicação:
            print(f"A multiplicação será: {x} * {b}")
            print(f"O resultado será: {i}")
        elif z == Divisão:
            print(f"A divisão será: {x} / {b}")
            print(f"O resultado será: {j}")
        else:
            print("Operação solicitada não pode ser efetuada.")

        sim = "y"
        não = "n"

        if S == 1:
            print("você deseja sair")
            print("sim = y")
            print("não = n")

        z = (input(" "))

        if z == sim:
            S = 0
        elif z == não:
            S = 1   
        else:
            print(" ")
            print("comando inválido")
            print(" ")

        if S == 1:
            print("você deseja sair")
            print("sim = y")
            print("não = n")
        z = (input(" "))

        if z == sim:
                S = 0
        elif z == não:
                S = 1   
        else:
            print(" ")
            print("comando inválido")
            print(" ")
            S = 2

