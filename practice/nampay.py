import numpy as np
#%% basic işler
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

reshaped = array.reshape(3,5) # 3 satır 5 sütunlu bir matrise çevirdi

shape = reshaped.shape # kaça kaçlık bir matris olduğunu yazar

boyut = reshaped.ndim # kaç boyutlu bir dizi

veri_tipi = reshaped.dtype.name #içindeki veri tipi

dizi_buyukluk = reshaped.size #eleman sayısı

dizi_buyukluk_a = array.size

sifirlar  = np.zeros((3,5)) #3x5 sıfırlardan olusan matris olusturur

birler  = np.ones((3,5)) #3x5 birlerden olusan matris olusturur

guzel_ozellik = np.arange(10,50,5) # 10'dan başla 50'ye kadar 5er 5er artcak bir array olustur

guzel_ozellik_2 = np.linspace(10,50,5) # 10'dan başla 50 dahil araya 5 sayı koy

#%% bu da basic operasyonlar
x = np.array([3,4,5])
y = np.array([7,8,9])

toplam = x + y

fark = x - y

carpim = x * y

sin_a = np.sin(x)

sin_y = np.sin(y)

x_ikiden_kucukler = x < 2

y_ikiden_buyukler = y > 2

a = np.linspace(0,1,6).reshape(3,2)

b = np.linspace(1,2,6).reshape(2,3)

c = np.linspace(8,10,6).reshape(3,2)

a_b = a.dot(b) #carptik

transpose_a_b = a_b.T #matrisin transpozu

randomlar = np.random.random((3,5)) # 3e 5lik 0-1 aralığında random sayılar

min_random = randomlar.min()

sum_random = randomlar.sum()

sutunlari_topla = randomlar.sum(axis=0)

satirlari_topla = randomlar.sum(axis=1)

max_random = randomlar.max()


new_matris_from_randomlar = (np.linspace(min_random*100, max_random*100, 50)).reshape(25,2) #reshape in tersi .ravel()


dikey_birlesik = np.vstack((a,c))

yatay_birlesik = np.hstack((a,c))