public class Main {
    public static void Main(String[] args){
        double[] a,b,c;
        int n=20;
        a= new double[n];
        b= new double[n];
        c= new double[n];
        for(int i=0; i<n; i++){
            a[i]=i;
            b[i]=n-i;
        }
        System.nanoTime();
        suma(a,b,n,c);
        System.nanoTime();
    }

    public static void suma(double[]a, double[]b, int n, double[]c){
        for(int i=0; i<n; i++){
            c[i]=a[i]+b[i];
        }
    }
    public static void  printVector(double[] v, int n){
        for (int i=0; i<n; i++){
            System.out.println(v[i]+" ");
        }
        System.out.println();
    }
}
