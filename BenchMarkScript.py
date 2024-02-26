from mpi4py import MPI
import time
import sys
import board
import adafruit_dht

def calculate_primes(start, end, all_temperature_humidity):
    # Dummy operation using temperature and humidity
    for temperature_humidity in all_temperature_humidity:
        dummy_value = (temperature_humidity.temperature_c + temperature_humidity.humidity) % 10
    primes = []
    for num in range(start, end + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes

def read_sensor():
    dht_device = adafruit_dht.DHT11(board.D23)
    while True:
        try:
            temperature_c = dht_device.temperature
            humidity = dht_device.humidity
            dht_device.exit()
            break
        except RuntimeError as error:
            print(error.args[0])
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
    return temperature_c, humidity

def main():
    comm = MPI.COMM_WORLD

    rank = comm.Get_rank()
    size = comm.Get_size()
    
    # Poll every device for temperature and humidity values
    temp_humidity = read_sensor()
    all_temp_humidity = comm.gather(temp_humidity, root=0)  
    print("Gatered themperature and Humidity: ")
    print(all_temp_humidity)

    start = 2
    end = 300000 

    start_time = time.time()

    # Distribute workload among MPI processes
    chunk_size = (end - start + 1) // size
    my_start = start + rank * chunk_size
    my_end = my_start + chunk_size - 1 if rank < size - 1 else end
    primes = calculate_primes(my_start, my_end, all_temp_humidity)

    # Gather results
    all_primes = comm.gather(primes, root=0)
    if rank == 0:
        print(all_primes)
    if rank == 0:
        end_time = time.time()
        print(f"Elapsed time: {end_time - start_time:.2f} seconds")
        # Process and display the collected primes as needed

if __name__ == "__main__":
    main()
