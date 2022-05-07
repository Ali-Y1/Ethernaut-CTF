from brownie import network, config,accounts
from web3 import Web3


LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def get_environment():
    return Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/" + config['Web3']))
