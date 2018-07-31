from note import Note

class Notebook:
	def __init__(self, filename):
		self.notes = []
		self.filename = filename

	def __str__(self):
		result = ''
		for index, note in enumerate(self.notes, start = 1):
			result += str(index) + '. ' + str(note) + '\n'
		return result

	def add_note(self, content, category):
		self.notes.append(Note(content, category))
	
	def save(self):
		fout = open(self.filename, 'w')
		for note in self.notes:
			fout.write(str(note))
			fout.write('\n')
		fout.close()
	
	def load(self):
		fin = open(self.filename)
		line = fin.readline()
		while line:
			record = line.strip().replace(')','').split(" (")
			self.add_note(record[0], record[1])
			line = fin.readline()

	def delete_by_note_number(self, num):
		del self.notes[num-1]	

	def delete_by_keyword(self, key):
		self.notes = list(filter(lambda note: not note.match_content(key) ,self.notes))
		

if __name__ == '__main__':
	notebook = Notebook('notebook.txt')
#	notebook.add_note('Drink  lot of water', 'health')
#	notebook.add_note('Exercise regularly', 'health')
#	notebook.add_note('Do not talk to strangers', 'safety')
#	notebook.add_note('Always say "thank you"', 'social')

#	notebook.save()
	notebook.load()
	
	print('Original notebook:')
	print(notebook)
	
	print('Delete the 2nd note:')
	notebook.delete_by_note_number(2)
	print(notebook)
	
	print('Delete notes that contains the keyword: "you"')
	notebook.delete_by_keyword('you')
	print(notebook)
