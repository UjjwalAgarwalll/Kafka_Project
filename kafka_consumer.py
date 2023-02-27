from kafka import KafkaConsumer
consumer = KafkaConsumer('input')


# Function to check if the number is prime or not


def check_prime_number(number):
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        
        if number % i == 0:
            return False
        
    return True


# Displaying the result


for message in consumer:

    input_data = message.value.decode('utf-8').split(',')
    n = int(input_data[0])
    m = int(input_data[1])
    prime_count = 0
    current_number = n
    while prime_count <= m:

        if check_prime_number(current_number):
            prime_count = prime_count + 1

        current_number = current_number + 1
        
    print(f"The {m}th prime number from {n} is {current_number - 1}")
