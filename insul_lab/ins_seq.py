with open("ins-seq.txt") as f:
	data = f.read()
print(data)

del_chars = ["ORIGIN", "1", "6", "//", " ", "\n"]
for i in del_chars:
	data = data.replace(i, "")
print(data)
print(len(data))
with open("preproinsulin-seq-clean.txt", "w") as f:
	f.write(data)
with open("lsinsulin-seq-clean.txt", 'w') as f:
	f.write(data[0:24])
with open("binsulin-seq-clean.txt", "w") as f:
	f.write(data[24:54])
with open("cinsulin-seq-clean.txt", "w") as f:
	f.write(data[54:89])
with open("ainsulin-seq-clean.txt", "w") as f:
	f.write(data[89:110])
