package com.company;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Main {
    private static List<Reteta> retete = new ArrayList<>();
    private static Queue coada_retete ;
    private static int p = 5;
    private static int n = 100;

    public static void main(String[] args) throws InterruptedException, FileNotFoundException {
        Farmacist[] threaduri= new Farmacist[p];

	    genereazaCursanti(n);

	    coada_retete = new Queue(retete.size());
	    
	    initializeazaFarmacisti(threaduri);

	    Casier casier = new Casier(coada_retete);
        long startTime, endTime;

        startTime = System.nanoTime();
        for(int i =0 ; i<p; i++){
            threaduri[i].start();
        }
        casier.start();

        for(int i =0 ; i<p; i++){
            threaduri[i].join();
        }
        casier.join();

        endTime = System.nanoTime();
        System.out.println((double)(endTime - startTime)/1E6);

    }

    private static void initializeazaFarmacisti(Farmacist[] threaduri) {
        int cat= n/p;
        int rest= n%p;
        int start,end;
        start=0;
        for(int i=0; i<p; i++) {
            if (rest != 0) {
                end = start + cat + 1;
                rest--;
            } else {
                end = start + cat;
            }
            threaduri[i] = new Farmacist(retete, coada_retete, start, end);
            start = end;
        }
    }

    private static void genereazaCursanti(int max) {
        Random random = new Random();
        for (int i = 0; i<max; i++){
            int nr_med = random.nextInt(5)+1;
            List<Integer> coduri = generateCodes(nr_med);
            retete.add(new Reteta(random.nextInt(), nr_med, coduri));
        }
    }

    private static List<Integer> generateCodes(int nr_med) {
        List<Integer> a = new ArrayList<>();
        Random random = new Random();
        for (int i =0; i<nr_med; i++){
            a.add(random.nextInt(30)+1);
        }
        return a;
    }
}
