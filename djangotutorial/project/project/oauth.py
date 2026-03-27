# import random
# import string
# import base64
# import hashlib


## for user code athentication 
# code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128)))
# print(code_verifier)
# code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
# code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')
# print(code_challenge)




# client_id="KmW5uMN8pCnkzYH9n0HUuyjHgA9KN269hYf4qmSD"
# client_secret="pbkdf2_sha256$1200000$wkjgftTct2gllhhDRRL9b4$c4KXd1eNBBNgUaDBJW+ts3obMWJ/jM/BPHMwu8O7ebM="
# code_challenge="A4zeqxUtQ48P4zxzxJP9JE0uDd_7MUYhXw7_inHnrxs"
# code="66Z6xM9jnODDjmEC5Yr0VRJYHSFGQt"
# code_verifier="NKAI24RFTY3KPG0RJNATLC6BSD4D8TFH52Q3BO5SOIATGKDZIJSF128DH2CP3406I7QDA34EVA135SFOG5DOU3UM2K89MFN"
# access="g2nQ93cQ4VTBrFn9pCFtjuqZbhigUo"
# refresh="alMjv6jAIf9xYrDYntGv2BznqJnTp0"

#for client-credentials
import base64
client_id = "dfJ0q47gOF2SnSgaAPYHahoQ35jHKXLDrOiR357I"
secret = "Aebnsh4NvHGkpqHAVM36ivRWtfjf50DDJMwjz7TMjjy9kjA5RJodWFDxvdoGCmhrStfAKIV3QU4kWlgpYIl6bPmpyy9ObplcM3ESdaXtv3ryuDNBJgfyCGaXRImJf5DH"
credential = "{0}:{1}".format(client_id, secret)
base64.b64encode(credential.encode("utf-8"))

