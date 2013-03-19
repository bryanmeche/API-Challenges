import pyrax

#Authenticate
pyrax.set_credential_file("/home/python/.rackspace_cloud_credentials")

dc = int(raw_input ("Press 1 for DFW, 2 for ORD Default DFW: "))

if dc == 2:
  cs = pyrax.connect_to_cloudservers(region="ORD")
else:
	cs = pyrax.cloudservers
	


ubuntu_image = [img for img in cs.images.list()
	if "Ubuntu 12.04" in img.name][0]
	
flavor_512 = [flavor for flavor in cs.flavors.list()
	if flavor.ram == 512][0]
	
num_servers = int(raw_input ("How many servers do you want to create: "))
i = 0
name = str(raw_input ("What prefix do you want the servers to be named: "))

while (i < num_servers):
	i = i + 1
	server_name = name + str(i)
	print "This is server #: " , i
	server = cs.servers.create(server_name, ubuntu_image.id, flavor_512.id)
	print "Name:", server.name
	print "ID:", server.id
	print "Status:", server.status
	print "Admin Password:", server.adminPass
	print "Networks:", server.networks

	
	

