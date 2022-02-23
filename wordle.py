import re

import random

import table as tb

with open("wordle.txt") as file:

    words = file.read().replace(" '","").replace("'","").replace("\n","").split(",")

#sıralama input ile alınacak (doğruluk)

#örn 02102

#0 harf yok

#sarı 1 harf var yeri yanlış

#yeşil 2 harf var yeri doğru

ilk = input("İlk kelimeyi siz mi seçmek istersiniz ,şansa mı (e-h) : ")

if ilk =="e":

	rastgele = input("Kelimeyi giriniz : ")

else:

	rastgele = random.choice(words)

sifir= ""

def ekle(num,k):

	num+= k

	return "".join(set(num))

def yerlestir():

	global sifir

	bir,iki = "",""

	for s,k in zip(sıralama,kelime):

		if s == "0" and (k not in (bir or iki)):

			sifir= ekle(sifir,k)

		elif s =="1":

			bir+= ekle(bir,k)

		else:

			iki+= k

	return bir,iki

def srch():

    	search=""

    	for harf,sır in zip(kelime,sıralama):

    		if sır =="0":

    			search+=f"[^{sifir}]"

    		elif sır =="1":

    			search+=f"[^{harf+sifir}]"

    		else:

    			search+=harf	

    	return search

def elemine():

    wordl = []

    

    for i in set(kelimeler):

    	w = re.search(sorgu,i)

    	if w:

    		if bir:

    			var = True

    			for b in bir:

    				if b not in i:

    					var = False

    					break

    			if var:

    				wordl.append(i)

    		else:

    				wordl.append(i)

    return wordl

	

while True:

    kelimeler = words

    words = []

    kelime = rastgele

    print("*********")

    print("*",kelime.upper(),"*")

    print("*********")

    

    sıralama = input("doğruluğu  giriniz : ")

    

    bir,iki = yerlestir()

    sorgu= srch()

    words= elemine()

    words.sort()    

    tb.tablo(words)

    

    if len(words) >1:

    	secim = input("Seçimi siz mi yapmak istersiniz rastgele mi (e-h) : ")

    	if secim == "e":

    		y,x = input("Seçimizi giriniz (örn : 154 5) : ").split()

    		rastgele = words[int(y)*6+int(x)]

    	else:

    		rastgele = random.choice(words)

    else:

    	break

    
