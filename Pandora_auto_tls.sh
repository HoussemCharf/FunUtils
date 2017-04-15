#!/bin/bash
tlst=`openssl s_client -connect tuner.pandora.com:443 < /dev/null 2> /dev/null | \
openssl x509 -noout -fingerprint | tr -d ':' | cut -d'=' -f2`
new_tls="/home/pi/.config/pianobar/config"
sed -ie "s/^tls_fingerprint =.*/tls_fingerprint = $tls/" $new_tls
