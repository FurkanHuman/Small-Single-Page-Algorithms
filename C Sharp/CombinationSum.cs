using System;
using System.Collections.Generic;
using System.Linq;

namespace Kombinasyon
{
    class Program
    {
        static void Main(string[] args)
        {

            int[] arr = new int[] { 3, 5, -1, 8, 12 };
            int bigNumber = 0;
            for (int i = 0; i < arr.Length; i++)
            {
                if (bigNumber < arr[i])
                {
                    bigNumber = arr[i];
                }
            }
            int[] newArr = arr.Where((source, index) => index != Array.IndexOf(arr, bigNumber)).Distinct().ToArray();
            int[][] plus = Con(newArr).ToArray();
            bool result = false;
            for (int i = 0; i < plus.Length; i++)
            {
                int total = 0;
                for (int j = 0; j < plus[i].Length; j++)
                {

                    total += plus[i][j];


                }
                if (total == bigNumber)
                {
                    result = true;
                }

            }
            Console.WriteLine(result.ToString());

        }
        public static IEnumerable<T[]> Con<T>(T[] ts) where T : struct
        {
            T[] data = ts.ToArray();
            var str = Enumerable.Range(0, 1 << (data.Length));
            IEnumerable<T[]> str2 = str.Select(index =>
            data.Where((v, i) => (index & (1 << i)) != 0).ToArray());
            return str2;

            //v1 değişkenine ataması yapılırken indexi binary olarak karşılaştırır eğer binary basamakları eşleşirse v1 true döner
            //eğer index basamakları binary olarak eşleşmesse v1 i false döndürür 
            //eğer true dönerse dizinin i'nci elemanını yeni dizinin indexinci elemanının içine aktarır
        }
    }
}
