MOD = 10**9 + 7

# Elegí un MAXN que cubra al máximo 'n' del problema.
# Si en el enunciado dice que a <= 10^6, esto está bien.
MAXN = 10**6 + 5

# Precomputo factoriales e inversos factoriales UNA sola vez.
fact = [1] * (MAXN + 1)
inv_fact = [1] * (MAXN + 1)

# factoriales: fact[i] = i! mod MOD
for i in range(1, MAXN + 1):
    fact[i] = (fact[i - 1] * i) % MOD

# inverso del factorial más grande usando Fermat: a^(MOD-2) mod MOD
inv_fact[MAXN] = pow(fact[MAXN], MOD - 2, MOD)

# resto de los inversos factoriales hacia atrás:
for i in range(MAXN, 0, -1):
    inv_fact[i - 1] = (inv_fact[i] * i) % MOD


def binomial_coefficient(n, m):
    """
    Devuelve C(n, m) mod MOD.

    Misma interfaz que antes:
        - n: total de elementos
        - m: elementos elegidos

    Ahora usa:
        C(n,m) = fact[n] * inv_fact[m] * inv_fact[n-m] (mod MOD)

    Importante:
        - Si m > n, devuelve 0.
        - Asegurate de que n <= MAXN.
    """
    if m < 0 or m > n:
        return 0
    return (fact[n] * inv_fact[m] % MOD) * inv_fact[n - m] % MOD