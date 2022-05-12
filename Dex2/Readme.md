# Dex2    
This is a modified version of dex where `require(IERC20(from).balanceOf(msg.sender) >= amount, "Not enough to swap");` is removed.
By removing this we now can deploy our own malicious token with high liquid and drain these two coins.
## Steps:
1. Deploy your own token with 400 tokens initial supply.
2. approve the spend of 100 tokens.
3. Transfer 100 token to Dex2.
4. swap 100 of your evil token by 100 of token1.
5. repeat the process with token2.
