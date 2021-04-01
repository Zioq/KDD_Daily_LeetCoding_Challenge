/**
 * Leetcode, 322.Coin Change https://leetcode.com/problems/coin-change/
 */

public class l_322_coin_change {
  /**
   * First solution Won't work -> Sorting coins blocks getting all possible
   * options
   */
  public int coinChange1(int[] coins, int amount) {
    Arrays.sort(coins);
    return coinHelper(coins, amount, coins.length - 1);
  }

  public int coinHelper1(int[] coins, int amount, int index) {
    if (index == 0 && amount % coins[index] != 0)
      return -1;
    if (index < 0)
      return -1;
    if (amount == 0)
      return 0;
    System.out.println("amount: " + amount);
    int a = amount / coins[index];

    System.out.println("a: " + a);

    if (a > 0)
      return a + coinHelper(coins, amount - (coins[index] * a), index - 1);
    else
      return coinHelper(coins, amount, index - 1);
  }

  /**
   * DP (Bottom-up) Solution
   * Key: get minimum value between the last possible options with the current possible options
   */
  public int coinChange(int[] coins, int amount) {
    // To keep all possible options for amount
    int[] coinNums = new int[amount + 1];
    Arrays.fill(coinNums, amount + 1);
    coinNums[0] = 0;

    for (int i = 1; i <= amount; ++i) {
      for (int j = 0; j < coins.length; ++j) {
        // if coin amount is smaller than the current amount
        if (coins[j] <= i)
          // compare between the last possible coin options and current + 1
          coinNums[i] = Math.min(coinNums[i], coinNums[i - coins[j]] + 1);
      }
    }

    /* Since we fill whole array with max value, 
     * if amount has not been replaced with number of options,
     * it means it can not be able to produced with the given coins
     */ 
    return coinNums[amount] > amount ? -1 : coinNums[amount];
  }
}
