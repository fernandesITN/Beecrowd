A, B, C=[float(x) for x in input().split()]

pi = 3.14159

RT = (A * C) / 2
RC = C**2 * pi
TR = (A + B) * C / 2
SQ = B**2
RCT = A * B

print(f"TRIANGULO: {RT:.3F}\nCIRCULO: {RC:.3F}\nTRAPEZIO: {TR:.3F}\nQUADRADO: {SQ:.3F}\nRETANGULO: {RCT:.3F}")