#make alphabetized version of CatLLex and check for duplicates.

CATLEXLOC = "CatLLex"

o = open(CATLEXLOC)

lines = [(ln+'$').split('$')[0].strip() for ln in o.readlines()]
o.close()

lines = [ln for ln in lines if ln != ''] 
lines = sorted(lines)

o = open("CatLLex_alphasorted.txt",mode='w')

for i in range(len(lines)-1):
	o.write(lines[i] + "\n")
	if lines[i] == lines[i+1]:
		print("duplicate line at alphabetically sorted line number "+str(i)+": "+lines[i])
o.write(lines[-1]+"\n")
o.close()
