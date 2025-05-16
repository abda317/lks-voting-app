using System;
using System.IO;
using System.Threading;

class Program
{
    static void Main()
    {
        string path = "/data/votes.txt";

        while (true)
        {
            if (File.Exists(path))
            {
                var lines = File.ReadAllLines(path);
                var summary = new System.Collections.Generic.Dictionary<string, int>();

                foreach (var vote in lines)
                {
                    if (!summary.ContainsKey(vote))
                        summary[vote] = 0;
                    summary[vote]++;
                }

                foreach (var item in summary)
                    Console.WriteLine($"{item.Key}: {item.Value}");
            }

            Thread.Sleep(10000); // tunggu 10 detik
        }
    }
}
