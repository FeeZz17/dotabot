import httpx
def get_benchmarks():

    

    pass

def gpm_hero(response):
    gpm = response["result"]['gold_per_min']
    for i in gpm:
        if i["percentile"] in [0.5]:
            return i["value"]

def xpm_hero(response):
    xpm = response["result"]["xp_per_min"]
    for i in xpm:
        if i["percentile"] in [0.5]:
            return i["value"]