# This gives us the IP address of host OS.
export HOST_IP_ADDRESS=`ifconfig eth0 | grep inet | grep -v inet6 | sed -E "s/inet ([0-9]{1,3}.[0-9]{1,3}.[0-9].{1,3}.[0-9]{1,3}) .*$/\1/" | tr -d "\t"`
docker-compose up -d
