package com.company;

import java.util.ArrayList;
import java.util.List;

public class Paralel {
    private final Polinom rezultatPolinom;
    private final MyQueue coada;
    private final int n;
    private final int p;
    private final String folderPath;

    public Paralel(int n, int p, String folderPath) {
        this.rezultatPolinom = new Polinom();
        this.coada = new MyQueue(n);
        this.n = n;
        this.p = p;
        this.folderPath = folderPath;
    }

    public void calculatePolinom() throws InterruptedException {
        List<MyThread> threads = new ArrayList<>(p);
        for(int i=1; i < p; i++) {
            MyThread thread = new MyThread(coada, rezultatPolinom);
            threads.add(thread);
        }

        Thread threadForReading = new Thread(() -> {
            for(int i=1; i <= n; i++) {
                String filename = folderPath + "polinom" + i + ".txt";
                try {
                    coada.add(new Polinom(filename));
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            try {
                coada.add(null);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        threadForReading.start();
        for(Thread t : threads)
            t.start();

        threadForReading.join();
        for(Thread t : threads) {
            t.join();
        }
    }

    public void writeToFile() {
        rezultatPolinom.writeToFile(folderPath + "result_paralel.txt");
    }
}
