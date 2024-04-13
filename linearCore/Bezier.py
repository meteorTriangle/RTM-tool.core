def Bezier(t, P0, P1, P2, P3):
            X0:float = 1 * ((1-t) ** 3) * (t**0)
            X1:float = 3 * ((1-t) ** 2) * (t**1)
            X2:float = 3 * ((1-t) ** 1) * (t**2)
            X3:float = 1 * ((1-t) ** 0) * (t**3)
            D0 = P0 * X0
            D1 = P1 * X1
            D2 = P2 * X2
            D3 = P3 * X3
            return D0+D1+D2+D3