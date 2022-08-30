package model;

import java.io.Serializable;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Vanzare implements Serializable {
    private int id_vanzare;
    private int id_spectacol;
    private LocalDate data_vanzare;
    private int nr_bilete;
    private List<Integer> locuri_vandute;
    private int suma;

    public Vanzare() {
        this.locuri_vandute = new ArrayList<>();
    }

    public int getId_vanzare() {
        return id_vanzare;
    }

    public void setId_vanzare(int id_vanzare) {
        this.id_vanzare = id_vanzare;
    }

    public int getId_spectacol() {
        return id_spectacol;
    }

    public void setId_spectacol(int id_spectacol) {
        this.id_spectacol = id_spectacol;
    }

    public LocalDate getData_vanzare() {
        return data_vanzare;
    }

    public void setData_vanzare(LocalDate data_vanzare) {
        this.data_vanzare = data_vanzare;
    }

    public int getNr_bilete() {
        return nr_bilete;
    }

    public void setNr_bilete(int nr_bilete) {
        this.nr_bilete = nr_bilete;
    }

    public List<Integer> getLocuri_vandute() {
        return locuri_vandute;
    }

    public void setLocuri_vandute(List<Integer> locuri_vandute) {
        this.locuri_vandute = locuri_vandute;
    }

    public int getSuma() {
        return suma;
    }

    public void setSuma(int suma) {
        this.suma = suma;
    }

    @Override
    public String toString() {
        return "Vanzare{" +
                "id_vanzare=" + id_vanzare +
                ", id_spectacol=" + id_spectacol +
                ", data_vanzare=" + data_vanzare +
                ", nr_bilete=" + nr_bilete +
                ", locuri_vandute=" + locuri_vandute.size() +
                '}';
    }
}
