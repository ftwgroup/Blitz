import boto
import time
from moto import mock_ec2
from blitz.EC2Manager import EC2Manager

## Creates 2 servers
@mock_ec2
def test_add_servers():
    manager = EC2Manager()
    manager.add_servers('ami-1234abcd', 2)
    conn = boto.connect_ec2('the_key', 'the_secret')
    reservations = conn.get_all_instances()
    print(reservations)
    assert len(reservations) == 2
    instance1 = reservations[0].instances[0]
    assert instance1.image_id == 'ami-1234abcd'

## Creates 2 servers and deletes the first one
@mock_ec2
def test_delete_server():
    manager = EC2Manager()
    manager.add_servers('ami-1234abcd', 2)
    manager.delete_server()
    time.sleep(1)
    conn = boto.connect_ec2('the_key', 'the_secret')
    reservations = conn.get_all_instances()
    print("List of remaining servers")
    for reservation in reservations:
        print(reservation.instances[0].id)
