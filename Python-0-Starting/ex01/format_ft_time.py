
import time

ts = time.time()

vdecimal = "{:.3e}".format(ts)


# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
print(f'Seconds since January 1, 1970: {ts:3,.4f} or {vdecimal} in scientific notation')

vgmtime = time.localtime(ts)
str = time.strftime("%b %d %Y", vgmtime)
print(str)
# Oct 21 2022$

