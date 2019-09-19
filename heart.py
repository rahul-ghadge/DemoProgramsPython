
#num = int(input("Enter number > 5 to print Heart :"))

num = 6

for row in range(num):
    for col in range(num+1):
        if (row==0 and col%3 !=0) or (row == 1 and col % 3 ==0) or ((row-col)==2) or (row+col==8):
            print("* ", end="")
        else:
            print("  ", end="")
    else:
        print()
   
# Output :   
#  * *   * *   
#*     *     * 
#*           * 
#  *       *   
#    *   *     
#      *   
