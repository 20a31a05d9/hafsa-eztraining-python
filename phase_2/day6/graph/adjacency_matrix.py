#o/p not getting 

class graph(object):
    #initialise the matrix
    def __init__(self,size):
        self.adjmatrix=[]
        for i in range(size):
            self.adjmatrix.append([ 0 for i in range(size)]) # to initialise with 0 all elements in a matrix
        self.size=size 

    def add_edge(self,v1,v2):
        if v1==v2:
            print("same vertex %d and %d " %(v1,v2))
            self.adjmatrix[v1][v2]=1
            self.adjmatrix[v2][v1]=1

    def remove_edge(self,v1,v2):   #not needed
        if self.adjmatrix[v1][v2]==0:
            print('no edge btw %d and %d' %(v1,v2))
            return
        self.adjmatrix[v1][v2]=0
        self.adjmatrix[v2][v1]=0

    def __len__(self):       #not needed
        return self.size

    # print the matrix
    def print_matrix(self):
        for row in self.adjmatrix:
            for val in row:
                print('{:4}'.format(val))
            #print
            
def main():
        g=graph(5)
        g.add_edge(0,1)
        g.add_edge(0,2)
        g.add_edge(1,2)
        g.add_edge(2,0)
        g.add_edge(2,3)

        g.print_matrix()

if __name__ == '__main__':
    main()
