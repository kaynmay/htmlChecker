#create stack class
class Stack(object):

	#initialize the stack
	def __init__(self):
		self.items = []

	#method to push items onto the stack
	def push(self, item):
		self.items.append(item)

	#method to pop items off of the stack
	def pop(self):
		return self.items.pop()

	#method to peek at the top of the stack
	def peek(self):
		return self.items[-1]

	#method to check if the stack is empty
	def isEmpty(self):
		return self.items == []

	#method to return the size of the stack
	def size(self):
		return len(self.items)

#global tag list
tagList = []

#function to get tags
def getTag(string):
	
	#go through the string one character at a time
	i = 0
	while i < len(string):
		#if the character isn't the start of a tag do nothing
		if string[i] != '<':
			i += 1
			None
		#if the character is the start of a tag..
		else: 
			#create a newstring for tag
			newString = ''
			for j in range(1, len(string[i+1:])):
				#go through string and find where the end of the tag is
				if string[i+j] == ('>') or string[i+j] == ' ':
					#append newstring to tag list
					tagList.append(newString)
					i += j
					break
				else:
					#if the character isn't the end of the tag add it to newstring
					newString += string[i+j]

def main():

	#open file "htmlfile.txt" for reading
	file = open ('htmlfile.txt', 'r')

	#get all the tags into a list
	for line in file:
		getTag(line)

	#create an exceptions list
	exceptions = ['meta', 'br'] 

	#create a new stack
	stack = Stack()

	#print out tag list
	print(tagList)

	#iterate through tag list
	for item in tagList:
		#if item is in the exception list do not add it to stack
		if item in exceptions:
			print('Tag is', item, ': does not need to match: stack is now', stack.items)
		#if tag is a start tag add it to the stack
		elif item[0] != '/':
			stack.push(item)
			print('Tag is', item, ': pushed: stack is now', stack.items)
		else:
			#if tag is an end tag check if it matches top of stack
			if item[1:] == stack.items[-1]:
				stack.pop()
				print('Tag is', item, ': matches: stack is now', stack.items)
			#if end tag does not match top of stack print out an error message
			else:
				print('Error: tag is', item, 'but top of stack is', stack.items[-1])
				quit()

	#if stack is empty / not empty after processing print out appropriate message
	if stack.isEmpty():
		print('Processing complete. No mismatches found.')
	else:
		print('Processing complete. Unmatched tags remain on stack:', stack.items)

main()
