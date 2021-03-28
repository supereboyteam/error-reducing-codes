import itertools
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def error_generator(H,G):
        Map = {}

        for i in range(16):

                C = np.array([int(x) for x in list('{0:04b}'.format(i))])

                GT = np.transpose(G)

                Codeword = np.dot(GT,C)%2
                num = 0
                poww = 1
                for j in Codeword:
                        num = num + j*poww
                        poww = poww*2
                Map[num] = C

        errors = 0

        for i in range(16):

                C = np.array([int(x) for x in list('{0:04b}'.format(i))])

                GT = np.transpose(G)

                Codeword = np.dot(GT,C)%2


                perm = 0

                lis = list(set(list(itertools.permutations([1,1,0,0,0,0,0]))))

                for listt in lis:
                        e = np.array([int(x) for x in listt])
                        perm = perm + 1

                        Transmitted = (e + Codeword)%2

                        decode = np.dot(H,Transmitted)%2

                        val = -1
                        HT = np.transpose(H)
                        for i in range(HT.shape[0]):
                                if (HT[i][0:] == decode).all():
                                        val = i
                                        break

                        if(val != -1):
                                Transmitted[val] = (Transmitted[val]+1)%2

                        decode = np.dot(H,Transmitted)%2

                        num = 0
                        poww = 1

                        for j in Transmitted:
                                num = num + j*poww
                                poww = poww*2
                        if (Map[num] == C).all():
                                errors = errors
                        else:
                                errors += np.sum(C != Map[num])


        return errors / (16 * perm)



G1 = np.array([[1,1,1,0,0,0,0],
               [0,1,1,1,1,0,0],
               [0,1,0,1,0,1,0],
               [0,0,1,1,0,0,1]])

G = np.array([[1,1,1,0,0,0,0],
              [1,0,0,1,1,0,0],
              [0,1,0,1,0,1,0],
              [0,0,1,1,0,0,1]])

H = np.array([[0,0,0,1,1,1,1],
              [0,1,1,0,0,1,1],
              [1,0,1,0,1,0,1]])


objects = ('Standard Decoding', 'Optimized Standard Decoding')
y_pos = np.arange(len(objects))

GH = error_generator(H,G)
GH1 = error_generator(H,G1)


performance = [GH,GH1]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Average Error')
plt.title('Comparison for two bit error')

plt.show()

