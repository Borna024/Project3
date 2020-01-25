### To send transactions on your new network requires you to have bitcoin to send. This regtest bitcoin can be generated thorugh mining to an address one of the nodes. 
### Lets start with generating a wallet on one of the nodes.
## cd
## cd bitcoin/bitcoin
### Now that you are in the right directory its time to choose which node you will generate the mneumonic for by specifying it with '-datadir=' and your preference of passowrd.
## bitcoin-cli -regtest -datadir=agent1 encryptwallet yourPassword
### Now that you have a a wallet and a password to it, you need to unlock the wallet for a given time measured in seconds before you can send transations.
## bitcoin-cli -regtest -datadir=agent1 walletpassphrase yourPassword 3000
### It is important that you secure this password somewhere otherwise you may not be able to send transactions from that node.
### Generate a bitcoin address.
## bitcoin-cli -regtest -datadir=agent1 getnewaddress
## Now you can fund that address by generating a specified number of blocks to it.
## bitcoin-cli -regtest -datadir=network generatetoaddress 1 yourWalletAddress
## To have access to your newly mined bitcoin you need to have at least 100 confirmations or additional blocks to make the block reward you recieved from the coinbase spendable.
## bitcoin-cli -regtest -datadir=network generatetoaddress 100 yourWalletAddress
### Congradulations, you should now have some regtest bitcoins and spend them as you wish. You can repeat the prcess of encrypting a wallet on a different node simply generate a new address on your existing node and send funds there. 
### Keep in mind that you may get signed out by the timer you set on the walletpassphrase unlock. 
### Now that you have another address you can send a transaction from your wallet. Make sure to specify the datadirectory of the command to a wallet you unlocked.
## bitcoin-cli -regtest -datadir=agent1 sendtoaddress yourRecieveAddress
### Your transaction is now in the mempool. The regtest network requires at least one confirmation before the bitcoin can be spent. 
## bitcoin-cli -regtest -datadir=network generatetoaddress 1 yourWalletAddress
### You now have access to the funds on your new wallet