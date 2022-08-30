package com.company;

import java.util.List;

public class Farmacist extends Thread{
    private List<Reteta> retete;
    private Queue coada_retete;
    private int start;
    private int end;
    public Farmacist(List<Reteta> retete, Queue coada_retete, int start, int end) {
        this.retete= retete;
        this.coada_retete =coada_retete;
        this.end=end;
        this.start= start;
    }

    public void run(){
        for(int i=start; i< end; i++){
            this.coada_retete.addReteta(retete.get(i));
        }

        coada_retete.addReteta(null);
    }
}
