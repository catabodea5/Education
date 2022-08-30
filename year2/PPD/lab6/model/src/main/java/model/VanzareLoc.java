package model;

import java.io.Serializable;

public class VanzareLoc implements Serializable {
    private int id_vanzare;
    private int nr_loc;

    public VanzareLoc() {}

    public int getId_vanzare() {
        return id_vanzare;
    }

    public void setId_vanzare(int id_vanzare) {
        this.id_vanzare = id_vanzare;
    }

    public int getNr_loc() {
        return nr_loc;
    }

    public void setNr_loc(int nr_loc) {
        this.nr_loc = nr_loc;
    }
}
