from OpenSSL import crypto
from consts import CertConsts


def build_cert(dns: str) -> crypto.X509:
    """
    Builds cert object
    :param dns: dns name to be signed
    """
    cert = crypto.X509()
    cert.get_subject().CN = dns
    cert.set_serial_number(CertConsts.SERIAL_NUMBER)
    cert.gmtime_adj_notBefore(CertConsts.VALID_FROM_SECONDS)
    cert.gmtime_adj_notAfter(CertConsts.EXPIRE_IN_SECONDS)
    cert.set_issuer(cert.get_subject())
    return cert


def cert_gen(dns: str = CertConsts.DNS, cert_file: str = CertConsts.CERT_FILE, key_file: str = CertConsts.KEY_FILE):
    """
    Generates self-signed certificate for DNS
    :param dns: dns name to be signed
    :param cert_file: self-signed certificate filename
    :param key_file: private key filename
    """
    # create a key pair
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, CertConsts.KEY_SIZE)
    # create a self-signed cert
    cert = build_cert(dns)
    cert.set_pubkey(k)
    cert.sign(k, CertConsts.HASH_METHOD)
    with open(cert_file, "w") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))
    with open(key_file, "w") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8"))
