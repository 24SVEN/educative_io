def flip_and_invert_image(matrix):
    #TODO: Write your code here.

    #first flip
    for li in matrix:
        li.reverse()
        for i in range(len(li)):
            if li[i] == 1:
                li[i] = 0
            else:
                li[i] = 1

    return matrix


def main():
  print(flip_and_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
  #print(flip_and_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

main()