﻿using System.Collections.Generic;

namespace StarterBot.Healpers
{
    public static class ListHealper
    {
        public static T RemoveAndReturnFirst<T>(this List<T> list)
        {
            if (list == null || list.Count == 0)
            {
                // Instead of returning the default,
                // an exception might be more compliant to the method signature.

                return default(T);
            }

            T currentFirst = list[0];
            list.RemoveAt(0);
            return currentFirst;
        }
    }
}