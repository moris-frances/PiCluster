from mpi4py import MPI
import time
import sys
import board
import adafruit_dht

def read_sensor():
    dht_device = adafruit_dht.DHT11(board.D23, use_pulseio=False)
    temperature_c = dht_device.temperature
    humidity = dht_device.humidity
    dht_device.exit()
    return temperature_c, humidity

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
        print("Usage: mpiexec -n <num_processes> python my_script.py <iterations>")
        return

    iterations = int(sys.argv[1])

    print(f"Running with {iterations} iterations")

    start_time = time.time()

    # Read sensor data
    temperature, humidity = read_sensor()

    # Distribute workload among MPI processes
    chunk_size = iterations // size
    my_start = rank * chunk_size
    my_end = my_start + chunk_size - 1 if rank < size - 1 else iterations

    for i in range(my_start, my_end + 1):
        # Use sensor data in resource-intensive algorithm
        primes = calculate_primes(2, temperature * humidity)

    # Gather results
    all_primes = comm.gather(primes, root=0)

    if rank == 0:
        end_time = time.time()
        print(f"Elapsed time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
