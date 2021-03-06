# coding: utf-8
import argparse, sys, os, time, re, codecs, random

def split(filename, args):
	path = args.input_dir + "/" + filename
	filename_without_ext = filename.split(".")[0]
	print filename_without_ext
	sentences = []
	with codecs.open(path, "r", "utf-8") as f:
		for s in f:
			sentences.append(s)
	num_per_file = len(sentences) // args.split
	sentences = [sentences[i * num_per_file:(i + 1) * num_per_file] for i in range(args.split)]
	for i, dataset in enumerate(sentences):
		with codecs.open("{}/{}_{}.txt".format(args.output_dir, filename_without_ext, i), "w", "utf-8") as f:
			for sentence in dataset:
				f.write(sentence)

def main(args):
	try:
		os.mkdir(args.output_dir)
	except:
		pass
	assert args.input_dir is not None
	assert os.path.exists(args.input_dir)
	assert args.split > 0
	for filename in os.listdir(args.input_dir):
		if re.search(r".txt$", filename):
			split(filename, args)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--input-dir", type=str, default=None)
	parser.add_argument("-o", "--output-dir", type=str, default=None)
	parser.add_argument("-s", "--split", type=int, default=10)
	main(parser.parse_args())