import base64
import csv
import glob
import hashlib
import hmac
import os
import struct
import time

HERE = os.path.dirname(os.path.abspath(__file__))


def totp(secret: str, period: int = 30, digits: int = 6) -> str:
    secret = secret.strip().upper().replace(" ", "")
    padding = "=" * ((8 - len(secret) % 8) % 8)
    key = base64.b32decode(secret + padding)
    counter = int(time.time() // period)
    msg = struct.pack(">Q", counter)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    offset = h[-1] & 0x0F
    code = (struct.unpack(">I", h[offset:offset + 4])[0] & 0x7FFFFFFF) % (10 ** digits)
    return str(code).zfill(digits)


def parse_g2g_csv(path: str):
    accounts = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        for row in reader:
            if len(row) < 16:
                continue
            username = row[1].lstrip("'").strip()
            password = row[3].strip()
            remark = row[15].strip()
            if not username or ":" not in remark:
                continue
            secret = remark.split(":", 1)[0].strip()
            if not secret:
                continue
            accounts.append({"username": username, "password": password, "secret": secret})
    return accounts


def load_all_accounts():
    accounts = []
    for path in sorted(glob.glob(os.path.join(HERE, "*.csv"))):
        try:
            accounts.extend(parse_g2g_csv(path))
        except Exception as e:
            print(f"[!] Erreur lecture {os.path.basename(path)}: {e}")
    return accounts


def main():
    accounts = load_all_accounts()
    if not accounts:
        print("Aucun CSV G2G trouve dans ce dossier.")
        print("Depose un export CSV G2G ici puis relance.")
        input("\nAppuie sur Entree pour quitter...")
        return

    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            remaining = 30 - int(time.time()) % 30
            print(f"A2F - {len(accounts)} compte(s) - refresh dans {remaining:2d}s   (Ctrl+C pour quitter)\n")
            print(f"{'Username':<25} {'Code':<8} {'Password':<15}")
            print("-" * 50)
            for acc in accounts:
                code = totp(acc["secret"])
                print(f"{acc['username']:<25} {code:<8} {acc['password']:<15}")
            time.sleep(1)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
