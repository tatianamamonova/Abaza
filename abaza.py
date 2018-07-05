import re

def distance(a, b):
	n, m = len(a), len(b)
	if n > m:
		# Make sure n <= m, to use O(min(n,m)) space
		a, b = b, a
		n, m = m, n

	current_row = range(n+1) # Keep current and previous row, not entire matrix
	for i in range(1, m+1):
		previous_row, current_row = current_row, [i]+[0]*n
		for j in range(1,n+1):
			add, delete, change = previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]
			if a[j-1] != b[i-1]:
				change += 1
			current_row[j] = min(add, delete, change)

	return current_row[n]

def splitabazacons(AbazaWord):
	Cons = ('б', 'пI', 'п', 'в', 'фI', 'ф', 'м', 'у', 'д', 'тI', 'т', 'дз', 'цI', 'ц', 'з', 'с', 'н', 'джв', 'чIв', 'чв', 'жв', 'шв', 'дж', 'шI', 'тш', 'ж', 'ш', 'р', 'джь', 'чI', 'ч', 'жь', 'щ', 'й', 'ль', 'лI', 'тл', 'л', 'гь', 'кIь', 'кь', 'гъь', 'хь', 'г', 'кI', 'к', 'гъ', 'х', 'гв', 'кIв', 'кв', 'гъв', 'хв', 'къь', 'къ', 'хъ', 'къв', 'хъв', 'ъ', 'гI', 'хI', 'гIв', 'хIв')
	Splitted = []
	for i in range(len(AbazaWord)):
		if AbazaWord[i:i+3] in Cons:
			Splitted.append(AbazaWord[i:i+3])
			i += 2
		elif AbazaWord[i:i+2] in Cons:
			Splitted.append(AbazaWord[i:i+2])
			i += 1
		elif AbazaWord[i:i+1] in Cons:
			Splitted.append(AbazaWord[i:i+1])
	return Splitted

def consdata(abazacons):
	Consdict = { \
	'б': 'labial stop +v', \
	'пI': 'labial stop +ej', \
	'п': 'labial stop -ej', \
	'в': 'labial sibilant +v', \
	'фI': 'labial sibilant +ej', \
	'ф': 'labial sibilant -ej', \
	'м': 'labial nasal', \
	'у': 'labial sonorant', \
	'д': 'dental stop +v', \
	'тI': 'dental stop +ej', \
	'т': 'dental stop -ej', \
	'дз': 'dental affricate +v', \
	'цI': 'dental affricate +ej', \
	'ц': 'dental affricate -ej', \
	'з': 'dental sibilant +v', \
	'с': 'dental sibilant -ej', \
	'н': 'dental nasal', \
	'джв': 'laminal-closed affricate +v', \
	'чIв': 'laminal-closed affricate +ej', \
	'чв': 'laminal-closed affricate -ej', \
	'жв': 'laminal-closed sibilant +v', \
	'шв': 'laminal-closed sibilant -ej', \
	'дж': 'alveolar affricate +v', \
	'шI': 'alveolar affricate +ej', \
	'тш': 'alveolar affricate -ej', \
	'ж': 'alveolar sibilant +v', \
	'ш': 'alveolar sibilant -ej', \
	'р': 'alveolar sonorant', \
	'джь': 'palatal affricate +v', \
	'чI': 'palatal affricate +ej', \
	'ч': 'palatal affricate -ej', \
	'жь': 'palatal sibilant +v', \
	'щ': 'palatal sibilant -ej', \
	'й': 'palatal sonorant', \
	'ль': 'lateral sibilant +v', \
	'лI': 'lateral sibilant +ej', \
	'тл': 'lateral sibilant -ej', \
	'л': 'lateral sonorant', \
	'гь': 'velar stop +p +v', \
	'кIь': 'velar stop +p +ej', \
	'кь': 'velar stop +p -ej', \
	'гъь': 'velar sibilant +p +v', \
	'хь': 'velar sibilant +p -ej', \
	'г': 'velar stop -p +v', \
	'кI': 'velar stop -p +ej', \
	'к': 'velar stop -p -ej', \
	'гъ': 'velar sibilant -p +v', \
	'х': 'velar sibilant -p -ej', \
	'гв': 'velar stop +l +v', \
	'кIв': 'velar stop +l +ej', \
	'кв': 'velar stop +l -ej', \
	'гъв': 'velar sibilant +l +v', \
	'хв': 'velar sibilant +l -ej', \
	'къь': 'uvular stop +p +ej', \
	'къ': 'uvular stop -p +ej', \
	'хъ': 'uvular stop -p -ej', \
	'къв': 'uvular stop +l +ej', \
	'хъв': 'uvular stop +l -ej', \
	'ъ': 'laryngeal stop -l -ej', \
	'гI': 'laryngeal sibilant -l +v', \
	'хI': 'laryngeal sibilant -l -ej', \
	'гIв': 'laryngeal sibilant +l +v', \
	'хIв': 'laryngeal sibilant +l -ej' \
	}
	consdata = Consdict[abazacons]
	return consdata

def process():
	with open('abaza-russian.csv','r',encoding='utf-8') as f:
		data = f.readlines()
	d = open('detected-duplicates.txt','w',encoding='utf-8')
	with open('abaza-missed.txt','w',encoding='utf-8') as e:
		with open('abaza-russian-out.csv','w',encoding='utf-8') as o:
			o.write('Abaza,Russian,Levinstein,Vowels,StressedSyllable,Foc,Vow1st,Vow2nd,FirstCons,LastCons,Consonants\n')
			for line in data:
				try:
					string = line
					Abaza = re.search(r'(.*?)\t',string).group(1)
					parenth = re.search(r'\\n1\) ([а-яё]+)',string)
					if parenth:
						Russian = parenth.group(1)
					else:
						parenth = re.search(r'\\n1\. ([а-яё]+)',string)
						Russian = parenth.group(1)
					non_duplis = ('начинать', 'декадент', 'референт')
					if Russian not in non_duplis and len(Russian)>6 and Russian[:int(len(Russian)/2)][:-2] == Russian[int(len(Russian)/2):][:-2]:
						d.write(Russian+'\n')
						Russian = Russian[:int(len(Russian)/2)]
					Levinstein = distance(Abaza,Russian)
					Vowels = len(re.findall(r'[аеёиоыэюя]',Abaza))
					string = string[len(Abaza):]
					StressedSyllable = len(re.findall(r'[аеёиоыэюя]',re.findall(r'[а-яёI\-]+',string)[0]))
					Foc =''
					Vow1st = ''
					Vow2nd = '' 
					FirstCons = ''
					LastCons = ''
					if Vowels == 2:
						Foc = re.search(r'[аеёиоыэюя](.*?)[аеёиоыэюя]',Abaza).group(1)
						vows = re.findall(r'[аеёиоыэюя]',Abaza)
						Vow1st = vows[0]
						Vow2nd = vows[1]
						if Abaza[0] not in vows:
							FirstCons = Abaza[0]
						if Abaza[-1] not in vows:
							LastCons = Abaza[-1]
					Consonants = []
					for letter in splitabazacons(Abaza):
						Consonants.append(letter)
						Consonants.append(consdata(letter))
					output = [Abaza,Russian,Levinstein,Vowels,StressedSyllable,Foc,Vow1st,Vow2nd,FirstCons,LastCons]
					output = output + Consonants
					output = [str(elem) for elem in output]
					output = ','.join(output)
					o.write(output+'\n')
				except Exception as E:
					e.write(line)
					print('CAUGHT:',str(E))
	d.close()
	print('Done.')
	return 1

process()