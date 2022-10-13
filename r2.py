def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	allen_word_count = 0
	allen_stiker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_stiker_count = 0
	viki_iamge_count = 0
	for line in lines:
		s = line.split(" ")
		time = s[0]
		name = s[1]
		if "Allen" == name:
			if s[2] == "貼圖":
				allen_stiker_count += 1
			elif s[2] == "圖片":
				allen_image_count += 1
			else:
				for w in s[2:]:
					allen_word_count += 1

		elif "Viki" == name:
			if s[2] == "貼圖":
				viki_stiker_count += 1
			elif s[2] == "圖片:"
				viki_iamge_count += 1
			else:
				for w in s[2:]:
					viki_word_count += 1
			

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)


main()