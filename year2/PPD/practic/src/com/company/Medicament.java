package com.company;

public class Medicament {
    public int getCod_medicament() {
        return cod_medicament;
    }

    public void setCod_medicament(int cod_medicament) {
        this.cod_medicament = cod_medicament;
    }

    public int getPret() {
        return pret;
    }

    public void setPret(int pret) {
        this.pret = pret;
    }

    private int cod_medicament;
    private int pret;

    public Medicament(int cod_medicament, int pret) {
        this.cod_medicament = cod_medicament;
        this.pret = pret;
    }

    @Override
    public String toString() {
        return "Medicament{" +
                "cod_medicament=" + cod_medicament +
                ", pret=" + pret +
                '}';
    }
}
