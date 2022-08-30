package com.company;

import java.io.FileWriter;
import java.io.IOException;

public class Casier extends Thread {
    private Queue retete;

    public Casier(Queue retete) {
        this.retete = retete;
    }
    public void run(){
        try {

            FileWriter myWriter = new FileWriter("D:\\Facultate\\An3\\PPD\\practic\\src\\com\\company\\Retete.txt");
            Reteta reteta;
            reteta = retete.afiseazaReteta();
            while (reteta != null){

                myWriter.write(reteta.toString());
                reteta = retete.afiseazaReteta();
                retete.reteta = null;
            }
            myWriter.close();

        } catch (InterruptedException | IOException e) {
            e.printStackTrace();
        }

    }

}
