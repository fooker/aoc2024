#!/usr/bin/env python3

import sys
import importlib
import solutions.day01


if __name__ == "__main__":
    day = int(sys.argv[1])
    day = "day%02d" % (day, )

    mod = importlib.import_module("solutions.%s" % (day, ))
    
    def run(part):
        fn = getattr(mod, "part%d" % (part, ), None)

        if fn is None:
            print("Part %d not found" % (part, ), file=sys.stderr)
            return

        with open("inputs/%s" % (day, ), "rt") as data:
            result = fn(data)
            print("Part %d: %s" % (part, result))

    run(1)
    run(2)

