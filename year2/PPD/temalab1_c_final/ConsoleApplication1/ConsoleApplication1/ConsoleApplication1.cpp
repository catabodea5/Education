
#pragma once
#include <random>
#include <random>
#include <fstream>

#include <iostream>
#include <fstream>
#include <sstream>
#include <chrono>
#include <thread>
#define _CRT_SECURE_NO_DEPRECATE
#pragma warning(disable:4996)
#include <stdio.h>
#include "C:/Users/B0/Downloads/barrier.h"
using namespace std;
using namespace std::chrono;


//read matrix f
void readMatrix(int n, int m, ifstream& reader, int** x) {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			reader >> x[i][j];
}
//make matrix f
void createMatrixF(int N, int M, int n, int m) {

	ofstream fout;
	fout.open("data.txt");
	fout << N << " " << M << " " << endl;
	

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			int valoare = rand() % 255;
			fout << valoare << " ";
		}
		fout << endl;
	}
	fout << n << " " << m << " " << endl;
	fout.close();
}



//writing results in file
void printMatrix(int** matrix, char const* filename, int N, int M) {
	FILE* (file);
	file = fopen(filename, "w");

	fprintf(file, "%d %d\n", N, M);
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			fprintf(file, "%d ", matrix[i][j]);
		}
		fprintf(file, "\n");
	}

	fclose(file);
}
bool equalMatrix(int** matrix1, int** matrix2, int N, int M) {

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++)
			if (matrix1[i][j] != matrix2[i][j])
				return false;
	}

	return true;
}
void modifyMatrixParalel(int** f, int**w, int** rezultat, int N, int M, int n, int m, int start, int end, BarrierMine& barrier) {
	int rezult;
	vector<int> rezultate;
	for (int i = start; i < end; i++)
	{
		for (int j = 0; j < M; j++) {
			rezult = 0;
			for (int a = -n / 2; a <= n / 2; a++)
				for (int b = -m / 2; b <= m / 2; b++) {
					if ((i + a < 0 && j + b < 0) || (i + a < 0 && j + b >= M) || (i + a >= N && j + b < 0) || (i + a >= N && j + b >= M))
						rezult += f[i][j] * w[a + n / 2][b + m / 2];
					else
						if ((i + a < 0 || i + a >= N) && (j + b < M && j + b >= 0))
							rezult += f[i][j + b] * w[a + n / 2][b + m / 2];
						else
							if ((i + a >= 0 && i + a < N) && (j + b < 0 || j + b >= M))
								rezult += f[i + a][j] * w[a + n / 2][b + m / 2];
							else
								rezult += f[i + a][j + b] * w[a + n / 2][b + m / 2];
				}

			rezultate.push_back(rezult);
		}
		
	}
	barrier.wait();
	int index = 0;
	for (int i = start; i < end; i++) {
		for (int j = 0; j < M; j++) {
			f[i][j] = rezultate.at(index++);
		}
	}
}
void modifyMatrixParalel2(int** f, int** w, int** rezultat, int N, int M, int n, int m, int start, int end, BarrierMine& barrier) {
	int suma;
	vector<int> rezultate;
	for (int i = 0; i < N; i++)
	{
		for (int j = start; j < end; j++) {
			suma = 0;
			for (int a = -n / 2; a <= n / 2; a++)
				for (int b = -m / 2; b <= m / 2; b++) {
					if ((i + a < 0 && j + b < 0) || (i + a < 0 && j + b >= M) || (i + a >= N && j + b < 0) || (i + a >= N && j + b >= M))
						suma += f[i][j] * w[a + n / 2][b + m / 2];
					else
						if ((i + a < 0 || i + a >= N) && (j + b < M && j + b >= 0))
							suma += f[i][j + b] * w[a + n / 2][b + m / 2];
						else
							if ((i + a >= 0 && i + a < N) && (j + b < 0 || j + b >= M))
								suma += f[i + a][j] * w[a + n / 2][b + m / 2];
							else
								suma += f[i + a][j + b] * w[a + n / 2][b + m / 2];
				}
			rezultate.push_back(suma);
		}
		
	}
	barrier.wait();
	int index = 0;
	for (int i = 0; i < N; i++) {
		for (int j = start; j < end; j++) {
			f[i][j] = rezultate.at(index++);
		}
	}
}


//complexitate spatiu: O(N*M*n*m)
void modifyMatrixSequential(int** f, int** w, int** r, int N, int M, int n, int m) {
	int suma;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++) {
			suma = 0;
			for (int a = -n / 2; a <= n / 2; a++)
				for (int b = -m / 2; b <= m / 2; b++) {
					if ((i + a < 0 && j + b < 0) || (i + a < 0 && j + b >= M) || (i + a >= N && j + b < 0) || (i + a >= N && j + b >= M))
						suma += f[i][j] * w[a + n / 2][b + m / 2];
					else if ((i + a < 0 || i + a >= N) && (j + b < M && j + b >= 0))
						suma += f[i][j + b] * w[a + n / 2][b + m / 2];
					else if ((i + a >= 0 && i + a < N) && (j + b < 0 || j + b >= M))
						suma += f[i + a][j] * w[a + n / 2][b + m / 2];
					else
						suma += f[i + a][j + b] * w[a + n / 2][b + m / 2];
				}
			r[i][j] = suma;
		}
	

}

