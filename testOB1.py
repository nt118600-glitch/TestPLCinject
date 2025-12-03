import snap7
from ctypes import c_int32

# ======== BlockType: fallback chắc chắn đúng ========
try:
    from snap7.type import BlockType       # phiên bản chuẩn
except Exception:
    class _BT:
        def __init__(self, v):
            self.ctype = c_int32(v)

    class BlockType:
        OB  = _BT(0x38)
        DB  = _BT(0x41)
        FC  = _BT(0x43)
        FB  = _BT(0x45)
        SFC = _BT(0x44)
        SFB = _BT(0x46)
# ===================================================


def main():
    cli = snap7.client.Client()
    cli.connect("192.168.0.203", 0, 2)

    print("Connected:", cli.get_connected())

    try:
        res = cli.full_upload(BlockType.DB, 1)

        if isinstance(res, tuple):
            data = res[0]
        else:
            data = res

        with open("DB1.bin", "wb") as f:
            f.write(data)

        print("Upload OK, size:", len(data))

    except Exception as e:
        print("Khi upload DB1:", e)

    cli.disconnect()
    print("Disconnected.")
    
if __name__ == "__main__":
    main()
