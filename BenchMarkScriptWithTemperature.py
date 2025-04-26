# Import necessary libraries
from mpi4py import MPI  # MPI for parallel computing
import time             # Time module for performance measurement
import os               # OS module for interacting with the operating system
import json             # JSON module for parsing JSON files

# Function to read configuration from a JSON file
def read_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config.get('nfs_dir'), config.get('tempFileSuffix')

# Function to calculate prime numbers in a given range
def calculate_primes(start, end, all_temperature):
    # Process temperature data for some dummy operation (not used in prime calculation)
    for temperature in all_temperature:
        dummy_value = (temperature) % 10
    primes = []
    # Calculate primes in the specified range
    for num in range(start, end + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes

# Function to read sensor readings from files in a directory
def get_sensor_readings_from_files(nfs_dir, tempFileSuffix):
    temp_values = []
    for filename in os.listdir(nfs_dir):
        if filename.endswith(tempFileSuffix):
            with open(os.path.join(nfs_dir, filename), 'r') as file:
                content = file.read()
                try:
                    temp_value = int(content.strip())
                    temp_values.append(temp_value)
                except ValueError:
                    # Ignore files with non-integer contents
                    continue
    return temp_values

# Main function
def main():
    # Read configuration and setup MPI
    nfs_dir, tempFileSuffix = read_config('config.json')
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    all_temperature = []
    
    # Start timing the computation
    start_time = time.time()
    
    # Master process (rank 0) reads sensor data
    if rank == 0:
        all_temperature = get_sensor_readings_from_files(nfs_dir, tempFileSuffix)
        print("Gathered temperature: ")
        print(all_temperature)

    # Define the range for prime number calculation
    start = 2
    end = 300000 

    # Distribute the workload among available MPI processes
    chunk_size = (end - start + 1) // size
    my_start = start + rank * chunk_size
    my_end = my_start + chunk_size - 1 if rank < size - 1 else end
    primes = calculate_primes(my_start, my_end, all_temperature)

    # Gather computed prime numbers from all processes to the master process
    all_primes = comm.gather(primes, root=0)

    # Master process (rank 0) concludes timing and prints elapsed time
    if rank == 0:
        end_time = time.time()
        print(f"Elapsed time: {end_time - start_time:.2f} seconds")

# Entry point of the script
if __name__ == "__main__":
    main()
