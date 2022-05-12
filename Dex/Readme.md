# Dex     
The vulrenambility in this level is in calculating the swap price in function`get_swap_price`
## Steps:
1. First you should approve for the contract to swap 10 tokens by calling function `approve`.
2. Then you need to swap 10 of token1 by 10 of token2.
Here the ration between the two coins changed to 110:90.
3. Now you will swap 20 of token2 by 24 of token1 according to the `swap_price` ratio 110:90.
4. keep doing this till one of them is drained.