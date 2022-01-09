print ("NIM \t: 5200411413")
print ("Nama \t: Juan Fredrick Pandia")
print ("===============================================================")

def cariwaktutunggu(processes, jumlah, jw,
						wt, quantum):
	rem_jw = [0] * jumlah

	for i in range(jumlah):
		rem_jw[i] = jw[i]
	t = 0 

	while(1):
		done = True

		for i in range(jumlah):
			if (rem_jw[i] > 0) :
				done = False 
				
				if (rem_jw[i] > quantum) :
					t += quantum
					rem_jw[i] -= quantum
				
				else:
					t = t + rem_jw[i]
					wt[i] = t - jw[i]

					rem_jw[i] = 0
				
		if (done == True):
			break
			
def cariwaktuganti(processes, jumlah, jw, wt, tat):
	for i in range(jumlah):
		tat[i] = jw[i] + wt[i]

def cariwakturatarata(processes, jumlah, jw, quantum):
	wt = [0] * jumlah
	tat = [0] * jumlah

	cariwaktutunggu(processes, jumlah, jw,
						wt, quantum)

	cariwaktuganti(processes, jumlah, jw,
								wt, tat)

	print("Proses", "\t\tjumlahwaktu", "\tWaktu Tunggu",
					"\tWaktu Berganti")
	total_wt = 0
	total_tat = 0
	for i in range(jumlah):

		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", i + 1, "\t\t", jw[i],
			"\t\t", wt[i], "\t\t", tat[i])

	print("\nRata - rata Waktu Tunggu \t= %.5f "%(total_wt /jumlah) )
	print("Rata - rata Waktu Berganti \t= %.5f "%(total_tat / jumlah))
	
if __name__ =="__main__":
	
	proses = [1, 2, 3, 4, 5]
	jumlahproses = 5

	jumlahwaktu = [9, 6, 4, 10, 15]

	quantum = 4;
	cariwakturatarata(proses, jumlahproses, jumlahwaktu, quantum)