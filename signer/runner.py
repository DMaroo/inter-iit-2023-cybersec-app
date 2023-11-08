#!/usr/bin/env python

from signer import Signer

sgn = Signer()

# You can NOT use the [__sign] or [__verify] function in [signer.py].
# Your solution should work for any value of [key] and therefore should not be a
# hardcoded solution.

_, all_zeroes_enc_hex = sgn.execute("sign", "0" * 30)
all_zeroes_enc = bytes.fromhex(all_zeroes_enc_hex[:32])

target_msg = "InterIIT-2023".encode() + b'\x00' * 3

# We XOR the target messa, with the obtained encryption.
# This way the signer would not detect the `INTER_IIT` string
# and would inadvertently return the signature for it.
_, xored_target_enc = sgn.execute("sign", "0" * 31 + "1" + "0" * 32 + bytes.hex(Signer.xor(target_msg, all_zeroes_enc)) + "0" * 30)

sign_of_xored_target = xored_target_enc[:32]
_, answer = sgn.execute("verify", sign_of_xored_target + bytes.hex(target_msg) + "0" * 30)

# The final and the only print statement in the program should print out
# "Congratulations, you did it!" after a successful execution.
# There should be no other print statements in the program and you cannot
# hardcode this string to be printed.
print(answer)
