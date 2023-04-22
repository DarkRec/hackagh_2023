#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <iostream>
#include <cstdlib>
#include <ctime>
#define PORT 1234
  
int main(int argc, char const* argv[])
{
    int status, valread, client_fd;
    struct sockaddr_in serv_addr;
    //char* hello = "60.23423434, 50.234234";
    
    srand(time(nullptr)); // seed the random number generator

    // generate random latitude and longitude coordinates
    double latitude = (rand() % 180) - 90 + static_cast<double>(rand() % 10000000) / 10000000.0;
    double longitude = (rand() % 360) - 180 + static_cast<double>(rand() % 10000000) / 10000000.0;

    // create a char* variable and format the coordinates as a string literal
    char* hello = new char[50];
    sprintf(hello, "%.8f, %.8f", latitude, longitude);

    char buffer[2048] = { 0 };
    if ((client_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("\n Socket creation error \n");
        return -1;
    }
  
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);
    
    // Convert IPv4 and IPv6 addresses from text to binary
    // form
    if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr)
        <= 0) {
        printf(
            "\nInvalid address/ Address not supported \n");
        return -1;
    }
  
    if ((status
         = connect(client_fd, (struct sockaddr*)&serv_addr,
                   sizeof(serv_addr)))
        < 0) {
        printf("\nConnection Failed \n");
        return -1;
    }
    send(client_fd, hello, strlen(hello), 0);
    printf("Hello message sent\n");
    valread = read(client_fd, buffer, 2048);
    printf("%s\n", buffer);
  
    // closing the connected socket
    close(client_fd);
    return 0;
}