//complexitate spatiu: O(p*N*M*n*m)
void modifyParallelDynamic(int** f_dinamic, int** w_dinamic, int** rezultat_dinamic, int N, int M, int n, int m, int p) {
	BarrierMine barrier(p);

	thread* threads = new thread[p];
	int cat = N / p;
	int rest = N % p;
	int start, end;
	start = 0;
	for (int i = 0; i < p; i++) {
		if (rest != 0) {
			end = start + cat + 1;
			rest--;
		}
		else
			end = start + cat;
		
		threads[i] = thread(modifyMatrixParalel, f_dinamic, w_dinamic, rezultat_dinamic, N, M, n, m, start, end, ref(barrier));
		start = end;
	}
	for (int i = 0; i < p; i++)
		threads[i].join();
	delete[] threads;




}

//complexitate spatiu: O(p*N*M*n*m)
void modifyParallelDynamic2(int** f_dinamic, int** w_dinamic, int** rezultat_dinamic, int N, int M, int n, int m, int p) {
	BarrierMine barrier(p);
	thread* threads = new thread[p];
	int cat = M / p;
	int rest = M % p;
	int start, end;
	start = 0;
	for (int i = 0; i < p; i++) {
		if (rest != 0) {
			end = start + cat + 1;
			rest--;
		}
		else
			end = start + cat;

		threads[i] = thread(modifyMatrixParalel2, f_dinamic, w_dinamic, rezultat_dinamic, N, M, n, m, start, end, ref(barrier));
		start = end;
	}
	for (int i = 0; i < p; i++)
		threads[i].join();
	delete[] threads;




}
void setKernel(int** w_dinamic, int n, int m) {

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			w_dinamic[i][j] = j * 2;
		}
	}
}

int main()
{
	ifstream file;
	file.open("data.txt");
	ofstream file1;
	file1.open("rulari_secv.txt");
	ofstream file2;
	file2.open("rulari_paralel.txt");
	int p = 4;
	int M, N, m, n;

	createMatrixF(10, 10, 3, 3);
	
	file >> N >> M;

	int** f_dinamic = new int* [N];
	for (int i = 0; i < N; i++)
		f_dinamic[i] = new int[M];

	int** rezultat_dinamic = new int* [N];
	for (int i = 0; i < N; i++)
		rezultat_dinamic[i] = new int[M];

	int** rezultat2_dinamic = new int* [N];
	for (int i = 0; i < N; i++)
		rezultat2_dinamic[i] = new int[M];

	readMatrix(N, M, file, f_dinamic);
	file >> n >> m;
	int** w_dinamic = new int* [n];
	for (int i = 0; i < n; i++)
		w_dinamic[i] = new int[m];
	

	


	
	//readFromFile(f_dinamic);
	
	setKernel(w_dinamic, n, m);
	
		
		

	float suma = 0;
	float suma2 = 0;
	for (int i = 0; i < 10; i++) {

		auto t1 = steady_clock::now();
		modifyMatrixSequential(f_dinamic, w_dinamic, rezultat_dinamic, N, M, n, m);
		auto t2 = steady_clock::now();
		printMatrix(rezultat_dinamic, "output0.txt", N, M);
		auto diff = t2 - t1;
		file1 << chrono::duration <double, milli>(diff).count() << endl;

		suma2 += float(chrono::duration <double, milli>(diff).count());

		t1 = steady_clock::now();
		if (N > M) {
			modifyParallelDynamic(f_dinamic, w_dinamic, rezultat2_dinamic, N, M, n, m, p);
		}
		else {
			modifyParallelDynamic2(f_dinamic, w_dinamic, rezultat2_dinamic, N, M, n, m, p);
		}
		t2 = steady_clock::now();
		diff = t2 - t1;
		file2 << chrono::duration <double, milli>(diff).count() << endl;

		suma += float(chrono::duration <double, milli>(diff).count());

	}
	file1 << suma2 / 10;
	file2 << suma / 10;
	
		
	
	
	printMatrix(f_dinamic, "output1.txt", N, M);

	bool ok = equalMatrix(rezultat_dinamic, f_dinamic, N, M);

	cout << ok;
	for (int i = 0; i < N; i++)
		delete[] f_dinamic[i];
	delete[] f_dinamic;

	for (int i = 0; i < N; i++)
		delete[] rezultat_dinamic[i];
	delete[] rezultat_dinamic;

	for (int i = 0; i < N; i++)
		delete[] rezultat2_dinamic[i];
	delete[] rezultat2_dinamic;

	for (int i = 0; i < n; i++)
		delete[] w_dinamic[i];
	delete[] w_dinamic;

	file.close();
	file1.close();
	file2.close();

}