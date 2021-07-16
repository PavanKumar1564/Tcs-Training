class solution():
	def rotateRight(self,head,k):
		if not head or not head.next:
			return head

		cur=head
		n=1
		while cur.next:
			n+=1
			cur=cur.next
		cur.next = head
		m = n-k%n

		i=0
		cur=head
		while i < m:
			prev=cur
			cur=cur.next
			i+=1

		prev.next=None
		head=cur

		return head
