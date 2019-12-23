
'''This Config python file have tenant id, cliend id and MISP key for accessing MISP portal Events
and also have misp domain name, misp event filter'''

graph_auth = {
    'tenant': '83a8ed06-53b4-4ea7-95e7-1fcfb93f84bc',
    'client_id': 'bbc59f15-f909-43e1-9acb-b2e94072fbe5',
    'client_secret': 'JdAOp?6VA5G6[0mgXmrWqn-U-i/L_j/x',
}
targetProduct = "Azure Sentinel"
misp_event_filters = [
    {
        "eventid": '1246'
    }
]
action = "allow"
passiveOnly = False
days_to_expire = 20
misp_key = 'pTJstoMcR1oLNyr1jXIVMLsq6sd8LXwqeHinxLdE'
misp_domain = 'https://192.168.0.22/'
misp_verifycert = False

