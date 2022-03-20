import os
try:
    os.mkdir("elma") #klasör oluşturur
except FileExistsError:
    print("Aynı adla klasör var!")
