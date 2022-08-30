package com.company;


class MyThread extends Thread {
        private final MyQueue coada;
        private final Polinom polinomRezultat;

        public MyThread(MyQueue queue, Polinom polinomRezultat) {
            this.coada = queue;
            this.polinomRezultat = polinomRezultat;
        }

        @Override
        public void run() {
            while(true) {
                Polinom polinomCurent = new Polinom();
                synchronized (coada) {
                    //verific daca coada e goala. in caz afirmativ adaug un element nul
                    try {
                        polinomCurent = coada.delete();
                        if (polinomCurent == null) {
                            coada.add(null);
                            coada.notifyAll();
                            return;
                        }
                    } catch (InterruptedException ex) {
                        System.out.println(ex.getMessage());
                    }
                }

                synchronized (polinomRezultat) {
                    for(Monom monom : polinomCurent.getPolinomList()) {
                        polinomRezultat.setMonom(monom);
                    }
                }
            }
        }
    }

