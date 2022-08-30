package com.company;

public class Secvential {
    private final Polinom polinomRezultat;
    private final int n;
    private final String baseDataPath;

    public Secvential(int n, String baseDataPath) {
        this.polinomRezultat = new Polinom();
        this.n = n;
        this.baseDataPath = baseDataPath;
    }

    public void calculatePolinom() {
        for(int i=1; i <= n; i++) {
            String filename = baseDataPath + "polinom" + i + ".txt";
            Polinom polinom = new Polinom(filename);

            for(Monom monom : polinom.getPolinomList()) {
                polinomRezultat.setMonom(monom);
            }
        }
    }

    public void writeToFile() {
        polinomRezultat.writeToFile(baseDataPath + "result_secvential.txt");
    }
}
