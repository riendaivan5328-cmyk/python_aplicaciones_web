import datetime
fecha= datetime.datetime.now().year


listaaños=[1990, 1994, 2001, 2004, 2012, 2015, 2026]
for año in listaaños:
    listaedad=[fecha-año]
    for edad in listaedad:
        print(edad)