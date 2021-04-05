using System;

namespace Solution
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();

            int[] a = { 3, 4, 5, 1, 2 };
            Console.WriteLine($"Minimum element of a is: {solution.FindMin(a)}");

            int[] b = { 4, 5, 6, 7, 0, 1, 2 };
            Console.WriteLine($"Minimum element of b is: {solution.FindMin(b)}");


            int[] c = { 11, 13, 15, 17 };
            Console.WriteLine($"Minimum element of c is: {solution.FindMin(c)}");
        }

        public class Solution
        {
            public int FindMin(int[] nums)
            {
                Array.Sort(nums);
                return nums[0];
            }
        }
    }
}
