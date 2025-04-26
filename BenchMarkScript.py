from mpi4py import MPI  # Import MPI from mpi4py for parallel computing
import time             # Import time for performance measurement

# Function to calculate prime numbers within a given range
def calculate_primes(start, end):
    primes = []  # Initialize an empty list to store prime numbers
    # Loop through each number in the given range
    for num in range(start, end + 1):
        # Check if num is a prime number
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)  # If prime, add to the list
    return primes  # Return the list of prime numbers

# Main function where the parallel computation is orchestrated
def main():
    comm = MPI.COMM_WORLD  # Initialize MPI environment

    rank = comm.Get_rank()  # Get the rank (ID) of the current process
    size = comm.Get_size()  # Get the total number of processes

    # Define the range of numbers to check for primality
    start = 2
    end = 300000 

    start_time = time.time()  # Record start time for performance measurement

    # Distribute workload among MPI processes
    chunk_size = (end - start + 1) // size  # Calculate workload for each process
    my_start = start + rank * chunk_size    # Calculate start number for this process
    my_end = my_start + chunk_size - 1 if rank < size - 1 else end  # Calculate end number for this process
    primes = calculate_primes(my_start, my_end)  # Calculate primes for this process's range

    # Gather all calculated primes from each process
    all_primes = comm.gather(primes, root=0)  # Root process collects results from all processes

    # If this is the root process, conclude and print the results
    if rank == 0:
        end_time = time.time()  # Record end time for performance measurement
        print(f"Elapsed time: {end_time - start_time:.2f} seconds")  # Print elapsed time
        # Process and display the collected primes as needed

# Entry point of the script
if __name__ == "__main__":  
    main()  # Call the main function if this script is executed
