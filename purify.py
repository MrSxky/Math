def purify(x):
  p = []
  for i in x:
    if i%2==0:
      p.append(i)
  return p

print (purify([1,2,3]))