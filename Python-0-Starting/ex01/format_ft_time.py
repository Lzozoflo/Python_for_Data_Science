
import time

ts = time.time()

# vdecimal = "{:.3e}".format(ts)


# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific
#  notation$
print(
    f"Seconds since January 1, 1970: {ts:,.4f} or {ts:.2e} "
    "in scientific notation"
)

print(time.strftime("%b %d %Y", time.localtime(ts)))
# Oct 21 2022$
