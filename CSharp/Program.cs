using Blocket_ScraperCSharp.Mod;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;

namespace Blocket_ScraperCSharp
{
    class Program
    {
        private static List<Product> _products = new();

        static void Main(string[] args)
        {
            InstallAllReq();


            Console.WriteLine("Downloading all data...");

            string startupPath = Path.Combine(Directory.GetParent(System.IO.Directory.GetCurrentDirectory()).Parent.Parent.FullName, "blocket_scraper.py");

            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = @"python.exe";
            start.Arguments = startupPath;
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                    _products = JsonConvert.DeserializeObject<List<Product>>(result);
                }
            }

            foreach (var product in _products)
            {
                Console.WriteLine(product.Name);
            }
        }

        private static void InstallAllReq()
        {
            string req = Path.Combine(Directory.GetParent(System.IO.Directory.GetCurrentDirectory()).Parent.Parent.FullName, "requirements.txt");

            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = @"pip";
            start.Arguments = $"install -r {req}";
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            Process.Start(start);
        }
    }
}
