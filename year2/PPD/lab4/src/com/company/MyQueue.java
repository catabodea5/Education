package com.company;

import java.util.LinkedList;

public class MyQueue {
    private final LinkedList<Polinom> queueList;
    private final int n;
    private int queueSize;


    public MyQueue(int n) {
        this.n = n;
        this.queueSize = 0;
        this.queueList = new LinkedList<>();
    }

    synchronized public void add(Polinom polinom) throws InterruptedException {
        // asigur nedepasirea dimensiunii maxime
        while(queueSize == n) {
            this.wait();
        }

        queueList.add(polinom);
        ++queueSize;
        this.notifyAll();
    }

    synchronized public Polinom delete() throws InterruptedException {
        //ma asigur ca coada nu va fi nula
        while(queueSize == 0) {
            this.wait();
        }

        --queueSize;
        Polinom polinom = queueList.get(0);
        queueList.remove(0);
        this.notifyAll();
        return polinom;
    }
}
