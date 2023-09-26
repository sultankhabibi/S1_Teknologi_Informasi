from experta import *

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
	global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
	diseases = open("./Sistem Pakar Diagnosa Penyakit/penyakit.txt")
	diseases_t = diseases.read()
	diseases_list = diseases_t.split("\n")
	diseases.close()
	for disease in diseases_list:
		disease_s_file = open("./Sistem Pakar Diagnosa Penyakit/Gejala penyakit/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		s_list = disease_s_data.split("\n")
		diseases_symptoms.append(s_list)
		symptom_map[str(s_list)] = disease
		disease_s_file.close()
		disease_s_file = open("./Sistem Pakar Diagnosa Penyakit/Deskripsi penyakit/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_desc_map[disease] = disease_s_data
		disease_s_file.close()
		disease_s_file = open("./Sistem Pakar Diagnosa Penyakit/Obat penyakit/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_treatment_map[disease] = disease_s_data
		disease_s_file.close()
	

def identify_disease(*arguments):
	symptom_list = []
	for symptom in arguments:
		symptom_list.append(symptom)
	# Handle key error
	return symptom_map[str(symptom_list)]

def get_details(disease):
	return d_desc_map[disease]

def get_treatments(disease):
	return d_treatment_map[disease]

def if_not_matched(disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("")
		print("Kemungkinan penyakit yang kamu miliki adalah %s\n" %(id_disease))
		print("Sedikit deskripsi tentang penyakit yang diberikan :")
		print(disease_details+"\n")
		print("Pengobatan umum dan prosedur yang disarankan oleh dokter adalah :")
		print(treatments+"\n")

class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print ("===================================")
		print ("Deteksi Demam Berdarah dan Malaria")
		print ("==================================")
		print("Apakah anda merasakan beberapa gejala dibawah ini(yes/no):")
		print("")
		yield Fact(action="find_disease")

    #Gejala
    
    #suhu badan tinggi
	@Rule(Fact(action='find_disease'), NOT(Fact(suhu_badan_tinggi=W())),salience = 1)
	def symptom_0(self):
		self.declare(Fact(suhu_badan_tinggi=input("Apakah suhu badan anda tinggi: ")))

    # sakit kepala
	@Rule(Fact(action='find_disease'), NOT(Fact(sakit_kepala=W())),salience = 1)
	def symptom_1(self):
		self.declare(Fact(sakit_kepala=input("Apakah anda mengalami sakit kepala: ")))

    # nyeri sendi, otot, dan tulang (nyeri sendi).
	@Rule(Fact(action='find_disease'), NOT(Fact(nyeri_sendi=W())),salience = 1)
	def symptom_2(self):
		self.declare(Fact(nyeri_sendi=input("Apakah anda mengalami nyeri sendi: ")))

    # mual dan muntah
	@Rule(Fact(action='find_disease'), NOT(Fact(mual_muntah=W())),salience = 1)
	def symptom_3(self):
		self.declare(Fact(mual_muntah=input("Apakah anda merasa mual dan ingin muntah: ")))

    # hilang selera makan
	@Rule(Fact(action='find_disease'), NOT(Fact(hilang_selera_makan=W())),salience = 1)
	def symptom_4(self):
		self.declare(Fact(hilang_selera_makan=input("Apakah anda kehilangan selera makan: ")))

    # nyeri di belakang mata
	@Rule(Fact(action='find_disease'), NOT(Fact(nyeri_belakang_mata=W())),salience = 1)
	def symptom_5(self):
		self.declare(Fact(nyeri_belakang_mata=input("Apakah anda merasa nyeri di belakang mata: ")))

    # muncul ruam merah 
	@Rule(Fact(action='find_disease'), NOT(Fact(ruam_merah=W())),salience = 1)
	def symptom_6(self):
		self.declare(Fact(ruam_merah=input("Apakah anda muncul ruam merah: ")))
	
    # menggigil
	@Rule(Fact(action='find_disease'), NOT(Fact(menggigil=W())),salience = 1)
	def symptom_7(self):
		self.declare(Fact(menggigil=input("Apakah anda menggigil: ")))
	
    # tubuh kelelahan
	@Rule(Fact(action='find_disease'), NOT(Fact(tubuh_kelelahan=W())),salience = 1)
	def symptom_8(self):
		self.declare(Fact(tubuh_kelelahan=input("Apakah tubuh anda kelelahan: ")))
	
    # berkeringat berlebihan
	@Rule(Fact(action='find_disease'), NOT(Fact(berkeringat_berlebih=W())),salience = 1)
	def symptom_9(self):
		self.declare(Fact(berkeringat_berlebih=input("Apakah tubuh anda berkeringat berlebihan: ")))
	
    # diare
	@Rule(Fact(action='find_disease'), NOT(Fact(diare=W())),salience = 1)
	def symptom_10(self):
		self.declare(Fact(diare=input("Apakah anda mengalami diare: ")))
	
	@Rule(Fact(action='find_disease'),
	      Fact(suhu_badan_tinggi="yes"),
	      Fact(sakit_kepala="yes"),
		  Fact(nyeri_sendi="yes"),
		  Fact(mual_muntah="yes"),
		  Fact(hilang_selera_makan="yes"),
		  Fact(nyeri_belakang_mata="yes"),
		  Fact(ruam_merah="yes"),
		  Fact(menggigil="no"),
		  Fact(tubuh_kelelahan="no"),
		  Fact(berkeringat_berlebih="no"),
		  Fact(diare="no"))
	def disease_0(self):
		self.declare(Fact(disease="demam berdarah"))

	@Rule(Fact(action='find_disease'),
	      Fact(suhu_badan_tinggi="yes"),
	      Fact(sakit_kepala="yes"),
		  Fact(nyeri_sendi="yes"),
		  Fact(mual_muntah="yes"),
		  Fact(hilang_selera_makan="no"),
		  Fact(nyeri_belakang_mata="no"),
		  Fact(ruam_merah="no"),
		  Fact(menggigil="yes"),
		  Fact(tubuh_kelelahan="yes"),
		  Fact(berkeringat_berlebih="yes"),
		  Fact(diare="yes"))
	def disease_0(self):
		self.declare(Fact(disease="malaria"))		    

	@Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)

	def disease(self, disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("")
		print("Kemungkinan terbesar yang anda alami adalah %s\n" %(id_disease))
		
		print("Berikut deskripsi singkat dari penyakit yang diberikan :")
		print(disease_details+"\n")
		print("Beberapa pengobatan yang disarankan :")
		print(treatments+"\n")		

	@Rule(Fact(action='find_disease'),
		  Fact(suhu_badan_tinggi=MATCH.suhu_badan_tinggi),
		  Fact(sakit_kepala=MATCH.sakit_kepala),
		  Fact(nyeri_sendi=MATCH.nyeri_sendi),
		  Fact(mual_muntah=MATCH.mual_muntah),
		  Fact(hilang_selera_makan=MATCH.hilang_selera_makan),
		  Fact(nyeri_belakang_mata=MATCH.nyeri_belakang_mata),
		  Fact(ruam_merah=MATCH.ruam_merah),
		  Fact(menggigil=MATCH.menggigil),
		  Fact(tubuh_kelelahan=MATCH.tubuh_kelelahan),		  
		  Fact(berkeringat_berlebih=MATCH.berkeringat_berlebih),		  		  
		  NOT(Fact(disease=MATCH.disease)),salience = -999)

	def not_matched(self,suhu_badan_tinggi, sakit_kepala, nyeri_sendi, mual_muntah, hilang_selera_makan, nyeri_belakang_mata, ruam_merah, menggigil, tubuh_kelelahan, berkeringat_berlebih):
		print("\nTidak menemukan penyakit yang sangat pas dengan gejala yang anda alami")
		lis = [suhu_badan_tinggi, sakit_kepala, nyeri_sendi, mual_muntah, hilang_selera_makan, nyeri_belakang_mata, ruam_merah, menggigil, tubuh_kelelahan, berkeringat_berlebih]
		max_count = 0
		max_disease = ""
		for key,val in symptom_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "yes"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_disease = val
		if_not_matched(max_disease)


if __name__ == "__main__":
	preprocess()
	engine = Greetings()
	while(1):
		engine.reset()  # Prepare the engine for the execution.
		engine.run()  # Run it!
		print("Ingin mencoba diagnosa dengan gejala yang lain? (yes/no)")
		if input() == "no":
			print(engine.facts)
			exit()