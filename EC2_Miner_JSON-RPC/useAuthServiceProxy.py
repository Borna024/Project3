from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException


rpcPort = 18443
# The RPC username and RPC password MUST match the one in your bitcoin.conf file
rpc_user = "vinay"
rpc_password = "fintech"

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_connection = AuthServiceProxy("http://vinay:fintech@127.0.0.1:18443",timeout=120)

best_block_hash = rpc_connection.getbestblockhash()
print(best_block_hash)

# batch support : print timestamps of blocks 0 to 9 in 2 RPC round-trips:
commands = [ [ "getblockhash", height] for height in range(2) ]
#print(commands)
block_hashes = rpc_connection.batch_(commands)
#print(block_hashes)
blocks = rpc_connection.batch_([ [ "getblock", h ] for h in block_hashes ])
print(blocks)
#block_times = [ block["time"] for block in blocks ]
#print(block_times)


