import random

def generate_test_cases(num_cases):
    cases = []
    for _ in range(num_cases):
        nr = random.randint(1, 24)  # Número de linhas
        nc = random.randint(1, 24)  # Número de colunas
        r = random.randint(1, 7)    # Máximo de elementos em uma linha
        c = random.randint(1, 7)    # Máximo de elementos em uma coluna
        cases.append((nr, nc, r, c))
    return cases

def main():
    num_cases = 10  # Você pode ajustar o número de casos de teste aqui
    test_cases = generate_test_cases(num_cases)
    
    with open('./tests/input_gerar.txt', 'w', encoding='utf-8') as f:
        f.write(f"{num_cases}\n")
        for case in test_cases:
            nr, nc, r, c = case
            f.write(f"{nr} {nc}\n")
            f.write(f"{r} {c}\n")

if __name__ == "__main__":
    main()
