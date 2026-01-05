def eh_primo(num):
    """Verifica se um número é primo"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def obter_n_primeiros_primos(n):
    """Obtém os n primeiros números primos"""
    primos = []
    num = 2
    
    while len(primos) < n:
        if eh_primo(num):
            primos.append(num)
        num += 1
    
    return primos


# Exibir os 100 primeiros números primos
primos = obter_n_primeiros_primos(100)

print(f"Os 100 primeiros números primos:\n")
for i, primo in enumerate(primos, 1):
    print(f"{i:3d}. {primo:4d}", end="   ")
    if i % 5 == 0:  # Nova linha a cada 5 números
        print()

print(f"\n\nTotal: {len(primos)} números primos")
print(f"O 100º número primo é: {primos[-1]}")
