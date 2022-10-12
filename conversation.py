def read_file(filename):
	lines = []
	with open(filename, "r", encoding="utf-8") as f:
		for line in f:
			lines.append(line)
	return lines

def conver(lines):
	for c in f:
		if "Allen" in c:
			name = c.strip("\ufeff").strip()
		elif "Tom" in c:
			name = c.strip()
		else:
			conver = c.strip()
			lines.append([name,conver])
	return lines

def write_file(filename,lines):
	with open(filename, "w", encoding="utf-8") as f:
		for w in lines:
			f.write(w[0] + ":" + " " + w[1] + "\n")

def main():
	lines = read_file("input.txt")
	lines = conver(lines)
	write_file("output.txt",lines)
