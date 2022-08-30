package model;

import java.io.Serializable;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Spectacol implements Serializable {
    private int id_spectacol;
    private LocalDate data_spectacol;
    private String titlu;
    private int pret_bilet;
    private List<Integer> locuri_vandute;
    private int sold;

    public Spectacol() {
        this.locuri_vandute = new ArrayList<>();
    }

    public int getId_spectacol() {
        return id_spectacol;
    }

    public void setId_spectacol(int id_spectacol) {
        this.id_spectacol = id_spectacol;
    }

    public LocalDate getData_spectacol() {
        return data_spectacol;
    }

    public void setData_spectacol(LocalDate data_spectacol) {
        this.data_spectacol = data_spectacol;
    }

    public String getTitlu() {
        return titlu;
    }

    public void setTitlu(String titlu) {
        this.titlu = titlu;
    }

    public int getPret_bilet() {
        return pret_bilet;
    }

    public void setPret_bilet(int pret_bilet) {
        this.pret_bilet = pret_bilet;
    }

    public List<Integer> getLocuri_vandute() {
        return locuri_vandute;
    }

    public void setLocuri_vandute(List<Integer> locuri_vandute) {
        this.locuri_vandute = locuri_vandute;
    }

    public int getSold() {
        return sold;
    }

    public void setSold(int sold) {
        this.sold = sold;
    }
}
