using System;

namespace MissingNumberSolution
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution method = new Solution();
            int[] a = { 3, 0, 1};
            Console.WriteLine(method.MissingNumber(a));

            int[] b = { 0, 1 };
            Console.WriteLine(method.MissingNumber(b));

            int[] c = { 9, 6, 4, 2, 3, 5, 7, 0, 1 };
            Console.WriteLine(method.MissingNumber(c));

            int[] d = { 0 };
            Console.WriteLine(method.MissingNumber(d));
        }

        public class Solution
        {
            public int MissingNumber(int[] nums)
            {
                Array.Sort(nums);

                int n = nums.Length;
                for (int i = n - 1; i >= 0; i--)
                {
                    if (n != nums[i])
                    {
                        return n;
                    }
                    else
                    {
                        n--;
                    }
                }
                return n;
            }
        }
    }
}
