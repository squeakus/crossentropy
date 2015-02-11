import random
import numpy as np

def main():
    # axes: cols = 0, rows = 1
    x = np.array([[0, 0, 0, 0],
                  [1, 1, 1, 1], 
                  [2, 2, 2, 2], 
                  [3, 3, 3, 3], 
                  [4, 4, 4, 4], 
                  [5, 5, 5, 5]])
    
    # find mean,std for each column
    mean = np.mean(x,0)
    std = np.std(x,0)
    print np.std([0,1,2,3,4,5,6,7,8,9])
    print "mean", mean, "+-", std

    newindiv = []
    for idx, val in enumerate(mean):
	print "mu", mean[idx], "+-", std[idx]
        newindiv.append(int(round(random.gauss(mean[idx], std[idx]))))
    print np.array(newindiv)

if __name__=='__main__':
    main()


