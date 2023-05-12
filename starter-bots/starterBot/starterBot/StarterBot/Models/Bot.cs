
using Microsoft.Extensions.Logging;
using System;

namespace StarterBot.Models
{
    public class Bot
    {
      

        public int CurrentLevel;

        public Guid Id;

        public string NickName;

        public string ConnectionId;

        public DateTime LastUpdated;

        public int TotalPoints { get; set; }

        //Needed for SignalR unit test
        public Bot()
        {
        }

      
    }
}
