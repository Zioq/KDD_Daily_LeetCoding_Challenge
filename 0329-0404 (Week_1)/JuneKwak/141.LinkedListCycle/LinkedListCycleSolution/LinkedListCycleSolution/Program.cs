using System;
using System.Collections.Generic;

namespace LinkedListCycleSolution
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution method = new Solution();

            List<ListNode> listA = new List<ListNode>();
            listA.Add(new ListNode(3));
            listA.Add(new ListNode(2));
            listA.Add(new ListNode(0));
            listA.Add(new ListNode(-4));
            int posA = 1;
            bool isCycleA = true;

            method.ConstructList(listA, posA);

            method.PrintResult(isCycleA, method.HasCycle(listA), "A");

            List<ListNode> listB = new List<ListNode>();
            listB.Add(new ListNode(1));
            listB.Add(new ListNode(2));
            int posB = 0;
            bool isCycleB = true;

            method.ConstructList(listB, posB);

            method.PrintResult(isCycleB, method.HasCycle(listB), "B");


            List<ListNode> listC = new List<ListNode>();
            listC.Add(new ListNode(1));
            bool isCycleC = false;
            int posC = -1;

            method.ConstructList(listC, posC);
            method.PrintResult(isCycleC, method.HasCycle(listC), "C");
        }

        public class ListNode {
            public int val;
            public ListNode next;
            public ListNode(int x) {
                val = x;
                next = null;
            }

         }

        public class Solution
        {
            public bool HasCycle(List<ListNode> list)
            {
                ListNode head = list[0];
                if (head == null)
                {
                    return false;
                }
                List<ListNode> numList = new List<ListNode>();

                ListNode current = head;
                while (current != null)
                {
                    if (numList.Contains(current.next))
                    {
                        return true;
                    }
                    else
                    {
                        numList.Add(current);
                        current = current.next;
                    }
                }
                return false;
            }

            public void ConstructList(List<ListNode> list, int pos)
            {
                for (int i = 0; i < list.Count - 1; i++)
                {
                    if (list.Count <= 1)
                    {
                        break;
                    }
                    list[i].next = list[i + 1];
                }

                if (pos < 0)
                {
                    return;
                }
                list[list.Count - 1].next = list[pos];
            }

            public void PrintResult(bool isCycle, bool result, string type)
            {
                if (isCycle == result)
                {
                    Console.WriteLine($"{type} passed");
                }
                else
                {
                    Console.WriteLine($"{type} failed");
                }
            }
        }
    }

}
