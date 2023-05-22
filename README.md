Namecheap Dynamic DNS updater
-----------------------------

Python 3 script for checking if the hosts public IP has changed (using checkip.amazonaws.com) and updates dynamic DNS on Namecheap if necessary.

Add your domains settings to `config.ini` according to the provided example.

| Key           | Value                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------|
| HOST          | `@` for base domain<br> `subdomain` for subdomain (e.g. `test` if full domain is `test.example.com`) |
| DOMAIN        | Domain name (e.g. `example.com`)                                                                   |
| DDNS_PASSWORD | Dynamic DNS Password, **NOT** your Namecheap account password                                          |
| UPDATE_INTERVAL | Frequency of hosts public IP address check in seconds.    |

The program checks the hosts public IP every 10 minutes (configurable in `config.ini`). Start the program by executing

    python ddns.py

# Run as a service using systemctl

1. Download this repo into `/usr/local/bin/ddns` (or wherever you like)
1. Edit `ddns.service` if required. Configured to run script from `/usr/local/bin/ddns`
1. Copy the systemd unit file to systemd: `cp ddns.service /etc/systemd/system/`
1. Then run it with:

```
sudo systemctl start ddns    # Runs the script now
sudo systemctl enable ddns   # Sets the script to run every boot
journalctl -u ddns.service   # Check systemd journal for errors
```
