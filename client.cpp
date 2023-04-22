#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netdb.h>
#include <unistd.h>
    
#define ADDR "192.168.0.101"
#define PORT "12003"
    
void sendall(int socket, char *bytes, int length)
{
    int n = 0, total = 0;
    while (total < length) {
        n = send(socket, bytes + total, total-length, 0);
        if (n == -1) {
            perror("send");
            exit(1);
        }
        total += n;
    }
}
    
int main()
{
    struct addrinfo hints = {0}, *addr = NULL;
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    
    int status = getaddrinfo(ADDR, PORT, &hints, &addr);
    if (status != 0) {
        fprintf(stderr, "getaddrinfo()\n");
        exit(1);
    }
    int sock = -1;
    {
        struct addrinfo *p = NULL;
        for (p = addr; p != NULL; p = addr->ai_next) {
            sock = socket(p->ai_family, p->ai_socktype, p->ai_protocol);
            if (sock == -1) {
                continue;
            }
            if (connect(sock, p->ai_addr, p->ai_addrlen) != -1) {
                break;
            }
            close(sock);
        }
        if (p == NULL) {
            fprintf(stderr, "connect(), socket()\n");
            exit(1);
        }
        freeaddrinfo(addr);
        /* Do whatever. */
        sendall(sock, "Hello, World", 12);
    
        /* Do whatever. */
    }
    
    close(sock);
    return 0;
}