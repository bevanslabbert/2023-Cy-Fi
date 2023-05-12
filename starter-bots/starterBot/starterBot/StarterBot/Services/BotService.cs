using StarterBot.Enums;
using StarterBot.Models;
using System;

namespace StarterBot.Services
{
    public class BotService
    {
        private Bot _bot;
        private BotStateDTO _gameState;

        public BotService()
        {
           _bot = new Bot();
        }

        public Bot GetBot()
        {
            return _bot;
        }

        public CyFiCommand GetPlayerCommand()
        {


            return new CyFiCommand(_bot.Id, InputCommand.UPRIGHT);
        }



        public void SetBot(Bot bot)
        {
            _bot.Id = bot.Id;
        }

        public BotStateDTO GetGameState()
        {
            return _gameState;
        }

        public void SetGameState(BotStateDTO gameState)
        {
            _gameState = gameState;
            PrintJaggedArray(_gameState.HeroWindow);
        }


        public void PrintJaggedArray<T>(T[][] matrix)
        {
            Console.Clear();
            for (int i = 0; i < matrix.Length; i++)
            {
                for (int j = 0; j < matrix[i].Length; j++)
                {
                    Console.Write(matrix[i][j]);
                }
                Console.WriteLine();
            }

        }

    }
}