from jsonrpc import ServiceProxy
  
access = ServiceProxy("http://bitcoinrpc:7bLjxV1CKhNJmdxTUMxTpF4vEemWCp49kMX9CwvZabYi@127.0.0.1:18336")
#access = ServiceProxy("http://bitcoinrpc:7bLjxV1CKhNJmdxTUMxTpF4vEemWCp49kMX9CwvZabYi@127.0.0.1:8332")

access.getinfo()
access.listreceivedbyaddress(6)
#access.sendtoaddress("11yEmxiMso2RsFVfBcCa616npBvGgxiBX", 10)