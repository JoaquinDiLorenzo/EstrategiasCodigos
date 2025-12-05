def knapsack_01(weights, values, max_weight):
    n = len(weights)
    dp = [0] * (max_weight + 1)

    # Recorremos cada objeto una sola vez
    for i in range(n):
        wi = weights[i]
        vi = values[i]

        # Recorremos pesos de atrás hacia adelante.
        # Esto es CRÍTICO para forzar 0/1 knapsack.
        for w in range(max_weight, wi - 1, -1):
            # O no lo tomo (dp[w]) o lo tomo (dp[w - wi] + vi)
            dp[w] = max(dp[w], dp[w - wi] + vi)

    return dp[max_weight]

n, x = map(int, input().split())
objects_weight = list(map(int, input().split()))
objects_price = list(map(int, input().split()))

print(knapsack_01(objects_weight, objects_price, x))