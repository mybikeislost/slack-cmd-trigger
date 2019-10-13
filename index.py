from __future__ import print_function
from datetime import date
from datetime import timedelta
import argparse
from slacker import Slacker


# generate a legacy token at https://api.slack.com/custom-integrations/legacy-tokens
apiKey = "LEGACY_API_KEY_HERE"

channels = [
     "discuss-storage",
     "discuss-workstations"
     ]

slashCmd = "clip"

days = 2 #default number of days to clip. 2 sets it to yesterday

def init_settings():
	global days
	parser = argparse.ArgumentParser()
	parser.add_argument('-w','--week', help='clip the previous 7 days.', nargs='?', const=1, default=False)
	parser.add_argument('-m','--month', help='clip the prior 31 days', nargs='?', const=1, default=False)
	args = parser.parse_args()

	# set the days to a weekly or monthly lookback, default to yesterday with no args.
	if args.week:
 		days = 8
	if args.month:
 		days = 32
	return args

def main():
	global settings
	today = date.today()
	try:
		settings = init_settings()
		slack = Slacker(apiKey)
		for c in channels:
			print("#"+c)
			for i in range(1,days): #for the prior 7 days use (1,8), to include today use (0,7)...
				clipDate =  (today - timedelta(days=i)).strftime("%m/%d/%Y")
				print("\tclipping:", clipDate)				
				channel_id = slack.channels.get_channel_id(c)
				slack.chat.command(
                    channel=channel_id,
                    command='/' + slashCmd,
                    text=clipDate
				)
			
	except (KeyboardInterrupt, SystemExit):
		print("-> Aborted through user interaction")


if __name__ == "__main__":
	main()
