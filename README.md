# latihan_programming_pppk

Latihan untuk persiapan test PPPK

1.  menampilkan variabel tipe int 
2. Logika Dasar 
3. Menentukan kesalahan debug
4. Looping

latihan 3
```
Debug 
awal = int(input('Set Nilai Awal = '))
akhir = int(input('Set Nilai Akhir = '))

count = 0 
summ = 0 
print('Bilangan antara %d dan %d'%(awal, akhir))

#before
# for i in range(awal, akhir+1){
#     print (i, end=' ')
#     count = count+1
#     summ = summ+i
# }

Answer

for i in range(awal, akhir+1):
    print (i, end=' ')
    count = count+1
    summ = summ+i

print('Bilangan diatas ada %d bilangan' %count)
print('Jumlah semua Bilangan adalah  %d' %summ)
```

latihan 4 
``` 
Menentukan Output Dari Program di bawah ini : 
awal = int(input('Set Nilai Awal = '))
akhir = int(input('Set Nilai Akhir = '))

count = 0 
summ = 0 
print('Bilangan antara %d dan %d'%(awal, akhir))


for i in range(awal, akhir+1):
    print (i, end=' ')
    count = count+1
    summ = summ+i

print('Bilangan diatas ada %d bilangan' %count)
print('Jumlah semua Bilangan adalah  %d' %summ)

Outputnya Adalah : 
Set Nilai Awal = 5
Set Nilai Akhir = 20
Bilangan antara 5 dan 20
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 Bilangan diatas ada 16 bilangan
Jumlah semua Bilangan adalah  200
```
