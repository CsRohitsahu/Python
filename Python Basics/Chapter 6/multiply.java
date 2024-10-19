import java.util.Scanner;
class Main{
    static Scanner sc=new Scanner(System.in);
    
    public static  void multiplication() {
        System.out.println("Enter no. of rows in matrix 1 ");
       int  row = sc.nextInt();
        System.out.println("Enter no. of column in matrix 1");
       int  col = sc.nextInt();
        System.out.println("Enter no. of row in matrix 2 :");
       int  row1 = sc.nextInt();
        System.out.println("Enter no. of column in matrix 2:");
       int  col1 = sc.nextInt();
       float[][]  mt1 = new float[row][col];
       float mt2[][] = new float[row1][col1];
        float mt3[][] = new float[row][col1];
        if (col == row1) {
            System.out.println("Enter element in first matrix :");
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < col; j++) {
                    mt1[i][j] = sc.nextFloat();
                }
            }
            System.out.println("Enter element in second matrix :");
            for (int i = 0; i < row1; i++) {
                for (int j = 0; j < col1; j++) {
                    mt2[i][j] = sc.nextFloat();

                }
            }
            System.out.println("Entered element in matrix 1 is:");
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < col; j++) {
                    System.out.print(mt1[i][j] + "  ");
                }
                System.out.println();
            }
            System.out.println("Entered element in second matrix is;");
            for (int i = 0; i < row1; i++) {
                for (int j = 0; j < col1; j++) {
                    System.out.print(mt2[i][j] + "  ");
                }
                System.out.println();
            }
            //matrix multiplication code
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < col1; j++) {
                   // mt3[i][j] = 0;
                    for (int k = 0; k < col; k++) {
                        mt3[i][j] += mt1[i][k] * mt2[k][j];
                    }
                }
            }
            System.out.println("matrix multiplication is:");
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < col1; j++) {
                    System.out.print(mt3[i][j] + "  ");
                }
                System.out.println();
            }
        } else
            System.out.println("matrix multiplication is not possible:");
    }
    public static void main(String[] args) {
         multiplication();
        
    }
}