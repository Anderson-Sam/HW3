Sam Anderson
HW 3

PART 1 
mininet ping all result 
***** NOTE: used indexes to organise hosts and switches, so lables here start from 0, rather than 1
mininet> pingall
*** Ping: testing ping reachability
h0 -> h1 h2 h3 h4 h5 h6 h7 
h1 -> h0 h2 h3 h4 h5 h6 h7 
h2 -> h0 h1 h3 h4 h5 h6 h7 
h3 -> h0 h1 h2 h4 h5 h6 h7 
h4 -> h0 h1 h2 h3 h5 h6 h7 
h5 -> h0 h1 h2 h3 h4 h6 h7 
h6 -> h0 h1 h2 h3 h4 h5 h7 
h7 -> h0 h1 h2 h3 h4 h5 h6 
*** Results: 0% dropped (56/56 received)

P1 Q1:
nodes output:
mininet> nodes
available nodes are: 
h0 h1 h2 h3 h4 h5 h6 h7 s0 s1 s2 s3 s4 s5 s6

net output:
mininet> net
h0 h0-eth0:s2-eth2
h1 h1-eth0:s2-eth3
h2 h2-eth0:s3-eth2
h3 h3-eth0:s3-eth3
h4 h4-eth0:s5-eth2
h5 h5-eth0:s5-eth3
h6 h6-eth0:s6-eth2
h7 h7-eth0:s6-eth3
s0 lo:  s0-eth1:s1-eth1 s0-eth2:s4-eth2
s1 lo:  s1-eth1:s0-eth1 s1-eth2:s2-eth1 s1-eth3:s3-eth1
s2 lo:  s2-eth1:s1-eth2 s2-eth2:h0-eth0 s2-eth3:h1-eth0
s3 lo:  s3-eth1:s1-eth3 s3-eth2:h2-eth0 s3-eth3:h3-eth0
s4 lo:  s4-eth1:s5-eth1 s4-eth2:s0-eth2 s4-eth3:s6-eth1
s5 lo:  s5-eth1:s4-eth1 s5-eth2:h4-eth0 s5-eth3:h5-eth0
s6 lo:  s6-eth1:s4-eth3 s6-eth2:h6-eth0 s6-eth3:h7-eth0

P1 Q2:
**** used h6 since host indexes started from 0, so h7 labled in the hw documentation corresponds to h6 here. 
mininet> h6 ifconfig
h6-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.7  netmask 255.0.0.0  broadcast 10.255.255.255
        inet6 fe80::608e:cbff:fe2d:40aa  prefixlen 64  scopeid 0x20<link>
        ether 62:8e:cb:2d:40:aa  txqueuelen 1000  (Ethernet)
        RX packets 296  bytes 36036 (36.0 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 39  bytes 2826 (2.8 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        
PART 2:

P2 Q1:
	When packets arrive, we will start with def _handle_packetsIn, where first we ensure the packet is complete, then we use the act_like_a_hub function to determine how to reroute this packet. From there, depending on routing behavior, packets will be forwarded differently. As of part two, this function is fully commented out. 
	
P2 Q2: (a/b)
	h0 to h1 min/max/avg = .96/4.85/2.55
	h0 to h7 min/max/avg = 3.44/11.85/7.28
	
	(c) When pinging h0 to h1, there is only one switch between the two hosts, so there is mininal routing within the binary tree topology. Although when pinging h0 to h7, a packet must reach the top of the binary tree, then return to the bottom. In the first case, only one switch is needed, although in the second ping, the packet must pass through 5 switches. 

P2 Q3: 
	(a) iperf is used to measure the bandwith capability between two hosts. 
	(b) For h0 to h1, the bandwith is between 16.6 Mbits/sec and 19.3 Mbits/sec. For h0 to h7, the bandwith is between 3.75 Mbits/sec and 4.25 Mbits/sec.
	(c) The difference is because there is a larger propagation time between h0 and h7 so, communication is slower since packet integrity needs to be verified with tcp. As an example, it is harder to quickly share information when other hosts are slow to respond. Additioanlly there can be bottlenecks, especially near the root of the tree if there were other packets trying to cross to the other half of the binary tree. 

P2 Q4:
	In the handle_packetIn function, the function knows what switch is handling packet with the self input, and it knows a connection, both as function inputs. We can add a function, and call it in def handle_packetIn to log traffic by passing self and a connection to log a detected incomming packet. Then it can log where the packet was sent, if it was properly sent, otherwise it can log an error. 
	
PART 3:
PQ Q1:
	This functions allows the switch to learn where a packet should be forwarded so, there the network gets smarter, rather than flodding every switch like the hub function every time. In the ping example, the switch first adds the source mac address if the source is unknown. Next, if the switch knows which port to forward the packet, it will only forward it to the righty port. If the controller does not know where to forward the packet, it will pass it onto all other ports.
	
P3 Q2 (a/b) h0 to h1 min/max/avg = 1.11/5.51/2.14. h0 to h7 min/max/avg = 3.47/10.91/6.00

	(c) After running these tests a few times, there is a statistically significant decrease in the average ping time. We go to 2.55ms to 2.14ms  with the short ping, and 7.28 ms to 6ms. Using the provided stdev measurement simply by observation, there is a consistant and noticible decrease in ping times. Additionally the reason for this decrease could be due to some combination of learning where to forward packets, and not using the act_like_a_hub function which congests traffic by forwarding packets to all outputs.
	
P3 Q3: (a)
	The thorughput from h0 to h1 is between 16.5 mbits/sec and 19.3 mbits/sec. For h0 to h7, the throughput was between 3.93 mbits/sec and 4.52 mbits/sec
	
	(b)
	 There is a virtually no change between bandwidth between h0 and h1, likley because there is very little room for smart routing between h0 and h1 given the first switch connected to h0, also connects to h1. Although for the bandwidth between h0 an and h7, there is a noticible increase by about .25 mbits/sec. While this could be due to natual randomness in the test, if there were actually an improvement, this would be due to smarter routing so packets only go to the host they were intended to reach. 	

 
        



