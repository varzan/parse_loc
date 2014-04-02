import urllib
import sys

def load_loc(version):
	LOC_URL = 'http://dexonline.ro/scrabble-loc?locVersion={}'
	return urllib.urlopen(LOC_URL.format(version)).read()

def get_words(loc_str):
	words = [line.split()[0] for line in loc_str.strip().split('\n')]
	words = [word.replace("'", "") for word in words]
	words = [word.decode('utf-8') for word in words]
	return words
	
def filter_words(words, min_len=0, max_len=0):
	filtered_words = []
	for word in words:
		l = len(word)
		if min_len > 0 and l < min_len:
			continue
		if max_len > 0 and l > max_len:
			continue
		filtered_words.append(word)
	return filtered_words

def main():
	nargs = len(sys.argv) - 1
	if nargs == 0:
		print "Usage: {} OUTFILE MINWORDLEN MAXWORDLEN LOCVERSION"
		sys.exit(0)
	
	outfile = sys.argv[1]
	min_len = int(sys.argv[2]) if nargs >= 2 else 0
	max_len = int(sys.argv[3]) if nargs >= 3 else 0
	loc_version = sys.argv[4] if nargs >= 4 else '5.0'

	with open(outfile, 'w') as f:
		words = get_words(load_loc(loc_version))
		f.write('\n'.join(filter_words(words, min_len, max_len)).encode('utf-8'))

if __name__ == '__main__':
	main()
