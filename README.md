# Converting file.p12 into keys and certificate file using SSL cmds

openssl pkcs12 -in file.p12 -out keys.pem -nocerts

openssl pkcs12 -in file.p12 -nokeys -out certificate.pem

