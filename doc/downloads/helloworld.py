import matplotlib.pyplot as plt
from pyddm import Model
m = Model()
s = m.solve()
plt.plot(s.model.t_domain(), s.pdf_corr())
plt.savefig("helloworld.png")
plt.show()
