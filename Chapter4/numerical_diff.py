def numerical_diff(f, x): #中心差分
    h = 1e-4
    return ( f(x+h) - f(x-h) / (2*h))

