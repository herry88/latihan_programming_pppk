awal = int(input('Set Nilai Awal = '))
akhir = int(input('Set Nilai Akhir = '))

count = 0 
summ = 0 
print('Bilangan antara %d dan %d'%(awal, akhir))

# menentukan outputnya

for i in range(awal, akhir+1):
    print (i, end=' ')
    count = count+1
    summ = summ+i

print('Bilangan diatas ada %d bilangan' %count)
print('Jumlah semua Bilangan adalah  %d' %summ)