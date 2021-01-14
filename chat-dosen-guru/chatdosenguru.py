##By Widi Afandi

#Library
import pywhatkit as bot
import datetime
from googletrans import Translator
import os

#Gender guru/dosen
def isMale(gender_dosen):
	if (gender_dosen == "L"):
		sapaan = "pak"
	else:
		sapaan = "bu"
	return sapaan

#Waktu sekarang
def isTime():
	time = datetime.datetime.now()
	if (time.hour < 10):
		waktu = "pagi "
	elif (time.hour < 14):
		waktu = "siang "
	elif (time.hour < 18):
		waktu = "sore "
	else:
		waktu = "malam "	
	return waktu

def kalimat_siap(nama, kelas, pertanyaan, gender_dosen, no_telp, bahasa):
	#Sapaan untuk dosen/guru (pak/bu)
	sapaan = isMale(gender_dosen)
	
	#Salam pembuka (Pagi, Siang, Sore, Malam)	
	waktu = isTime()
		
	#Pesan yang dikirim
	kalimat = "Selamat " + waktu + sapaan + ", maaf mengganggu waktunya. \nPerkenalkan nama saya " + nama + " dari kelas " + kelas + ". Izin bertanya, " + pertanyaan + " " + sapaan + "?. \nTerima kasih sebelumnya " + sapaan
	
	#Bahasa pada pesan
	if (bahasa == "EN"):
		translator = Translator()
		kalimat = translator.translate(kalimat)
		kalimat = kalimat.text	
	
	#Lihat pesan yang akan dikirim
	os.system("clear")
	print("Kalimat yang akan dikirim:")
	print(kalimat)
	print("\nNOTE: Pesan dapat diubah ketika masuk pada whatsapp web")
	#Kirim ke Whatsapp
	bot.sendwhatmsg(no_telp, kalimat, time.hour, time.minute + 2)

#Main
#Input data Anda dan Dosen/guru Anda
nama = input("Nama Anda: ")
kelas = input("Kelas Anda: ")
pertanyaan = input ("Apa yang Anda ingin tanyakan: ")
gender_dosen = input("Gender dosen/guru anda (L/P): ")
no_telp = input("No telp dosen/guru Anda: ")
bahasa = input("Pilih bahasa pesan yang akan dikirim(EN/IN): ")

kalimat_siap(nama, kelas, pertanyaan, gender_dosen, no_telp, bahasa)
