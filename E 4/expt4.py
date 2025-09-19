import datetime
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID

# Generate a private key
key = rsa.generate_private_key(65537, 2048)
 
# Create a subject and issuer (they are the same for a self-signed cert)
name = x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, u"localhost"),
])
 
# Build the self-signed certificate
certificate = x509.CertificateBuilder().subject_name( name).issuer_name( name).public_key(key.public_key()).serial_number(x509.random_serial_number()).not_valid_before(datetime.datetime.utcnow()).not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365)).sign(key, hashes.SHA256())
 
# Save the certificate to a file
with open("self_signed_cert.pem", "wb") as f:
    f.write(certificate.public_bytes(serialization.Encoding.PEM))

print("Self-signed certificate created and saved as self_signed_cert.pem")
