import os.path
import random

class DB():

	def __init__(self):
		self.doc_name_path = None
		self.root = os.path.abspath('./') 
		self.word = []
		self.trans = []
		self.random_number = 0

	def set_path(self,path):
		self.doc_name_path= path
		return 0

	def init_words(self):
		# current_doc_name = self.root + "\\data\\" + str(self.doc_pointer) + ".txt"
		current_doc_name = self.doc_name_path

		f = open(current_doc_name,"r",encoding='utf-8')
		lines = f.readlines()
		f.close()

		for line in lines:
			line = line.strip("\n")
			line = line.split("-")
			self.word.append(line[0])
			self.trans.append(line[1])
		return self.word,self.trans

	def write_in(self,in_word,in_trans):
		current_doc_name = self.doc_name_path
		# current_doc_name = self.root + "\\data\\" + str(self.doc_pointer) + ".txt"

		f = open(current_doc_name,"a+",encoding='utf-8')
		f.write("\n"+in_word + '-'+in_trans)
		f.close()

		return 0

	def random_pick(self):
		r_index = random.randint(0,len(self.word)-1)
		self.random_number = r_index
		return self.word[r_index],self.trans[r_index]

