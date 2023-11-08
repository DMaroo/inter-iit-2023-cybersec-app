# signer

## Forgery attack

We exploit the fact that we don't check for the `INTER_IIT` string at every stage of the encryption. This allows us to sneak in the `INTER_IIT` string by XOR-ing it one of the valid encryptions. This way we would obtain the sign for the `INTER_IIT` string without the signer complaining. Now we can just ask the signer to verify this valid signature and print the output.

Have a look at [runner.py](./runner.py) for the script.
