nilai = 100
if nilai > 80:
	print ("Selamat, kamu dapat nilai A")
	if nilai > 95:
		print ("Selamat kamu dapat bonus voucher pendidikan karena nilai kamu A")
	elif nilai == 100:
		print ("Selamat kamu dapat buku pelajaran gratis selama satu semester karena nilai kamu A sempurna.")
elif nilai > 70 and nilai <=80:
	print ("Selamat, kamu dapat nilai B")
elif nilai > 60 and nilai <=70:
	print ("Selamat, kamu dapat nilai C")
elif nilai > 45 and nilai <=60:
	print ("Selamat, kamu dapat nilai D")
else:
	print ("Maaf, kamu dapat nilai E. Kamu harus ikut ujian remedial :(")