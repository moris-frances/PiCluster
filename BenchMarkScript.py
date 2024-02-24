from mpi4py import MPI
import time
import sys

def calculate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if len(sys.argv) != 2:
        print("Usage: mpiexec -n <num_processes> python my_script.py <memory>")
        return

    memory = sys.argv[1]
    if memory == '1GB':
        start = 2
        end = 30000  # Smaller range for lower memory usage
    else:
        print("Memory must be '1GB' for Raspberry Pi")
        return

    print(f"Running with {memory} of RAM")

    start_time = time.time()

    # Distribute workload among MPI processes
    chunk_size = (end - start + 1) // size
    my_start = start + rank * chunk_size
    my_end = my_start + chunk_size - 1 if rank < size - 1 else end
    primes = calculate_primes(my_start, my_end)

    # Gather results
    all_primes = comm.gather(primes, root=0)

    if rank == 0:
        end_time = time.time()
        print(f"Elapsed time: {end_time - start_time:.2f} seconds")
        # Process and display the collected primes as needed

if __name__ == "__main__":
    main()
