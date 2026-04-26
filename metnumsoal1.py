#this is my first journey to learn python, i hope i'll get more things to learn about science data and physics-based data implemetation
#anyway, i use bahasa Indonesia to code this one
#so sorry if this syntax not so simple, I'm newbie

import sympy 
import math

print('----------')
print('metode numerik')
print('----------')

iterasi = 0

print('''      1) bisection
       2) regula falsi
       3) newton-raphson
       4) secant''')
pilihan = int(input('masukkan operasi metode numerik: '))

if pilihan == 1:
        a = float(input('masukkan interval bawah: '))
        b = float(input('masukkan interval atas: '))
        print(f'INTERVAL = [{a} , {b}]')
        while iterasi < 5: 
            print('----------')
            print('biseksi')
            print('----------')

            iterasi += 1
            y1 = a**3 + 5*a - 1
            y2 = b**3 + 5*b - 1
            print(f'f ({a}) = {y1}')
            if y1 < 0:
                print('y1 negatif')
            else:
                print('y1 positif')
            print(f'f ({b}) = {y2}')
            if y2 < 0:
                print('y2 negatif')
            else:
                print('y2 positif')
            
            c = (a + b) / 2
            print(f'titik tengah interval adalah {c}')
            y3 = c**3 + 5*c - 1
            print(f'f({c}) = {y3}')

            if y3 < 0:
                a = c
                print(f'interval bawah terbaru adalah {c}')
            else:
                b = c
                print(f'interval atas terbaru adalah {c}')

            
            print(f'INTERVAL TERBARU = [{a},{b}]')
        if iterasi == 5:
            print(f'INTERVAL TERBARU NAN TERUJUNG = [{a},{b}]')
            akar = (a + b) / 2
            print(f'AKAR DUGAAN = {akar}')

elif pilihan == 2:
    a = float(input('masukkan interval bawah: '))
    b = float(input('masukkan interval atas: '))
    print(f'INTERVAL = [{a} , {b}]')
    while iterasi < 5:
        iterasi += 1
        print('----------')
        print('regula falsi')
        print('----------')
        
        y1 = a**3 + 5*a - 1
        y2 = b**3 + 5*b - 1
        print(f'f ({a}) = {y1}')
        if y1 < 0:
            print('y1 negatif')
        else:
            print('y1 positif')
        print(f'f ({b}) = {y2}')
        if y2 < 0:
            print('y2 negatif')
        else:
            print('y2 positif')
            
        regfas = b - (y2*(b-a)) / (y2 - y1) 
        print(f'regula falsi = {regfas}')

        y3 = regfas**3 + 5*regfas - 1
        print(f'f ({regfas}) = {y3}')

        if y3 < 0:
            a = regfas
            print(f'a terkini = {a}')
        else:
            b = regfas
            print(f'a terkini = {b}')
            
        print(f'INTERVAL TERBARU = [{a},{b}]')
    if iterasi == 5:
        print(f'INTERVAL TERBARU NAN TERUJUNG = [{a},{b}]')
        print(f'akar dugaan bisa dihipotesiskan menyesuaikan situasi hitungan berikut')

elif pilihan == 3:
    print('----------')
    print('newton-raphson')
    print('----------')
    x = float(input('masukkan titik awal: '))
    a = sympy.symbols('a')
    e = 2.718281828
    f = e**-a - a
    df = sympy.diff(f,a)
    print(f)
    print(df)
    while iterasi < 5:
        iterasi += 1
        fx = f.subs(a,x)
        dfx = df.subs(a,x)
        x_new = x - (fx/dfx)
        print(f'iterasi {iterasi} = {x_new}')
        x = x_new

    if iterasi == 5:
        print(f'AKAR BERUJUNG = {x}')

elif pilihan == 4:
    print('----------')
    print('newton-raphson')
    print('----------')

    x0 = float(input('masukkan titik pertama: '))
    x1 = float(input('masukkan titik kedua: '))

    while iterasi < 5:
        iterasi += 1

        f0 = x0**3 + 5*x0 - 1
        f1 = x1**3 + 5*x1 - 1

        x2 = x1 - (f1*(x1-x0))/(f1-f0)
        print(f'iterasi {iterasi} = {x2}')

        x0 = x1
        x1 = x2

    if iterasi == 5:
        print(f'AKAR BERUJUNG = {x2}')

    else:
        print('invalid')
        
else:
    print('invalid')
