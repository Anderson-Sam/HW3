from mininet.topo import Topo

class BinaryTreeTopo( Topo ):
    "Binary Tree Topology Class."
    def __init__( self ):
        "Create the binary tree topology."

        # Initialize topology
        Topo.__init__( self )

	# Add hosts
        h = []
        s = []
        for id in range(0,8):
                h.append(self.addHost('h' + str(id)))	
	# Add switches
        for id in range(0,7):
                s.append(self.addSwitch('s' + str(id)))
	# Add links
        for switch in [0,1,4]:
	        self.addLink(s[switch], s[switch+1])
		
        self.addLink(s[1], s[3])
        self.addLink(s[0], s[4])
        self.addLink(s[4], s[6])
		
        self.addLink(s[2],h[0])
        self.addLink(s[2],h[1])
        self.addLink(s[3],h[2])
        self.addLink(s[3],h[3])
        self.addLink(s[5],h[4])
        self.addLink(s[5],h[5])
        self.addLink(s[6],h[6])
        self.addLink(s[6],h[7])
	
topos = { 'binary_tree': ( lambda: BinaryTreeTopo() ) }
