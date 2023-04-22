#include<WinSock2.h>
#include<WS2tcpip.h>
#include<iostream>
#pragma comment(lib,"ws2_32.lib")
#pragma warning(disable:4996)
class client {
private:
    const char* IP;
    int PORT;
    SOCKET sock;
public:
    client(char* ip, int port){
        IP = ip;
        PORT = port;
    }
    void createSession();//Creates socket and connects with the server.
    void sendData(char* message);//Sends message to the server, it works fine
    char* receive()
    {
        char message[2000];
        if (recv(sock, message, 2000, 0) == SOCKET_ERROR)
        {
            WSACleanup();
            return (char*)"Failed to receive Message";
        }
        return message;
    }
};