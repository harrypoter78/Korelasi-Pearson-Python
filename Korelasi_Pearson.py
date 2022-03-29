import pandas as pd

def sigma1(inp):
    arr = []
    out = 0
    for x in range(n):
        arr.append(inp[x])
        out += arr[x]
    return out, arr

def sigma2(inpX, inpY):
    arr = []
    out = 0
    for x in range(n):
        arr.append((inpX[x] * inpY[x]))
        out += arr[x]
    return out, arr

def sigpow1(inp):
    arr = []
    out = 0
    for x in range(n):
        arr.append((inp[x] ** 2))
        out += arr[x]
    return out, arr

def cariHasil(inpX, inpY, inpN):
    Yi = sigma1(inpY)[0]
    Yi2 = sigpow1(inpY)[0]
    Xi2 = sigpow1(inpX)[0]
    Xi = sigma1(inpX)[0]
    XiYi = sigma2(inpX, inpY)[0]
    out = round(((inpN * XiYi) - (Xi * Yi))
                / ((((inpN * Xi2) - (Xi ** 2))
                    * ((inpN * Yi2) - (Yi ** 2))) ** 0.5), 3)

    print('Y = ', Yi)
    print('X = ', Xi)
    print('Y2 = ', Yi2)
    print('X2 = ', Xi2)
    print('XY = ', XiYi)

    # atas = ((inpN * XiYi) - (Xi * Yi))
    # bawahakar = ((((inpN * Xi2) - (Xi ** 2)) * ((inpN * Yi2) - (Yi ** 2)))** 0.5)
    # bawah1 = (inpN * Xi2)
    # bawah2 = (Xi ** 2)
    # bawah3 = (inpN * Yi2)
    # bawah4 = (Yi ** 2)
    # print('atas = ', atas)
    # print('bawahakar = ', bawahakar)
    # print('bawah1 = ', bawah1)
    # print('bawah2 = ', bawah2)
    # print('bawah3 = ', bawah3)
    # print('bawah4 = ', bawah4)
   
    return out

def skalaguilford(inp):
    if (inp < 0.2) and (inp >= 0):
        skala = 'Sangat Lemah'
    elif (inp < 0.4) and (inp >= 0.2):
        skala = 'Lemah'
    elif (inp < 0.6) and (inp >= 0.4):
        skala = 'Sedang'
    elif (inp < 0.8) and (inp >= 0.6):
        skala = 'Kuat'
    elif (inp <= 1.0) and (inp >= 0.8):
        skala = 'Sangat Kuat'
    return skala

if __name__ == '__main__':
    data = pd.read_csv("data.csv")

    X = data.columns[1]
    Y = data.columns[2]

    x = data[X]
    y = data[Y]

    n = len(data)
    print(n)

    hasil = cariHasil(x, y, n)
    print(f'Hubungan {X} dan {Y} = ', hasil)
    print('Hubungan dimiliki =', 'Lurus/linear' if (hasil > 0) else 'Terbalik')
    print('Skala Guilford =', skalaguilford(hasil))
    print('Koefisien Determinasi =', (hasil ** 2) * 100, '%')
    print('Kontribusi dari faktor lain =', 100 - ((hasil ** 2) * 100), '%')

