




celcius = int(input('masukan suhu anda dalam celcius: '))
satuan_suhu =(input('pilih satuan suhu yang anda konversikan (R,F,K): '))

if satuan_suhu =="R" or satuan_suhu == 'r' or satuan_suhu =='rearmur':
    hasil = (4/5) * celcius
    print(f"suhu anda dalam reamur adalah {hasil} Reamur")


elif satuan_suhu =="F" or satuan_suhu =='f':
    hasil = ((9/5) * celcius) + 32
    print(f"suhu anda dalam fahrenheit adalah {hasil} Fahrenheit")


elif satuan_suhu =="K" or satuan_suhu =='k':
    hasil = celcius + 273
    print(f"suhu anda dalam kelvin adalah {hasil} Kelvin")

else :
    print('tolong masukkan satuan suhu yang akan di konversikan dengan benar !')













