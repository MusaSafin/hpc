#!/usr/bin/env python
import random
from mpi4py import MPI


def main():
    communicator = MPI.COMM_WORLD
    rank = communicator.Get_rank()
    cpu_name = f"cpu{rank}"
    size = communicator.Get_size()
    free_ranks = list(range(size))

    if rank == 0:
        cpu_sequence = [(cpu_name, rank)]
        next_cpu = random.choice(free_ranks[1:])
        communicator.ssend(cpu_sequence, dest=next_cpu)
    else:
        cpu_sequence = communicator.recv()
        print(f"{cpu_sequence[-1][0]} greets {cpu_name}", flush=True)
        used_ranks = [elem[1] for elem in cpu_sequence] + [rank]
        unused_ranks = [elem for elem in free_ranks if elem not in used_ranks]
        if unused_ranks:
            cpu_sequence.append((cpu_name, rank))
            next_cpu = random.choice(unused_ranks)
            communicator.ssend(cpu_sequence, dest=next_cpu)

    MPI.Finalize()


if __name__ == "__main__":
    main()
