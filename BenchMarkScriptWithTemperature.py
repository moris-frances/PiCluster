from mpi4py import MPI
import time
import sys
import os
import json
# nfs_dir = "/nfsDir"
# tempFileSuffix = "TempValue"
# config = []

def read_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config.get('nfs_dir'), config.get('tempFileSuffix')


def calculate_primes(start, end, all_temperature):
    # Dummy operation using temperature and humidity
    for temperature in all_temperature:
        dummy_value = (temperature) % 10
    primes = []
    for num in range(start, end + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes

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

def main():
    nfs_dir, tempFileSuffix = read_config('config.json')
    comm = MPI.COMM_WORLD

    rank = comm.Get_rank()
    size = comm.Get_size()
    all_temperature = []
    if rank == 0:
        # Get the temperature reading from all of the devices
        all_temperature = get_sensor_readings_from_files(nfs_dir, tempFileSuffix)
        print("Gatered themperature: ")
        print(all_temperature)

    start = 2
    end = 300000 

    start_time = time.time()

    # Distribute workload among MPI processes
    chunk_size = (end - start + 1) // size
    my_start = start + rank * chunk_size
    my_end = my_start + chunk_size - 1 if rank < size - 1 else end
    primes = calculate_primes(my_start, my_end, all_temperature)

    # Gather results
    all_primes = comm.gather(primes, root=0)
    if rank == 0:
        end_time = time.time()
        # Display process time on the main node
        print(f"Elapsed time: {end_time - start_time:.2f} seconds")
        

if __name__ == "__main__":
    main()
