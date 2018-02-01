#include <sys/socket.h>
#include <errno.h>
#include <netinet/in.h>
#include <string.h>
#include <stdio.h>

#define BUF_LEN 1028
#define SERVER_PORT 8080

// html web server html  
const static char http_error_hdr[] = "HTTP/1.1 404 Not Found\r\nContent-type: text/html\r\n\r\n";
const static char http_html_hdr[] = "HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n";
const static char http_index_html[] = 
"<html><head><title>Congrats!</title></head>"
"<body><h1>Welcome to our HTTP server demo!</h1>"
"<p>This is a just small test page.</body></html>";

// HTTP 
// index html 
//  
int http_send_file(char *filename, int sockfd)
{
    if(!strcmp(filename, "/")){
        // write http HTTP --HTML  
        write(sockfd, http_html_hdr, strlen(http_html_hdr));
        write(sockfd, http_index_html, strlen(http_index_html));
    }
    else{
         //  404error  
        printf("%s:file not find!\n",filename);
        write(sockfd, http_error_hdr, strlen(http_error_hdr));
    }
  return 0;
}

//HTTP  
void serve(int sockfd){
    char buf[BUF_LEN];
    read(sockfd, buf, BUF_LEN);
    if(!strncmp(buf, "GET", 3)){
        char *file = buf + 4;
        char *space = strchr(file, ' ');
        *space = '\0';
        http_send_file(file, sockfd);
    }
    else{
         // HTTP POST HEAD   GET 
        printf("unsupported request!\n");
        return;
    }
}

int main(){
    int sockfd,err,newfd;
    struct sockaddr_in addr;
    // TCP  
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if(sockfd < 0){
        perror("socket creation failed!\n");
        return 0;
    }
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    // htons 
    //  
    addr.sin_port = htons(SERVER_PORT);
    addr.sin_addr.s_addr = INADDR_ANY;
    if(bind(sockfd, (struct sockaddr *)&addr, sizeof(struct sockaddr_in))){
        perror("socket binding failed!\n");
        return 0;
    }
    listen(sockfd, 128);
    for(;;){
        // HTTP  
        newfd = accept(sockfd, NULL, NULL);
        serve(newfd);
        close(newfd);
    }

    return 0;
}