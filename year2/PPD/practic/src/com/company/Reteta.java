package com.company;

import java.util.List;

public class Reteta {
    private int cod;
    private int nr_medicamente;
    public List<Integer> medicamente;

    public Reteta(int cod, int nr_medicamente, List<Integer> medicamente) {
        this.cod = cod;
        this.nr_medicamente = nr_medicamente;
        this.medicamente = medicamente;
    }

    @Override
    public String toString() {
        return "Reteta{" +
                "cod=" + cod +
                ", nr_medicamente=" + nr_medicamente +
                ", medicamente=" + medicamente +
                '}';
    }
}
