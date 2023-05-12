using Microsoft.AspNetCore.SignalR.Client;
using Microsoft.Extensions.Configuration;
using StarterBot.Models;
using StarterBot.Services;
using System;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;
using System.Diagnostics;
using System.Linq;


namespace StarterBot
{
    public class Program
    {
        public static IConfigurationRoot Configuration;

        private static async Task Main(string[] args)
        {
            // Set up configuration sources.
            var builder = new ConfigurationBuilder().AddJsonFile($"appsettings.json", optional: false);

            Configuration = builder.Build();

            var train = bool.Parse(Configuration.GetSection("train").Value);
            //OwnNNPlayer(train);

#if DEBUG
            if (train)
            {
                Process process;
                string strCmdText = System.IO.Path.Combine("..", "..", "..", "..", "..", "publish", "CyFi.exe");
                process = new Process();
                process.StartInfo.FileName = strCmdText;
                process.StartInfo.UseShellExecute = true;
                //process.StartInfo.CreateNoWindow = true;

                process.Start();

                process.StartInfo.WindowStyle = ProcessWindowStyle.Minimized;

                Thread.Sleep(7000);
            }
#endif

            await StarterBot();




        }


        static async Task StarterBot()
        {
            Stopwatch stopWatch = new Stopwatch();
            
            List<long> MoveTimer = new List<long>();
            bool isProcessing = false;

            var botName = Configuration.GetSection("botName").Value;
#if DEBUG
            botName = botName + "-debug";
#endif
            var registrationToken = Environment.GetEnvironmentVariable("Token");
            var environmentIp = Environment.GetEnvironmentVariable("RUNNER_IPV4");
            var ip = !string.IsNullOrWhiteSpace(environmentIp) ? environmentIp : Configuration.GetSection("RunnerIP").Value;
            ip = ip.StartsWith("http://") ? ip : "http://" + ip;

            var port = Configuration.GetSection("RunnerPort");

            var url = ip + ":" + port.Value + "/runnerhub";

            var connection = new HubConnectionBuilder()
                                .WithUrl($"{url}")
                                .ConfigureLogging(logging =>
                                {
                                    logging.SetMinimumLevel(LogLevel.Debug);
                                })
                                .WithAutomaticReconnect()
                                .Build();

            var botService = new BotService();

            await connection.StartAsync()
                .ContinueWith(
                    task =>
                    {
                        Console.WriteLine("Connected to Runner");
                        /* Clients should disconnect from the server when the server sends the request to do so. */
                        connection.On<Guid>(
                            "Disconnect",
                            (id) =>
                            {
                                Console.WriteLine("Disconnected:");
                               // Console.WriteLine("Max Population: "+botService.maxpopulation);
                                connection.StopAsync();
                                connection.DisposeAsync();
                            });
                        connection.On<Guid>(
                            "Registered",
                            (id) =>
                            {
                                Console.WriteLine("Registered Bot with the runner");
                                botService.SetBot(
                                    new Bot()
                                    {
                                        Id = id
                                    });
                            });

                        /* Get the current WorldState along with the last known state of the current client. */
                        connection.On<BotStateDTO>(
                            "ReceiveBotState",
                            (gameStateDto) =>
                            {
                                botService.SetGameState(gameStateDto);
                                var command = botService.GetPlayerCommand();
                                if (command != null)
                                    connection.InvokeAsync("SendPlayerCommand", command);

                            });

                        connection.On<object>("ReceiveGameComplete", (completeGameS) =>
                        {
                            Console.WriteLine($"Average time: {MoveTimer.Average()} Longest: {MoveTimer.Max()}");
                           // Console.WriteLine(JsonConvert.SerializeObject(completeGameS.WinningBot));
                           // Console. WriteLine(botService.maxpopulation + " score: " + completeGameS.Players.FirstOrDefault(x => x.Id == botService.GetBot().Id).Score);

                            connection.StopAsync();
                            connection.DisposeAsync();

                        });

                        var token = Environment.GetEnvironmentVariable("REGISTRATION_TOKEN");
                        token = !string.IsNullOrWhiteSpace(token) ? token : Guid.NewGuid().ToString();

                        Thread.Sleep(1000);
                        Console.WriteLine("Registering with the runner...");
                        connection.SendAsync("Register", botName);

                        while (connection.State == HubConnectionState.Connected)
                        {
                            Thread.Sleep(5);
                            //Console.WriteLine($"ConState: {connection.State}");
                            //Console.WriteLine($"Bot: {botService.GetBot()?.Id.ToString()}");

                            var bot = botService.GetBot();
                            if (bot == null)
                            {
                                continue;
                            }

                            if (botService.GetBot() != null)
                            {

                               //You can do stuff here if you want or on gamestate received

                            }

                        }
                        Console.WriteLine($"Average time: {MoveTimer.DefaultIfEmpty().Average()} Longest: {MoveTimer.DefaultIfEmpty().Max()}");
                      //  Console.WriteLine(botService.maxpopulation);

                    });
        }
    }
}
