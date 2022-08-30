package com.company;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Queue {
    private int size;
    private List<Integer> preturi;
    private List<Reteta> retete;
    private List<Medicament> medicamente = addMedicamente();
    private Map<Reteta, Integer> reteta_de_afisat = new HashMap<>();
    public Reteta reteta = null;

    private List<Medicament> addMedicamente() throws FileNotFoundException {
        List<Medicament> meds = new ArrayList<>();
        File myObj = new File("D:\\Facultate\\An3\\PPD\\practic\\src\\com\\company\\Medicamente.txt");
        Scanner myReader = new Scanner(myObj);
        int i=0;
        while (i < 30) {
            String data = myReader.nextLine();
            meds.add(new Medicament(i+1,Integer.parseInt(data)));
            i++;
        }
        myReader.close();
        return meds;

    }



    public Queue(int size) throws FileNotFoundException {
        this.size =size;
        retete = new ArrayList<>();
        preturi = new ArrayList<>();
    }

    public synchronized void addReteta(Reteta o) {
        if(o == null ){
            this.reteta = null;
            notifyAll();
            return;
        }
        retete.add(o);
        int pret = 0;
        for (int i =0; i<o.medicamente.size(); i++){
            pret += o.medicamente.get(i);
        }
        preturi.add(pret);
        this.reteta = o;
        notifyAll();
    }
    public synchronized Reteta afiseazaReteta() throws InterruptedException {
        while (reteta == null && size > retete.size()){
            wait();
        }
        notifyAll();
        return reteta;
    }
}
