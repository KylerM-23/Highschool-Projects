import math as m

def calcdis(t1,t2,l1,l2):
	t1 = m.radians(t1)
	t2 = m.radians(t2)
	l1 = m.radians(l1)
	l2 = m.radians(l2)

	d = m.acos(m.sin(t1)*m.sin(t2) + m.cos(t1)*m.cos(t2)*m.cos(l2-l1)) * 3959
	
	return d


