# latihan_programming_pppk

Latihan untuk persiapan test PPPK

1.  menampilkan variabel tipe int 
2. Logika Dasar 
3. Menentukan kesalahan debug

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