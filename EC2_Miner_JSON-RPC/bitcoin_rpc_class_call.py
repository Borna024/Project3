from bitcoin_rpc_class import RPCHost

# version 0.16 of bitcoind, default port for regtest network is changed from 18332 to 18443
# The port number depends on the one writtein the bitcoin.conf file
rpcPort = '18443'
# The RPC username and RPC password MUST match the one in your bitcoin.conf file
rpcUser = 'vinay'
rpcPassword = 'fintech'

#Accessing the RPC local server
serverURL = 'http://' + 'vinay' + ':' + 'fintech' + '@127.0.0.1:' + rpcPort
print(serverURL)

#Using the class defined in the bitcoin_rpc_class.py
host = RPCHost(serverURL)
print('123')
hash = host.call('getbestblockhash')
print (hash)
#block = host.call('getblock', hash)
#coin = block['tx'][0]
#test = host.call('listreceivedbyaddress', 0, True)
#print (test)


#from jsonrpc import ServiceProxy
  
#access = ServiceProxy("http://bitcoinrpc:7bLjxV1CKhNJmdxTUMxTpF4vEemWCp49kMX9CwvZabYi@127.0.0.1:18446")
#print( access.getinfo())

#access.listreceivedbyaddress(6)
#access.sendtoaddress("11yEmxiMso2RsFVfBcCa616npBvGgxiBX", 10)