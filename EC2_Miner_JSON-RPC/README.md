# Project 3 - Notes from Vinay Kakuru

* Name: *Vinay Kakuru*
* Assignment: Project 3
* Summary: *Notes summarizes steps to setup an ec2 instance, install bitcoin node, start bitcoin in regtest mode, install project related libraries, other key points*

## EC2 Instance

* t2.small
* Ubuntu Server 16.04 LTS (HVM), SSD Volume Type or higher
* Create a new key pair - download the file (*.pem)
    * A key pair consists of a public key that AWS stores and a private key file that you store. Together, they allow you to connect to your instance securely. For Windows AMIs, the private key file is required to obtain the password used to log into your instance. For Linux AMIs, the private key file allows you to securely SSH into your instance.
* Download Putty and PuttyGen
    * Use PuttyGen to convert the *.pem file to *.ppk
    * Use Putty to SSH into the remote Ubuntu server
        * Session Tab: Set the hostname as ec2 instance name, Port as 22, connection type as SSH
        * Connection->SSH->Auth Tab: Select the create *.ppk (Putty Private Key) File
    * User name for Ubuntu instance is "ubuntu" by default
        * Other operating systems might have other credential - can find respective credentials on AWS website

## Bitcoin Regtest Node

* https://samsclass.info/141/proj/pBitc1.htm
* https://samsclass.info/141/proj/pBitc2.htm

* To prepare your Ubuntu machine, execute these commands:
    * sudo apt-get update
    * sudo apt-get install git build-essential -y
    * sudo apt-get install autoconf libboost-all-dev libssl-dev libprotobuf-dev protobuf-compiler libqt4-dev libqrencode-dev libtool -y
    * sudo apt-get install libdb5.1++-dev libevent-dev pkg-config -y

* Install Berkley Database
    * wget http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz
    * sha256sum db-4.8.30.NC.tar.gz
    *tar -xvf db-4.8.30.NC.tar.gz
    * cd db-4.8.30.NC/build_unix
    * mkdir -p build
    * BDB_PREFIX=$(pwd)/build ../dist/configure --disable-shared --enable-cxx --with-pic --prefix=$BDB_PREFIX
    * make install
    * cd ../..

* Compile Bitcoin Core from Source
    * git clone https://github.com/bitcoin/bitcoin.git
    * cd bitcoin
    * git tag
    * git checkout v0.12.1rc2
    * ./autogen.sh
    * ./configure --help
    * ./configure --with-incompatible-bdb
    * make
        * "this takes 10-20 mins"
    * sudo make install
    * which bitcoind
    * which bitcoin-cli

* Create Config File
    * cd
    * mkdir .bitcoin
    * nano .bitcoin/bitcoin.conf
        * "See the bitcoin.conf in the repo"

* Start Bitcoin Daemon
    * bitcoind -regtest -daemon

## Most requently used RPCs during the project

* See Examples uploaded
    * bitcoin-cli -regtest getblockchaininfo
    * bitcoin-cli -regtest getinfo
    * bitcoin-cli -regtest encryptwallet P@ssw0rd
    * bitcoin-cli -regtest walletpassphrase P@ssw0rd 360
    * bitcoin-cli -regtest backupwallet wallet.backup
    * ls -l ~/wal*
    * bitcoin-cli -regtest importwallet wallet.backup
    * bitcoin-cli -regtest dumpwallet wallet.txt
    * head ~/.bitcoin/wallet.txt
    * bitcoin-cli -regtest getnewaddress
    * bitcoin-cli -regtest getbalance
    * bitcoin-cli getblock "BlockHash" 2
    * bitcoin-cli getblock "BlockHash" 1
    * bitcoin-cli getblock "BlockHash" 0
    * bitcoin-cli getblockhash 101
    * bitcoin-cli getbestblockhash
    * bitcoin-cli gettxout "TXid" 0
    * bitcoin-cli generatetoaddress 11 "Address"
    * bitcoin-cli listtransactions

## Installing Libraries to use JSON-RPC
* Refer to code in Repo
    * bitcoin_rpc_class.py
    * bitcoin_rpc_class_call.py
    * useAuthServiceProxy.py

* Libraries to install
    * python-apt (0.9.3.5ubuntu3)
    * python-bitcoinlib (0.11.0dev)
    * python-bitcoinrpc (1.0) <<<---- This is the lastest one
    * requests (2.2.1)

* Observations: 
    * vin [ txid + vout pair ] will give you the from address
    * when vin [coinbase], this is a system derived txn
    * all fees and block rewards collected as part of txn and block mining will be marked as [coinbase]
    * System Txn
        * "vin": [
        {
          "coinbase": "01660101",
          "sequence": 4294967295
        }
        ]
    * Actual Txn
        * "vin": [
        {
          "txid": "fffe6fa7c698d7534889413d753cd7bdae9ecfdef3984c42dfe79f68454acb3c",
          "vout": 0,
          "scriptSig": {
            "asm": "0014b1a7d3b0d1011a3475c32949d2786676f0a376b3",
            "hex": "160014b1a7d3b0d1011a3475c32949d2786676f0a376b3"
          },
          "txinwitness": [
            "304402200e72240746ec045668b8a2e30ecd36a761ecc9bab1b2cc039dbb7ba12c7218820220019d9e63738e1b6932b6bf331c3514dd85ae4c2221f19ef458184907fa7b345501",
            "02098cfd632f00010e78b712508cae2fc48c47a033b9a3c14e30b0eb3a074a5e48"
          ],
          "sequence": 4294967294
        }
        ]
    
## Other Notes

    * Good reference https://bitcoin.org/en/developer-reference#sendmany

    * EC2 server needs to have a minimum 2Gb ram to run a node

    * Select latest version of Ubuntu as the 14.xx does not have python 3.7, therefore pandas cannot be installed

    * Dont change the rpcuser and rpcpassword in the bitcoin.conf file once set, as this could cause problems with running "bitcoin-cli" from terminal. In case of errors, try to force the following:
        * bitcoin-cli -rpcuser=vinay -rpcpassword=fintech -rpcport=18443 xxxxxx
        * xxxxxx is RPC command

    * On Regtest Node, Bitcoin follows default rules, the first  150 blocks pay a reward of 50 bitcoins. After that, the reward halves after 150 blocks, so it pays 25, 12.5...

        https://github.com/ChristopherA/Learning-Bitcoin-from-the-Command-Line/blob/master/A2_2_Mining_with_Regtest.md

    *  Mined block must have 100 confirmations before that reward can be spent. i.e. needed to be followed by 100 blocks before it shows up in your wallet
