def isPrime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


cont = 1

while cont == 1:
    print("Tecle 1 para testar se o número é primo\n")
    print("Tecle 0 para finalizar")

    entrada = input("Digite o número da ação: ")

    if entrada == "1":
        primo = int(input("Digite o número: "))
        if isPrime(primo):
            print(f"{primo} é primo")
        else:
            print(f"{primo} não é primo")

    elif entrada == "0":
        print("Programa finalizado!")
        cont = 0
    else:
        print("Número incorreto, tente novamente!")

