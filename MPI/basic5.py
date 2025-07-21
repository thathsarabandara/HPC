from mpi4py import MPI
import numpy
comm = MPI.COMM_WORLD

rank = comm.Get_rank()

randNum = numpy.zeros(1)
diffNum = numpy.random.random_sample(1)

if rank == 1:
    randNum = numpy.random.random_sample(1)
    print("Process", rank, "drew the number", randNum[0])
    comm.Isend(randNum, dest=0)
    req = comm.Irecv(randNum, source=MPI.ANY_SOURCE)
    req.Wait()
    print("Process", rank, "Recievied the number", randNum[0])

if rank == 0:
    print("Process", rank, "before receiving has the number", randNum[0])
    req = comm.Irecv(randNum, source=1)
    req.Wait()
    print("Process", rank, "Recievied the number", randNum[0])
    randNum *= 2
    comm.Isend(randNum, dest=1)