s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s))

# Here Python consider 20 as 20.0 equel for numerically so that it is store only 20 one time.
