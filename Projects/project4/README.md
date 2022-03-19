##1.
#Proxy:
- 34.200.33.199 proxy
- 10.0.1.11 Server1
- 10.0.1.12 Server2

#Server1 & Server2:
- proxy 34.200.33.199

##2. ssh-agent key forwarding
- eval$(ssh-agent)
- ssh-add -K aws-keypair.pem
- ssh -A ubuntu@34.200.33.199
- ssh ubuntu@10.0.1.11

##3. haproxy config 
- /etc/haproxy/haproxy.cfg
- bind 34.200.33.199 to the front end, balance roundrobin, server1 check and server 2 chek
- sudo systemctl restart haproxy.service
- [haproxy setup website](https://linuxhint.com/how-to-install-and-configure-haproxy-load-balancer-in-linux/)

##4. Server config
- /etc/hosts was modified by adding: proxy 34.200.33.199
- site files were located at var/www/html/index.html so apache could access them
- sudo systemctl restart apache2
- used haproxy website in question 3

##5. Screenshots
- I tried for hours trying to debug haproxy, but it always gave me an issue of binding a socket, even though the IP address is correct. However, I was able to use curl to verify the  servers were working.

 
