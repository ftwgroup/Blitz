import boto


## This is a manager that handles all the server interfaces
class EC2Manager:
    def __init__(self):
        self.ec2conn = None
        self.access_key = 'the_key'
        self.secret_key = 'the_secret'
        self.connect()

    #connects to the ec2 server
    def connect(self):
        self.ec2conn = boto.connect_ec2(self.access_key, self.secret_key)

    #adds a single server with a name
    def add_server(self, ami_id, name=None):
        self.ec2conn.run_instances(ami_id, key_name=name)

    #adds multiple serves
    def add_servers(self, ami_id, count, names=None):
        for index in range(count):
            if len(names) == count:
                self.add_server(ami_id, names[index])
            else:
                self.add_server(ami_id)

    #deletes the server
    def delete_server(self):
        reservations = self.ec2conn.get_all_instances()
        print("List of running instances: ")
        for reservation in reservations:
            print(reservation.instances[0].id)
        server = raw_input("What server would you like to delete: ")
        self.ec2conn.terminate_instances(instance_ids=[server])
