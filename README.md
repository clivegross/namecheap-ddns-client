Namecheap Dynamic DNS updater
-----------------------------

## Description

A python based dynamic DNS updater client for Namecheap.

## Configuration

Create a `config.ini` file in the root of the directory. Use the provided example `config.ini.example` for reference.

    cp config.ini.example config.ini

Configure your dynamic DNS settings in `config.ini`.

| Key           | Value                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------|
| HOST          | `@` for base domain<br> `subdomain` for subdomain (e.g. `test` if full domain is `test.example.com`) |
| DOMAIN        | Domain name (e.g. `example.com`)                                                                   |
| DDNS_PASSWORD | Dynamic DNS Password, **NOT** your Namecheap account password                                          |
| UPDATE_INTERVAL | Frequency of hosts public IP address check in seconds.    |

## Update dynamic DNS record with public IP address

This Python 3 script checks if the hosts public IP address has changed (using [checkip.amazonaws.com](https://checkip.amazonaws.com/)) and updates the dynamic DNS record on Namecheap if necessary.

The program `ddns.py` runs forever and checks the hosts public IP address every 10 minutes (frequency configurable in `config.ini`). Start the program by executing:

    python ddns.py

Or run as a service (see below).

## Update dynamic DNS record with private IP address

An alternate Python 3 script can be used to check if the hosts private IP address (its primary local IP address) has changed instead. This can be useful in a private intranet where you do not have control of the DHCP server. Obtains the primary IP address of the host using [this socket solution by fatal_error on Stack Overflow](https://stackoverflow.com/a/28950776).

The program `ddns_private_ip.py` runs forever and checks the hosts primary private IP address every 10 minutes (frequency configurable in `config.ini`). Start the program by executing:

    python ddns_private_ip.py

Or run as a service (see below).

## Run as a service

### Using systemctl

1. Download this repo into `/usr/local/bin/ddns` (or wherever you like)
1. Edit `ddns.service` if required. Configured to run script from `/usr/local/bin/ddns`
1. Copy the systemd unit file to systemd: `cp ddns.service /etc/systemd/system/`
1. Then run it with:

```
sudo systemctl start ddns    # Runs the script now
sudo systemctl enable ddns   # Sets the script to run every boot
journalctl -u ddns.service   # Check systemd journal for errors
```

