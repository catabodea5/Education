#include <iostream>
#include <fstream>
#include <chrono>
#include "mpi.h"

using namespace std;
using namespace std::chrono;

#define MAX 100


int main(int argc, char* argv[]) {
    int nprocs, myrank;
    MPI_Status status;
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &nprocs);
    MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
    int value = myrank * 10;
    int sum = 0, tmp;
    MPI_Send(&value, 1, MPI_INT, (myrank + 1) % nprocs, 10, MPI_COMM_WORLD);
    MPI_Recv(&tmp, 1, MPI_INT, (myrank - 1 + nprocs) % nprocs, 10, MPI_COMM_WORLD, &status);
    sum += tmp;
    if (myrank == 0)
        printf("%d", sum);
    MPI_Finalize();
    return 0;
}