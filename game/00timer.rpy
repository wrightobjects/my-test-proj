init:
    python:
        def countdown(st, at, length = 0.0):
            remaining = length - st;
            if remaining > 5.0:
                return Text("%.3f" % remaining, color="fff", size=56), 0.05
            elif remaining > 3.0 and remaining < 5.0:
                return Text("%.3f" % remaining, color="f00", size=72), 0.05
            elif remaining > 1.0 and remaining < 3.0:
                return Text("%.3f" % remaining, color="f00", size=84), 0.05
            elif remaining > 0.0:
                return Text("%.3f" % remaining, color="f00", size=96), 0.05
            else:
                return anim.Blink(Text("0.0", color="#f00", size=84)), None
