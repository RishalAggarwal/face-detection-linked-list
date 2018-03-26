class node:
	def __init__(self, data=None):
		self.data = data
		self.next = None
		self.cflag = 0


class Linked_List:
	def __init__(self):
		self.head = node()

	def create_cycle(self, data, data_of_next):			#method to create the loop, data_of_next is required to know 
		new_node = node(data)					#which node to loop back to
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_node
		cur = self.head
		while cur.next != None:
			cur = cur.next
			if cur.data == data_of_next:
				new_node.next = cur
				return
		if cur.next == None:
			print('Node not in list')

	def locate_cycle(self):						#locating the node where the cycle has been joined
		cur = self.head
		while cur.next != None:
			if cur.cflag != 1:
				cur.cflag = 1
				cur = cur.next
			else:
				break
		cur1=self.head
		while cur1.next !=None and cur1.cflag==1:
			cur1.cflag=0
			cur1=cur1.next

		if cur.next == None:
			return node(-1)					#assuming all valid nodes are given positive integers for their 
		else:							#data, this can be used to check if the linked list has a loop 
			return cur					#as -1 is passed as the data of the node which is returned by 
									#the function
									
	def display_cycle(self):					#displaying the cycle

		cur=Linked_List.locate_cycle(self)
		if cur.data==-1:
			print 'No loop in cycle'
		else:
			data=cur.data
			elems=[]
			elems.append(data)
			cur=cur.next
			while cur.data!=data:
				elems.append(cur.data)
				cur=cur.next
			elems.append(data)
			print elems

	def append(self, data):
		new_node = node(data)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_node

	def loop_length(self):				#number of nodes in the cycle
		cur = Linked_List.locate_cycle(self)
		if cur.data == -1:
			return 'No loop in cycle'
		else:
			data = cur.data
			total=1
			cur = cur.next
			while cur.data != data:
				total+=1
				cur = cur.next
			return total


	def length(self):				#total number of nodes in the linked list
		cur = self.head
		loop = Linked_List.locate_cycle(self)
		if loop.data == -1:
			total = 0
		else:
			total= Linked_List.loop_length(self)-1
		while cur.next!=None and cur.data!=loop.data:
			total += 1
			cur = cur.next

		return total

	def display(self):
		elems = []
		cur_node = self.head
		while cur_node.next != None:
			cur_node = cur_node.next
			if cur_node.data in elems:
				break
			elems.append(cur_node.data)
		print(elems)

	def remove(self, data):
		cur_node = self.head
		while cur_node.next != None:
			last_node = cur_node
			cur_node = cur_node.next
			if cur_node.data == data:
				last_node.next = cur_node.next
				break

	def insert(self, data, data_of_prev):			#inserting node at a certain location. Data of prev is the data of the 
		cur_node=self.head				#node after whic a certain node has to be inserted
		while True:
			cur_node=cur_node.next
			if cur_node.data == data_of_prev:
				new_node = node(data)
				new_node.next = cur_node.next
				cur_node.next = new_node
				return



my_list = Linked_List()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)						#[1,2,3,4]
my_list.display()
my_list.insert(7,3)						#[1,2,3,7,4]
my_list.display()
my_list.remove(3)						#[1,2,7,4]
my_list.display()
my_list.create_cycle(5,2)					#[1,2,7,4,5,2]
my_list.display()						#this will display [1,2,7,4,5]
my_list.display_cycle()						#this will display [2,7,4,5,2]
print my_list.length()						#5
print my_list.loop_length()					#4
