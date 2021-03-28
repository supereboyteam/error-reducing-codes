import numpy as np
from pyldpc import make_ldpc, encode, decode, get_message
n = 100
d_v = 2
d_c = 4
snr = 20
H, G = make_ldpc(n, d_v, d_c, systematic=False, sparse=True)
print(H)
print(G)
k = G.shape[1]
print(k)
v = np.random.randint(2, size=k)
print(v)
import time
start_time = time.time()
y = encode(G, v, snr)
print(y)
d = decode(H, y, snr)
print("--- %s seconds ---" % (time.time() - start_time))
print(d)
x = get_message(G, d)
print(x)
assert abs(x - v).sum() == 0
