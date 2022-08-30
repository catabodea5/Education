package com.company;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.util.Arrays;
import java.util.Random;

public class Main {

private static final String folderPath = "D:\\Facultate\\An3\\PPD\\lab4\\src\\com\\company\\zecepolinoame\\";
    private static final int n = 5;   // numarul de polinoame
    private static final int p = 6;   // numarul de threaduri
    private static final int coeficientMaxim = 10000;

    public static void main(String[] args) throws InterruptedException, IOException {
        long startTime, endTime;
        //createFiles();

        Secvential secvential = new Secvential(n, folderPath);
        startTime = System.nanoTime();
        secvential.calculatePolinom();
        endTime = System.nanoTime();

        System.out.println((double)(endTime - startTime)/1E6);
        secvential.writeToFile();

        Paralel paralel = new Paralel(n, p, folderPath);
        startTime = System.nanoTime();
        paralel.calculatePolinom();
        endTime = System.nanoTime();

        System.out.println((double)(endTime - startTime)/1E6);
        paralel.writeToFile();

        try {
            boolean filesAreEqual = checkFiles(folderPath + "result_secvential.txt", folderPath + "result_paralel.txt");
            System.out.println("Equal files " + filesAreEqual);
        }
        catch(java.io.IOException ex) {
            System.out.println(ex.getMessage());
        }
    }

    public static void createFiles() {
        int coeficient, monom;
        Random random = new Random();
        int nrMonoame = random.nextInt(500);

        //generam cate un fisier pentru fiecare polinom
        for(int i=1; i <= n; i++) {
            try {
                File file = new File(folderPath + "polinom" + i + ".txt");
                boolean created = file.createNewFile();
                if(created) {
                    FileWriter writer = new FileWriter(folderPath + "polinom" + i + ".txt");

                    for(int j=0; j<nrMonoame; j++) {
                        //verific sa nu aiba coeficientul 0
                        coeficient = random.nextInt(coeficientMaxim - 1) + 1;
                        monom = random.nextInt(5000);

                        writer.write(coeficient + " " + monom + "\n");
                    }

                    writer.close();
                }

            } catch (IOException e) {
                System.out.println("An error occurred.");
                e.printStackTrace();
            }
        }
    }

    public static boolean checkFiles(String filename1, String filename2) throws IOException {
        File f1 = new File(filename1);
        File f2 = new File(filename2);
        byte[] b1 = Files.readAllBytes(f1.toPath());
        byte[] b2 = Files.readAllBytes(f2.toPath());
        return Arrays.equals(b1, b2);
    }
}
