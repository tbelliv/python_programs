# Fermat's Last Theorem states that no three positive integers a, b, and c satisfy the equation a^n + b^n = c^n

def attempt_disprove_fermat(limit=20):
    a = b = c = n = 1
    while n <= limit:
        if a**n + b**n == c**n:
            print(f"Counterexample found: {a}^{n} + {b}^{n} = {c}^{n}")
            return
        a += 1
        if a > limit:
            a = 1
            b += 1
        if b > limit:
            b = 1
            c += 1
        if c > limit:
            c = 1
            n += 1
    print("No counterexample found within the given limit.")

attempt_disprove_fermat()