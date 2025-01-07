# Given seconds (int) calculate hours, minutes, and seconds.
#   For example, given 80000 seconds that is
#   22 hours, 13 minutes, and 20 seconds.

secs_str = input("Input seconds: \n") # do not change this line
secs_int = int(secs_str)

# hours =
# minutes =
# seconds =
hours = secs_int // 3600

rfh = hours * 3600  #rfh = remainder from hours
R1 = secs_int - rfh

minutes = R1 // 60

rfm = minutes * 60 #rfm = remainder from mintues
R2 = R1 - rfm

seconds = R2


print(hours,":",minutes,":",seconds) # do not change this line
