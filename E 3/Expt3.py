# challenge_response_exp.py
import hashlib, time, secrets

shared_secret = "network_secret_key"
FRESHNESS_WINDOW = 5  # seconds

def generate_nonce():
    return secrets.token_hex(8)  # cryptographically stronger nonce

def hash_response(nonce, secret, timestamp=None):
    s = nonce + (timestamp or "") + secret
    return hashlib.sha256(s.encode()).hexdigest()

# Server -> Client
nonce = generate_nonce()
print("Server sends nonce:", nonce)

# Client computes (optionally with timestamp)
timestamp = str(int(time.time()))
client_resp = hash_response(nonce, shared_secret, timestamp)
print("Client sends response (with timestamp):", client_resp, " ts:", timestamp)

# Server verifies freshness + hash
now = int(time.time())
if abs(now - int(timestamp)) <= FRESHNESS_WINDOW:
    expected = hash_response(nonce, shared_secret, timestamp)
    print("Auth result:", "Success" if client_resp == expected else "Failed")
else:
    print("Replay detected / timestamp expired")
