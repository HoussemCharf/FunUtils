import requests
import argparse

# get the inputted links
parser = argparse.ArgumentParser(description='Query spoopy.link to filter out bad links')
parser.add_argument("links", metavar="Link", help="links to filter")
args = parser.parse_args()
input_links = args.links


# function for checking the links (can of course be called separately for use in other code)
def check_links(links):
    bad_links = []

    for link in links:
        reasons = []

        # query the spoopy.link api
        resp = requests.get(f"https://spoopy.link/api/{link}")
        resp.raise_for_status()

        # read the response
        resp_json = resp.json()
        for c in resp_json['chain']:
            if not c['safe']:
                reasons.append(c['reasons'])

        # decide if the link is dangerous or not
        if reasons:
            bad_links.append({
                "link": link,
                "reason": ", ".join(reasons)
            })

    # return the links that are dangerous
    return bad_links


# get the links that are dangerous
checked_bad_links = check_links(input_links)

# return the bad links and their reason for being dangerous, or say that they're all safe
if checked_bad_links:
    return_text = "The following links are dangerous:\n"
    for bad_link in checked_bad_links:
        return_text += f"{bad_link['link']} raised: {bad_link['reason']}"
    print(return_text)
else:
    print("all links are safe!")
