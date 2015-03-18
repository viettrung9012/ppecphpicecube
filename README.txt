EXPRESSCHECKOUT WITH PAYPAL DEMO

1) Live site here: http://ppecphpicecube-viettrung9012.rhcloud.com/index.php

2) There is also a Python version of the code because I worked on Python first but was unable to deploy

3) What I did:
	- Get source code from http://demo.paypal.com
	- Edit logo and item image
	- Modifies some parts in paypal_ec_redirect.php(.py) to make the calculation correct when quantity is changed
	- Edit index.php(.py) to remove demo explanation and to make the layout cleaner
	- Edit the form in index.php(.py) to enable changing the quantity of item to be bought
	- Use Openshift to host the demo online