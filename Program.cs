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
        static void Main(string[] args)
        {

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
                    Console.WriteLine(result);
                    List<Product> products = JsonConvert.DeserializeObject<List<Product>>(result);
                }
            }
        }
    }
}
