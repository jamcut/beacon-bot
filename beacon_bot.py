import argparse
import requests

TEAM_SERVER_NAME = "UPDATE TEAM SERVER NAME"
TEAM_HOOK = 'UPDATE MS TEAMS WEBHOOK'


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--external-ip', help='External IP of Beacon')
    parser.add_argument('-i', '--internal-ip', help='Internal IP of Beacon', required=True)
    parser.add_argument('-u', '--user', help='Compromised user', required=True)
    parser.add_argument('-m', '--machine', help='Compromised machine', required=True),
    parser.add_argument('-a', '--arch', help='Architecture of compromised machine')

    args = parser.parse_args()
    if args.arch == '1':
        arch = 'x64'
    else:
        arch = 'x86'

    json = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "summary": "New Beacon Active!",
        "title": "New Beacon Active!",
        "themeColor": "FF1000",
        "sections": [{"facts": [
				{"name": "Team Server", "value": "{0}".format(TEAM_SERVER_NAME)},
                                {"name": "External IP", "value": "{0}".format(args.external_ip)},
                                {"name": "Internal IP", "value": "{0}".format(args.internal_ip)},
                                {"name": "User", "value": "{0}".format(args.user)},
                                {"name": "Hostname", "value": "{0}".format(args.machine)},
                                {"name": "Arch", "value": "{0}".format(arch)}
                               ]},
                    {"text": "I love the smell of shellz in the morning!"}]
    }

    headers = {'content-type': 'application/json'}

    resp = requests.post(TEAM_HOOK, json=json, headers=headers)

    print('[*] Posting message to Teams...')
    print('[*] Got status code: {0}'.format(str(resp.status_code)))

if __name__ == '__main__':
    main()
