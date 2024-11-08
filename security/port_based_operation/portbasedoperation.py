import socket  #imports the socket library to create and manage network connections
import time    #imports the time library to handle delays

#initialize variables
operation = ""  #stores the operation from the server response
result = 0  #stores the current result after each operation
number = 0  #stores the number from the server response
next_port = 1337  #initial port to connect to
IP = "10.10.138.80"  #replace with the actual IP address of the deployed machine

#loop until port 9765 is reached or a stop condition occurs
while next_port != 9765:
    try:
        #create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)  #set a 4-second timeout for the connection attempt
        #attempt to connect to the server on the specified port
        s.connect((IP, int(next_port)))  
        print("connected to port", next_port)  #print a message indicating successful connection

        #send a request to the server to get data
        request = f"GET / HTTP/1.1\r\nHost:{IP}\r\n\r\n"  #request format
        s.send(request.encode())  #send the request to the server

        #receive the server's response
        response = s.recv(1024)
        response = s.recv(1024)  #call again to receive the full data
        response = response.decode()  #decode the bytes into a string
        
        print("raw response:", response)  #print the raw response for visibility

        #check if the response is valid and contains the expected data
        if "\r\n\r\n" in response:
            response = response.split("\r\n\r\n")[1].split(" ")  #parse the response after the header
            #extract operation, number, and next port from the response
            operation = response[0].lower()  #operation: add, minus, multiply, divide
            number = float(response[1])  #number for the operation
            next_port = int(response[2])  #next port to connect to
        else:
            print("unexpected response format, skipping this port")
            s.close()
            continue  #skip to the next iteration if the response is not in the expected format

        #perform the operation on the current result
        if operation == "add":
            result += number  #add the number to the result
        elif operation == "minus":
            result -= number  #subtract the number from the result
        elif operation == "multiply":
            result *= number  #multiply the result by the number
        elif operation == "divide":
            result /= number  #divide the result by the number
        else:
            continue  #ignore if the operation is unknown

        #close the socket
        s.close()
        print("current result:", result)  #print the current result for visibility

        #wait for the port to become available again
        time.sleep(3.5)  #wait 3.5 seconds to avoid overwhelming the server

    except ConnectionRefusedError:  #if connection is refused, retry
        print(f"port {next_port} is closed, retrying...")
        time.sleep(0.2)  #wait 0.2 seconds before retrying

    except TimeoutError:  #handle timeout errors
        print(f"timeout at port {next_port}, retrying...")
        time.sleep(0.2)  #wait 0.2 seconds before retrying

#print the final result after reaching port 9765
print(f"you have reached the end! here is your flag: {int(round(result, 2))}")
