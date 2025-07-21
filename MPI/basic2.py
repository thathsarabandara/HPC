from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
a = 3
b = 5

if rank == 0:
    print(a+b)
if rank == 1:
    print(a*b)
if rank == 2:
    print(max(a,b))


    