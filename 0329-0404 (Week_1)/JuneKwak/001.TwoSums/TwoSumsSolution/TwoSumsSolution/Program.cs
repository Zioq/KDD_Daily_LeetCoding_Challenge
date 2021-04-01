// Question number: 1
// Question url: https://leetcode.com/problems/two-sum/
using System;

namespace TwoSumsSolution
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution twoSum = new Solution();
            int[] numA = new int[] { 2, 7, 11, 15 };
            int targetA = 9;
            twoSum.PrintSolution(twoSum.TwoSum(numA, targetA));

            int[] numB = new int[] { 3, 2, 4 };
            int targetB = 6;
            twoSum.PrintSolution(twoSum.TwoSum(numB, targetB));

            int[] numC = new int[] { 3, 3 };
            int targetC = 6;
            twoSum.PrintSolution(twoSum.TwoSum(numC, targetC));
        }

        public class Solution
        {
            public int[] TwoSum(int[] nums, int target)
            {
                int pivot = 0;
                int[] indexes = new int[2];
                int j = 0;
                for (int i = 0; i < nums.Length; i++)
                {
                    if (pivot == nums.Length)
                    {
                        break;
                    }
                    int pivotNum = nums[pivot];


                    if (((pivotNum + nums[i]) == target) && pivot != i)
                    {
                        indexes[j] = pivot;
                        indexes[j + 1] = i;
                    }

                    if (i == (nums.Length - 1))
                    {
                        pivot++;
                        i = 0;
                    }
                }


                return indexes;
            }

            public void PrintSolution(int[] indexes)
            {
                Console.Write($"[");
                for (int i = 0; i < indexes.Length; i++)
                {
                    Console.Write(indexes[i]);
                    if (i != indexes.Length-1)
                    {
                        Console.Write(",");
                    }
                }
                Console.WriteLine($"]");
            }
        }
    }

}
