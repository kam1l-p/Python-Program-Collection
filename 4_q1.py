mochiko = float(input("Enter an amount (g) of mochiko: "))
sugar = float(input("Enter an amount (g) of sugar: "))
cornstarch = float(input("Enter an amount (g) of cornstarch: "))
anko = float(input("Enter an amount (g) of anko: "))

mcups = mochiko / 220
scups = sugar / 220
ccups = cornstarch / 220
acups = anko / 220

m_batch = mcups // 3
s_batch = scups // 1.5
c_batch = ccups // 2
a_batch = acups // 1

batches = int(m_batch)

if s_batch < batches:
    batches = int(s_batch)
if c_batch < batches:
    batches = int(c_batch)
if a_batch < batches:
    batches = int(a_batch)
    
print("With this amount of ingredients, you can make", batches, "batch(es) of 24 mochi.")