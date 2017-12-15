from argparse import (
    ArgumentParser,
)


class WhatWafParser(ArgumentParser):

    def __init__(self):
        super(WhatWafParser, self).__init__()

    @staticmethod
    def cmd_parser():
        parser = ArgumentParser(prog="whatwaf.py", add_help=True, usage="./whatwaf.py -[u|l|L] [value] --[args]")

        mandatory = parser.add_argument_group("mandatory arguments",
                                              "arguments that have to be passed for the program to run")
        mandatory.add_argument("-u", "--url", dest="runSingleWebsite", metavar="URL",
                               help="Pass a single URL to detect the protection")
        mandatory.add_argument("-l", "--list", dest="runMultipleWebsites", metavar="PATH",
                               help="Pass a file containing URL's (one per line) to detect the protection")

        req_args = parser.add_argument_group("request arguments",
                                             "arguments that will control your requests")
        req_args.add_argument("--pa", dest="usePersonalAgent", metavar="USER-AGENT",
                              help="Provide your own personal agent to use it for the HTTP requests")
        req_args.add_argument("--ra", dest="useRandomAgent", action="store_true",
                              help="Use a random user-agent for the HTTP requests")
        req_args.add_argument("--proxy", dest="runBehindProxy", metavar="PROXY",
                              help="Provide a proxy to run behind in the format "
                                   "type://address:port (IE socks5://10.54.127.4:1080")
        req_args.add_argument("--tor", dest="runBehindTor", action="store_true",
                              help="Use Tor as the proxy to run behind, must have Tor installed")
        req_args.add_argument("-p", "--payloads", dest="providedPayloads", metavar="PAYLOADS",
                              help="Provide your own payloads separated by a comma IE AND 1=1,AND 2=2")
        req_args.add_argument("--pl", dest="payloadList", metavar="PAYLOAD-LIST-PATH",
                              help="Provide a file containing a list of payloads 1 per line")

        misc = parser.add_argument_group("misc arguments",
                                         "arguments that don't fit in any other category")
        misc.add_argument("--verbose", dest="runInVerbose", action="store_true",
                          help="Run in verbose mode (more output)")
        misc.add_argument("--hide", dest="hideBanner", action="store_true",
                          help="Hide the banner during the run")

        opts = parser.parse_args()

        return opts

