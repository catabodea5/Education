package com.company;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.LinkedList;
import java.util.Scanner;

public class Polinom {
    private final LinkedList<Monom> polinomList;

    public LinkedList<Monom> getPolinomList() {
        return polinomList;
    }

    public Polinom() {
        polinomList = new LinkedList<>();
    }

    public Polinom(String filename) {
        polinomList = new LinkedList<>();

        try {
            Scanner scanner = new Scanner(new FileReader(filename));
            while (scanner.hasNextLine()) {
                String[] monoame = scanner.nextLine().split(" ");
                polinomList.add(new Monom(Integer.parseInt(monoame[0]), Integer.parseInt(monoame[1])));
            }
            scanner.close();

            sortPolinomByCoeficients();
        }
        catch(FileNotFoundException ex) {
            System.out.println("File not found");
        }
    }

    public int getIndexOfCoef(int coef) {
        for(int i = 0; i< polinomList.size(); i++) {
              if(polinomList.get(i).coeficient == coef) {
                return i;
            }
        }
        return -1;
    }

    public void setMonom(Monom monom) {
        int index = getIndexOfCoef(monom.coeficient);
        if(index != -1) {
            Monom temp = polinomList.get(index);
            temp.exponent += monom.exponent;
            polinomList.set(index, temp);
        }
        else {
            polinomList.add(monom);
        }
    }

    public void sortPolinomByCoeficients() {
        for(int i = 0; i < polinomList.size()-1; i++) {
            for(int j = i+1; j < polinomList.size(); j++) {
                if(polinomList.get(i).coeficient > polinomList.get(j).coeficient) {
                    Monom m = polinomList.get(i);
                    polinomList.set(i, polinomList.get(j));
                    polinomList.set(j, m);
                }
            }
        }
    }

    public void writeToFile(String filename) {
        sortPolinomByCoeficients();
        try {
            FileWriter writer = new FileWriter(filename);
            for(Monom monom : polinomList){
                writer.write(monom.coeficient + " " + monom.exponent + '\n');
            }
            writer.close();
        }
        catch( java.io.IOException ex) {
            System.out.println(ex.getMessage());
        }
    }
}
