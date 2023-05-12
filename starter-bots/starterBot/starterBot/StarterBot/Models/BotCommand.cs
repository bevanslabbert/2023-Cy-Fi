using StarterBot.Enums;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StarterBot.Models
{
    public class BotCommand
    {
        public Guid BotId { get; set; }
        public InputCommand Action { get; set; }
    }

    public class CyFiCommand : BotCommand
    {
        public CyFiCommand(Guid id, InputCommand action)
        {
            BotId = id;
            Action = action;
        }
    }
}
